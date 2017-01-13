# coding: utf-8
__author__ = 'fripSide'

import socket
import re
import errno
import json
import Queue
import threading
import cPickle
import base64
import select
import datetime
import random
import hashlib
from collections import namedtuple
import py2.config as config

DEBUG = True

def log(*m):
    if DEBUG:
        print(m)

support = """
Server support commands:
 help - show help information
 exit - client exit
 login [username] [password] - user login
 register [username] [password] - user register
 logout - user logout
 talk [username] [message]
 enter [integer] - enter room#id
 leave - leave room
 create - create a new room
"""


User = namedtuple("User", ["name", "psw", "online", "last_login", "total_time"])

class ChatClient(object):

    def __init__(self, conn, addr):
        self.room = None
        self.addr = addr
        self.conn = conn
        self.name = ""

    def recv(self):
        l = self._recv(2)
        if not l:
            return None
        # print(l, len(l))
        le = ord(l[0]) * 256 + ord(l[1])
        # print(l[0], l[1], l, le)
        raw = self._recv(le)
        pack = ChatMessage.decrypt(raw)
        pack = json.loads(pack)
        # print(pack)
        return pack

    def send(self, msg):
        if isinstance(msg, ChatMessage):
            msg = msg.encrypt()
        l = len(msg)
        le = chr(l / 256) + chr(l % 256)
        self._send(le + msg)

    def _send(self, data):
        total = len(data)
        cur = 0
        while cur < total:
            try:
                cur += self.conn.send(data[cur:])
            except:
                break
        return total

    def _recv(self, total):
        data = ""
        while total:
            d = self.conn.recv(total)
            if not d:
                print("Recv end", d, len(data))
                return data
            total -= len(d)
            data += d
        return data

    def __hash__(self):
        return repr(self.addr) + repr(self.name)

class ChatRoom(object):
    """
    0为大厅，
    """
    def __init__(self, id, name):
        self.id = id
        self.users = []
        self.tag = name
        self.game = Game21(self)
        self.game.room = self

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        user.room = self
        if self.id != 0:
            ret = ChatMessage(self.tag)
            ret.cmd = "msg"
            ret.msg = "You have entered room#%d." % self.id
            ret.msg_to = user.name
            ret.msg_from = self.tag
            user.send(ret.encrypt())
            for u in self.users:
                if u is not user:
                    ret.msg = "%s have entered this room." % user.name
                    u.send(ret.encrypt())


    def get_name_list(self):
        names = []
        for usr in self.users:
            names.append(usr.name)
        return names


class ChatMessage(object):
    commands = ["login", "chat", "talk", "create", "join", "leave", "exit", "21game"]

    def __init__(self, to_user="", **kwargs):
        self.data = {}
        self.msg = kwargs.get("msg", "")
        self.msg_from = kwargs.get("msg_from", "server")
        self.msg_to = to_user or kwargs.get("msg_to")
        self.cmd = kwargs.get("cmd", "show")
        self.success = True

    @staticmethod
    def decrypt(raw):
        return base64.b64decode(raw)

    def encrypt(self):
        # for atr in self.__dict__:
        #     print(atr, self.__dict__[atr])
        self.data["msg"] = self.msg
        self.data["cmd"] = self.cmd
        self.data["msg_from"] = self.msg_from
        self.data["msg_to"] = self.msg_to
        self.data["success"] = self.success
        data = json.dumps(self.data)
        return base64.b64encode(data)

class EventHandler(object):

    def __init__(self, s):
        self.server = s
        self.cmd = ""

    def handle(self, msg, client):
        pass

