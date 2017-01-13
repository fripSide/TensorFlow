# coding: utf-8
__author__ = 'fripSide'

import subprocess
import shlex
import sys
import pipes
import os

def test_subprocess():
    """
    args string or a sequence of args
    If passing a single string, either shell must be True (see below) or else the string must simply name the program to be executed without specifying any arguments.
    如果只有一个参数，就需要指定shell，表示在shell中执行命令
    :return:
    """
    subprocess.call(["ls", "-la"], stdin=sys.stdin, stdout=sys.stdout)
    subprocess.check_call("ls", stdout=sys.stdout, shell=False)
    print shlex.split("sadas dasdsa asd")
    filename = "something; ls ~"
    command = "ls -l {}".format(pipes.quote(filename))
    print(command)
    remote_command = "ssh home {}".format(pipes.quote(command))
    print(remote_command)

test_subprocess()

"""
os.popen()已经被废弃了

"""
def child(pipeout):
  bottles = 99
  n = 3
  while n:
    n -= 1
    bob = "bottles of beer"
    otw = "on the wall"
    take1 = "Take one down and pass it around"
    store = "Go to the store and buy some more"

    if bottles > 0:
      values =  (bottles, bob, otw, bottles, bob, take1, bottles - 1,bob,otw)
      verse = "%2d %s %s,\n%2d %s.\n%s,\n%2d %s %s." % values
      os.write(pipeout, verse)
      bottles -= 1
    else:
      bottles = 99
      values =  (bob, otw, bob, store, bottles, bob,otw)
      verse = "No more %s %s,\nno more %s.\n%s,\n%2d %s %s." % values
      os.write(pipeout, verse)

def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        counter = 1
        n = 3
        while n:
            n -= 1
            if counter % 100:
                verse = os.read(pipein, 117)
                print(len(verse))
            else:
                verse = os.read(pipein, 128)
            print 'verse %d\n%s\n' % (counter, verse)
            counter += 1

def parent2():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        os.close(pipein)
        child(pipeout)
    else:
        os.close(pipeout)
        counter = 1
        pipein = os.fdopen(pipein)
        n = 3
        while n:
            n -= 1
            print 'verse %d' % (counter)
            for i in range(4):
                verse = pipein.readline()[:-1]
                print '%s' % (verse)
            counter += 1
            print
# parent2()

# Bidirectional Pipes
import os, sys, random


def deviser(max):
    fh = open("deviser.log","w")
    to_be_guessed = int(max * random.random()) + 1

    guess = 0
    while guess != to_be_guessed:
        guess = int(raw_input())
        fh.write(str(guess) + " ")
        if guess > 0:
            if guess > to_be_guessed:
                print 1
            elif guess < to_be_guessed:
                print -1
            else:
                print 0
            sys.stdout.flush()
        else:
            break
    fh.close()

def guesser(max):
    fh = open("guesser.log","w")
    bottom = 0
    top = max
    fuzzy = 10
    res = 1
    while res != 0:
        guess = (bottom + top) / 2
        print guess
        sys.stdout.flush()
        fh.write(str(guess) + " ")
        res = int(raw_input())
        if res == -1: # number is higher
            bottom = guess
        elif res == 1:
            top = guess
        elif res == 0:
            message = "Wanted number is %d" % guess
            fh.write(message)
        else: # this case shouldn't occur
            print "input not correct"
            fh.write("Something's wrong")


def test_bi():
    n = 100
    stdin  = sys.stdin.fileno() # usually 0
    stdout = sys.stdout.fileno() # usually 1

    parentStdin, childStdout  = os.pipe()
    childStdin,  parentStdout = os.pipe()
    pid = os.fork()
    if pid:
        # parent process
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin,  stdin)
        os.dup2(parentStdout, stdout)
        deviser(n)
    else:
        # child process
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin,  stdin)
        os.dup2(childStdout, stdout)
        guesser(n)


def echo_server(read_in, write_out):
    n = 3
    fp = os.fdopen(read_in)
    while n:
        n -= 1
        res = fp.readline()
        print("server recv:" + res, n)
        os.write(write_out, res)


def send_client(read_in, write_out):
    n = 3
    fp = os.fdopen(read_in)
    while n:
        n -= 1
        import time
        time.sleep(1)
        os.write(write_out, "haha")
        print("client send ", n)
        res = fp.readline()
        print("echo " + res, n)

# client_in -> third_in -> server_in -> server_out -> third_out -> client_out
# client_in -> client_out -> server_in -> server_out -> client_in
# 关闭自己不需要的一端
# http://xiaorui.cc/2014/12/10/%E4%BD%BF%E7%94%A8pipe%E7%AE%A1%E9%81%93%E4%BD%BFpython-fork%E5%A4%9A%E8%BF%9B%E7%A8%8B%E4%B9%8B%E9%97%B4%E9%80%9A%E4%BF%A1/
def run_echo1():
    server_in, client_out = os.pipe()
    client_in, server_out = os.pipe()
    # third_in, third_out = os.pipe()
    if os.fork() == 0:
        # child, client
        os.close(server_in)
        os.close(server_out)
        # os.close(server_in)

        print("start client")
        send_client(client_in, client_out)
    else: # server
        os.close(client_in)
        os.close(client_out)
        print("start server")
        echo_server(server_in, server_out)

# run_echo1()


import os, time, sys
pipe_name = 'pipe_test'

def child( ):
    pipeout = os.open(pipe_name, os.O_WRONLY) # 只写
    counter = 0
    n = 10
    while n:
        n -= 1
        time.sleep(1)
        os.write(pipeout, 'Number %03d\n' % counter)
        counter = (counter+1) % 5

def parent( ):
    pipein = open(pipe_name, 'r')
    n = 10
    while n > 0:
        n -= 1
        line = pipein.readline()[:-1]
        print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time( ))

def run_name_pipe():
    if not os.path.exists(pipe_name):
        os.mkfifo(pipe_name)
    pid = os.fork()
    if pid != 0:
        parent()
    else:
        child()