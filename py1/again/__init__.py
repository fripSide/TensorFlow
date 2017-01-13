# coding: utf-8
__author__ = 'fripSide'

from PyLuaTblParser import PyLuaTblParser, Tokenizer
import traceback
import sys
import pprint

def test1():
    """
    单个测试用例
    """
    p = PyLuaTblParser()
    with open("t1.txt", "r") as fp:
        for idx, line in enumerate(fp):
            if line.isspace() or line.startswith("#") or line.startswith("--"):
                # print("Pass Comment")
                pass
            else:
                print("Line {}:".format(idx + 1))
                p.load(line)
                print(p.dump())
                p2 = PyLuaTblParser()
                p2.loadDict(p.dumpDict())
                print(p2.dump())
                # print(Tokenizer(line).get_tokens())

def test2():
    """
    组合用例
    """
    p1 = PyLuaTblParser()
    p2 = PyLuaTblParser()
    p3 = PyLuaTblParser()
    p1.loadLuaTable("t2_in.txt")
    # p1.dumpLuaTable("t2_out.txt")
    p2.loadDict(p1.dumpDict())
    p2.dumpLuaTable("t2_out.txt")
    p3.loadLuaTable("t2_in.txt")
    print(p1.dump())
    print(p2.dump())
    print(p3.dump())

def test3():
    parser = PyLuaTblParser()
    parser.loadLuaTable("t3.txt")
    pprint.pprint(parser.dumpDict())
    print(parser.dump())

def test4():
    ts = '{[""]="", ['']="", [\' \']= \'\'}'
    with open("t3.txt", "r") as fp:
        ts = fp.read()
    tokens = Tokenizer(ts).get_tokens()
    print(tokens)
    print(" | ".join(tokens))

if __name__ == "__main__":
    test1()
    test2()
    test3()