class LoginHandler(EventHandler):

    def _user_is_login(self, name):
        if name in self.server.users:
            return self.server.users[name].is_login
        return False

    def handle(self, msg, client):
        # print("Login Cmd", msg)
        if msg["cmd"] == "logout":
            self._handle_logout(msg, client)
            return
        name = msg.get("name", "")
        psw = msg.get("password", "")
        ret = ChatMessage(name)
        # u = User(name=name, psw=psw, online=False)
        if name in self.server.users:
            usr = self.server.users[name]
            client.name = name
            ret.cmd = "login"
            if usr.online:
                ret.success = False
                ret.msg = "Current user[%s] has already login!" % name
            elif psw == usr.psw:
                names = ", ".join(self.server.hall.get_name_list())
                status = self.server.get_user_status(name)
                ret.msg = "Login Success! " + status + support
                ret.msg += "You are current in hall.\n Current users: " + names + "\n Use 'chatall [message]' to talk to others."
                usr = usr._replace(online=True)
                usr = usr._replace(last_login = datetime.datetime.now())
                self.server.users[name] = usr
                print("Login Success, ", usr, psw)
            else:
                ret.success = False
                ret.msg = "Invalid username or password."
            client.send(ret.encrypt())
        else:
            print("Login Failed, ", name, psw)
            ret.msg = "Login Failed!\n Usage: login username password\n"
            ret.success = False
            client.send(ret.encrypt())

    def _handle_logout(self, msg, client):
        ret = ChatMessage()
        ret.msg = "%s have logout." % client.name
        for usr in client.room.users:
            usr.send(ret)
        if client in client.room.users:
            client.room.users.remove(client)
        self.server.hall.add_user(client)
        u = self.server.users[client.name]
        u = u._replace(online=False)
        self.server.update_users(u)


class RegisterHandler(EventHandler):

    def handle(self, msg, client):
        u = User(name=msg["name"], psw=msg["password"], online=False,
                 last_login=datetime.datetime.now(),
                       total_time=datetime.timedelta(0))
        ret = ChatMessage(u.name)
        ret.cmd = "register"
        if u.name in self.server.users:
            ret.success = False
            ret.msg = "Current user name is used."
        else:
            ret.msg = "Register success."
            self.server.update_users(u)
        client.send(ret.encrypt())


class RoomHandler(EventHandler):

    def handle(self, msg, client):
        cmd = msg["cmd"]
        if cmd == "chat":
            if self.server.hall.id != client.room.id:
                self._handle_chat(msg, client, client.room)
            else:
                ret = ChatMessage(client.name)
                ret.msg = "You are currently in hall. Use 'chatall [message]' to talk in hall."
                print("whererererer", len(self.server.rooms))
                if len(self.server.rooms) > 0:
                    ret.msg += "\nCurrent room list:\n"
                    ret.msg += ", ".join(self.server.get_rooms_list())
                    ret.msg += "\nUse 'enter [id]' to enter a room."
                else:
                    ret.msg += "\nThere no chat rooms. Use 'create' to create one."
                client.send(ret.encrypt())
        elif cmd == "chatall":
            self._handle_chat(msg, client, self.server.hall)
        elif cmd == "create":
            self._handle_create(msg, client)
        elif cmd == "talk":
            self._handle_talk(msg, client)
        elif cmd == "enter":
            self._handle_enter(msg, client)
        elif cmd == "leave":
            self._handle_leave(msg, client)

    def _handle_chat(self, msg, client, room):
        ret = ChatMessage(client.name)
        ret.cmd = "msg"
        ret.msg_from = client.name
        ret.msg_to = room.tag
        ret.msg = msg["msg"]
        for c in room.users:
            c.send(ret.encrypt())
        if room.id == 0 and client.room.id != 0:
            client.send(ret.encrypt())

    def _handle_create(self, msg, client):
        rid = 1
        for r in self.server.rooms:
            if not rid == r.id:
                break
            else:
                rid += 1
        name = "room#%d" % rid
        nr = ChatRoom(rid, name)
        self.server.rooms.append(nr)
        ret = ChatMessage(client.name)
        ret.msg = "You have create room [%s] room id is %d." % (name, rid)
        ret.msg += "\nCurrent room list:\n"
        ret.msg += ", ".join(self.server.get_rooms_list())
        client.send(ret.encrypt())

    def _handle_talk(self, msg, client):
        ret = ChatMessage(client.name)
        ret.cmd = "msg"
        ret.msg_from = client.name
        ret.msg_to = msg["msg_to"]
        ret.msg = msg["msg"]
        name = msg["msg_to"]
        other = self.server.get_user_client(name)
        if not other:
            ret.cmd = "show"
            ret.msg = "User %s is not online." % name
        client.send(ret.encrypt())
        other.send(ret.encrypt())

    def _handle_enter(self, msg, client):
        rid = msg["msg"]
        nr = None
        for r in self.server.rooms:
            if r.id == rid:
                nr = r
                break
        ret = ChatMessage(client.name)
        if nr:
            # if client.room.id != 0:
            if client in client.room.users:
                client.room.users.remove(client)
            client.room = nr
            nr.add_user(client)
        else:
            ret.msg = "Cannot find room#%d." % rid
            if len(self.server.rooms) > 0:
                ret.msg += "\nCurrent room list:\n"
                ret.msg += ", ".join(self.server.get_rooms_list())
            else:
                ret.msg += "\nThere no chat rooms. Use 'create' to create one."
        client.send(ret.encrypt())

    def _handle_leave(self, msg, client):
        if client.room.id != 0:
            client.room.users.remove(client)
        tag = client.room.tag
        old = client.room
        client.room = self.server.hall
        ret = ChatMessage()
        ret.msg_from = client.name
        ret.msg_to = tag
        ret.msg = "%s have leaved %s." % (client.name, tag)
        for usr in old.users:
            # print("", usr.name)
            usr.send(ret)
        ret.msg = "You have leaved %s." % tag
        client.send(ret)

