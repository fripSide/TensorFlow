# coding: utf-8
__author__ = 'fripSide'

from slpp import slpp as lua

data = lua.decode("{['false']=[===[false]===],['true']=True}")

print(data)