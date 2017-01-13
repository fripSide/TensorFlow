# coding: utf-8
__author__ = 'fripSide'

import json
import base64
import errno
import socket
import threading
import sys
import Queue
from collections import namedtuple
import py2.config as config


class ChatMessage(object):
    """
    cmd: login,
    """

    def __init__(self, user=""):
        self.data = {}
        self.msg = ""
        self.msg_from = user
        self.msg_to = ""
        self.status = True

    def get_data(self):
        self.data["msg_from"] = self.msg_from
        # self.data["msg_to"] = self.msg_to
        raw = self._encrypt(json.dumps(self.data))
        l1 = chr(len(raw) / 256)
        l2 = chr(len(raw) % 256)
        msg = l1 + l2 + raw
        # print(l1, l2, msg, len(raw))
        return l1 + l2 + raw

    def add_data(self, key, value):
        self.data[key] = value

    def _encrypt(self, raw):
        data = base64.b64encode(raw)
        return data

    @staticmethod
    def decrypt(raw):
        return base64.b64decode(raw)


class ChatClient(object):
    COMMANDS = ["chat", "chatall", "talk", "create", "enter", "leave", "login", "register"]

    def __init__(self, host="", port=None):
        self.host = host or config.ADDR
        self.port = port or config.PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None
        self.addr = None
        self.name = ""
        self.is_login = False
        # self.recv_queue = None

    def start(self):
        # try:
            self.sock.connect((self.host, self.port))
            self.start_to_recv()
            self.loop()

        # except Exception as ex:
        #     print(ex.message)


    def login(self, params):
        if len(params) == 3 and params[0] == "login":
            name, psw = params[1], params[2]
            self.send_command("login", dict(name=name, password=psw))
            self.name = name
        else:
            print("Incorrect params.")

    def register(self, params):
        if len(params) == 3 and params[0] == "register":
            name, psw = params[1], params[2]
            self.send_command("register", dict(name=name, password=psw))
            self.name = name
        else:
            print("Incorrect params.")


    def _send(self, data):
        total_send = 0
        raw = data
        while len(data):
            try:
                send = self.sock.send(data)
                total_send += send
                data = data[send:]
            except socket.error, e:
                if e.errno != errno.EAGAIN:
                    """there is no data available right now, try again later."""
                    raise e
                print("exception")
        # print("send ", raw, len(raw))
        return total_send


    def _recv_msg(self):
        l = self.sock.recv(2)
        le = ord(l[0]) * 256 + ord(l[1])
        raw = self.sock.recv(le)
        data = ChatMessage.decrypt(raw)
        # print("recv", le, raw, data)
        return json.loads(data)


    def send_command(self, cmd, data):
        msg = ChatMessage(user=self.name)
        msg.data["cmd"] = cmd
        for key in data:
            msg.add_data(key, data[key])
        self._send(msg.get_data())

    def start_to_recv(self):
        def recv_thread():
            while True:
                # print("try to receive...")
                msg = self._recv_msg()
                if msg["cmd"] == "register":
                    print(msg["msg"])
                elif msg["cmd"] == "login":
                    if msg["success"]:
                        self.is_login = True
                    print(msg["msg"])
                elif msg["cmd"] == "msg":
                    s = "[%s to %s]: " % (msg["msg_from"], msg["msg_to"])
                    print(s + msg["msg"])
                elif msg["cmd"] == "show":
                    print(msg["msg"])
                else:
                    print(msg["msg"])

        th = threading.Thread(target=recv_thread)
        th.daemon = True
        th.start()
        # th.join()


    def _on_message(self, msg):
        pass

    def loop(self):
        while True:
            line = sys.stdin.readline()
            items = line.split()
            if not items:
                continue
            elif items[0] == "exit":
                break
            elif not self.is_login:
                if items[0] == "login":
                    self.login(items)
                elif items[0] == "register":
                    self.register(items)
            else:
                if items[0] == "chat":
                    # print("chattting")
                    self.send_command("chat", dict(msg=items[1]))
                elif items[0] == "chatall":
                    self.send_command("chatall", dict(msg=items[1]))
                elif items[0] == "talk":
                    if len(items) == 3:
                        self.send_command("talk", dict(msg_to=items[1], msg=items[2]))
                    else:
                        print("Usage: talk [user] [message]")
                elif items[0] == "create":
                    self.send_command("create", {})
                elif items[0] == "enter":
                    if len(items) == 2:
                        try:
                            rid = int(items[1])
                            self.send_command("enter", dict(msg=rid))
                        except:
                            print("Please input 'enter [integer]'.")
                    else:
                        print("Usage: enter [id]")
                elif items[0] == "leave":
                    self.send_command("leave", {})
                elif items[0] == "21game":
                    if len(items) == 2:
                        self.send_command("21game", dict(msg=items[1]))
                    else:
                        print("Usage: 21game [1+2*10]. (express should not contains space.)")
                elif items[0] == "logout":
                    self.is_login = False
                    self.send_command("logout", {})
                elif items[0] == "help":
                    self.send_command("help", {})
                else:
                    print("Unrecognized command %s." % items[0])
                    self.send_command("help", {})

        self.sock.close()

if __name__ == "__main__":
    client = ChatClient()
    client.start()