class Game21(object):
    """ 21点游戏控制
    """
    def __init__(self, room):
        self.start_time = datetime.datetime.now()
        self.finished = True
        self.winner = ""
        self.mi = 21
        self.room = room
        self.nums = []
        self.ans = {}

    def check_start(self):
        m = datetime.datetime.now().minute
        ti = datetime.datetime.now() - self.start_time
        ret = ChatMessage()
        if ti > datetime.timedelta(minutes=20) and not self.finished:
            ret.msg = "21 Game [%s] is end. Winner is %s" % (", ".join(self.nums), self.winner)
            for client in self.room.users:
                client.send(ret)
            self._new_game()
        if ((m == 0 or m == 30) and not self.nums) or not self.nums:
            self._new_game()
        ret.msg = "21 Game is running: [%s]." % ", ".join(self.nums)
        if not self.finished:
            for client in self.room.users:
                if client.name not in self.ans:
                    self.ans[client.name] = 0
                    client.send(ret)

    def _new_game(self):
        self.finished = False
        self.nums = [str(random.randint(1, 10)) for i in range(4)]
        self.ans = {}
        self.start_time = datetime.datetime.now()

class Game21Handler(EventHandler):

    def handle(self, msg, client):
        exp = msg["msg"]
        room = client.room
        ret = ChatMessage()
        ret.cmd = "msg"
        ret.msg_from = room.tag
        ret.msg_to = client.name
        if room.game.ans[client.name] > 0:
            ret.msg = "You have answered the round! You can only answer once."
            client.send(ret)
            return
        if room.id == 0:
            return
        nums = room.game.nums
        dd = re.split("\+|\-|\*|/|\(|\)", exp)
        # print(dd)
        valid = True
        for d in dd:
            try:
                if d and d not in nums:
                    # print("not in", d, nums)
                    valid = False
            except:
                # print("except")
                valid = False
                break
        print(exp, valid, dd)
        try:
            val = eval(exp)
            room.game.ans[client.name] = val
            if val < 21 and 21 - val < room.game.mi:
                room.game.mi = 21 -val
                room.game.winner = "%s[%s]" % (client.name, exp)
            if room.game.mi == 0:
                room.game.finished = True
                room.game.nums = []
                ret.msg = "You win %s=21!" % exp
            else:
                ret.msg = "You have submit %s=%d success." % (exp, val)
        except:
            valid = False


        if not valid:
            ret.msg = "Invalid express %s." % exp
            ret.msg += "\n Nums are [%s]." % ", ".join(room.game.nums)
        client.send(ret)

class ChatServer(object):
    PROFILE = "profile"

    def __init__(self, host="", port=None):
        self.host = host or config.ADDR
        self.port = port or config.PORT
        self.clients = {}
        self.rooms = []
        self.users = {}
        self.send_queue = {}
        self.event_handlers = {}
        self._init_event_handlers()
        self.hall = ChatRoom(0, "hall")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))

    def start(self):
        self._load_users()
        print("Start to listen at {}:{}".format(repr(self.host), self.port))
        self.sock.listen(5)
        inputs = [self.sock]
        outputs = []
        while inputs:
            readable, writable, exceptional = select.select(inputs, outputs, inputs)
            for s in readable:
                if s is self.sock:
                    conn = self.handle_client()
                    inputs.append(conn)
                else:
                    print("Recv from client", s)
                    client = self.clients[s]
                    msg = client.recv()
                    if msg:
                        server.dispatch_message(msg, client)
                        if s not in outputs:
                            outputs.append(s)
                    else:
                        # client is close, remove client
                        log("client is close", s)
                        if s in outputs:
                            outputs.remove(s)

                        self.user_exit(client)
                        inputs.remove(s)
                        s.close()

            for s in writable:
                pass
            for r in self.rooms:
                r.game.check_start()

    def user_exit(self, client):
        # remove from room
        if client in client.room.users:
            client.room.users.remove(client)

        # update status
        name = client.name
        if name in self.users:
            u = self.users[name]
            u = u._replace(online = False)
            n_total = u.total_time +  datetime.datetime.now() - u.last_login
            u = u._replace(total_time = n_total)
            self.users[name] = u
            self.update_users(u)

    def get_user_client(self, name):
        for c in self.clients:
            client = self.clients[c]
            if client.name == name:
                return client
        return None

    def get_user_status(self, name):
        usr = self.users[name]
        s1 = usr.last_login.strftime("%Y-%m-%d %H:%M:%S")
        s2 = str(usr.total_time)
        status = "Last login: %s online time: %s" % (s1, s2)
        return status

    def get_rooms_list(self):
        rl = []
        for r in self.rooms:
            rl.append("room#%d" % r.id)
        return rl

    def handle_client(self):
        conn, addr = self.sock.accept()
        print("New Client comes, ", conn, addr)
        conn.setblocking(0)
        client = ChatClient(conn, addr)
        self.clients[conn] = client
        self.hall.add_user(client)
        login = ChatMessage(client.name)
        # login.cmd = "login"
        login.msg = "Welcome to Westworld!\nPlease login or register:\n login/register [username] [password]"
        client.send(login.encrypt())
        return conn

    def create_test_users(self):
        users = []
        for i in range(1, 5):
            usr = User(name="netease" + str(i), psw="123",
                       online=False, last_login=datetime.datetime.now(),
                       total_time=datetime.timedelta(0))
            users.append(usr)
        self._save_users(users)

    def _load_users(self):
        with open("user.dat", "rb") as fp:
            data = fp.read()
        data = base64.b64decode(data)
        data = cPickle.loads(data)
        for u in data:
            self.users[u.name] = u._replace(online=False)

    def _save_users(self, users):
        data = cPickle.dumps(users)
        data = base64.b64encode(data)
        with open("user.dat", "wb") as fp:
            fp.write(data)

    def _init_event_handlers(self):
        login = LoginHandler(self)
        self.event_handlers["login"] = login
        self.event_handlers["register"] = RegisterHandler(self)
        self.event_handlers["logout"] = login
        # room
        room = RoomHandler(self)
        self.event_handlers["create"] = room
        self.event_handlers["enter"] = room
        self.event_handlers["chat"] = room
        self.event_handlers["chatall"] = room
        self.event_handlers["talk"] = room
        self.event_handlers["leave"] = room

        self.event_handlers["21game"] = Game21Handler(self)


    def update_users(self, usr=None):
        if usr:
            self.users[usr.name] = usr

        def async_save_users(*users):
            self._save_users(users)
        th = threading.Thread(target=async_save_users, args=(self.users.values()))
        th.daemon = True
        th.start()

    def dispatch_message(self, msg, client):
        print("Recv Client Data: ", msg)
        cmd = msg["cmd"]
        if cmd in self.event_handlers:
            self.event_handlers[cmd].handle(msg, client)
        elif cmd == "help":
            ret = ChatMessage(client.name)
            ret.msg = "You are current in chat room#%d" % client.room.id
            ret.msg += support
            client.send(ret.encrypt())
        else:
            ret = ChatMessage(client.name)
            ret.msg = "Unrecognized command!" + support
            client.send(ret.encrypt())


if __name__ == "__main__":
    server = ChatServer()
    # server.create_test_users()
    server.start()
