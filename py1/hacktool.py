
# 参考这个重写
# https://github.com/IpursueI/LuaTableParser/blob/master/PyLuaTblParser.py
#
# https://github.com/dxsooo/MyParser/blob/master/PyLuaTblParser.py

def create_func_by_name(s, name, func):
    def y(s):
        func(s)
    y.__name__ = name
    y(s)


def hackfun(s):
    if not s:
        raise Exception()
    else:
        create_func_by_name(s[1:], s[0], hackfun)

def getcase(s):
    if not s:
        raise Exception
    elif ord(s[0]) == 0:
        getcase(s[1:])
    elif ord(s[0]) == 1:
        getcase(s[1:])
    elif ord(s[0]) == 2:
        getcase(s[1:])
    elif ord(s[0]) == 3:
        getcase(s[1:])
    elif ord(s[0]) == 4:
        getcase(s[1:])
    elif ord(s[0]) == 5:
        getcase(s[1:])
    elif ord(s[0]) == 6:
        getcase(s[1:])
    elif ord(s[0]) == 7:
        getcase(s[1:])
    elif ord(s[0]) == 8:
        getcase(s[1:])
    elif ord(s[0]) == 9:
        getcase(s[1:])
    elif ord(s[0]) == 10:
        getcase(s[1:])
    elif ord(s[0]) == 11:
        getcase(s[1:])
    elif ord(s[0]) == 12:
        getcase(s[1:])
    elif ord(s[0]) == 13:
        getcase(s[1:])
    elif ord(s[0]) == 14:
        getcase(s[1:])
    elif ord(s[0]) == 15:
        getcase(s[1:])
    elif ord(s[0]) == 16:
        getcase(s[1:])
    elif ord(s[0]) == 17:
        getcase(s[1:])
    elif ord(s[0]) == 18:
        getcase(s[1:])
    elif ord(s[0]) == 19:
        getcase(s[1:])
    elif ord(s[0]) == 20:
        getcase(s[1:])
    elif ord(s[0]) == 21:
        getcase(s[1:])
    elif ord(s[0]) == 22:
        getcase(s[1:])
    elif ord(s[0]) == 23:
        getcase(s[1:])
    elif ord(s[0]) == 24:
        getcase(s[1:])
    elif ord(s[0]) == 25:
        getcase(s[1:])
    elif ord(s[0]) == 26:
        getcase(s[1:])
    elif ord(s[0]) == 27:
        getcase(s[1:])
    elif ord(s[0]) == 28:
        getcase(s[1:])
    elif ord(s[0]) == 29:
        getcase(s[1:])
    elif ord(s[0]) == 30:
        getcase(s[1:])
    elif ord(s[0]) == 31:
        getcase(s[1:])
    elif ord(s[0]) == 32:
        getcase(s[1:])
    elif ord(s[0]) == 33:
        getcase(s[1:])
    elif ord(s[0]) == 34:
        getcase(s[1:])
    elif ord(s[0]) == 35:
        getcase(s[1:])
    elif ord(s[0]) == 36:
        getcase(s[1:])
    elif ord(s[0]) == 37:
        getcase(s[1:])
    elif ord(s[0]) == 38:
        getcase(s[1:])
    elif ord(s[0]) == 39:
        getcase(s[1:])
    elif ord(s[0]) == 40:
        getcase(s[1:])
    elif ord(s[0]) == 41:
        getcase(s[1:])
    elif ord(s[0]) == 42:
        getcase(s[1:])
    elif ord(s[0]) == 43:
        getcase(s[1:])
    elif ord(s[0]) == 44:
        getcase(s[1:])
    elif ord(s[0]) == 45:
        getcase(s[1:])
    elif ord(s[0]) == 46:
        getcase(s[1:])
    elif ord(s[0]) == 47:
        getcase(s[1:])
    elif ord(s[0]) == 48:
        getcase(s[1:])
    elif ord(s[0]) == 49:
        getcase(s[1:])
    elif ord(s[0]) == 50:
        getcase(s[1:])
    elif ord(s[0]) == 51:
        getcase(s[1:])
    elif ord(s[0]) == 52:
        getcase(s[1:])
    elif ord(s[0]) == 53:
        getcase(s[1:])
    elif ord(s[0]) == 54:
        getcase(s[1:])
    elif ord(s[0]) == 55:
        getcase(s[1:])
    elif ord(s[0]) == 56:
        getcase(s[1:])
    elif ord(s[0]) == 57:
        getcase(s[1:])
    elif ord(s[0]) == 58:
        getcase(s[1:])
    elif ord(s[0]) == 59:
        getcase(s[1:])
    elif ord(s[0]) == 60:
        getcase(s[1:])
    elif ord(s[0]) == 61:
        getcase(s[1:])
    elif ord(s[0]) == 62:
        getcase(s[1:])
    elif ord(s[0]) == 63:
        getcase(s[1:])
    elif ord(s[0]) == 64:
        getcase(s[1:])
    elif ord(s[0]) == 65:
        getcase(s[1:])
    elif ord(s[0]) == 66:
        getcase(s[1:])
    elif ord(s[0]) == 67:
        getcase(s[1:])
    elif ord(s[0]) == 68:
        getcase(s[1:])
    elif ord(s[0]) == 69:
        getcase(s[1:])
    elif ord(s[0]) == 70:
        getcase(s[1:])
    elif ord(s[0]) == 71:
        getcase(s[1:])
    elif ord(s[0]) == 72:
        getcase(s[1:])
    elif ord(s[0]) == 73:
        getcase(s[1:])
    elif ord(s[0]) == 74:
        getcase(s[1:])
    elif ord(s[0]) == 75:
        getcase(s[1:])
    elif ord(s[0]) == 76:
        getcase(s[1:])
    elif ord(s[0]) == 77:
        getcase(s[1:])
    elif ord(s[0]) == 78:
        getcase(s[1:])
    elif ord(s[0]) == 79:
        getcase(s[1:])
    elif ord(s[0]) == 80:
        getcase(s[1:])
    elif ord(s[0]) == 81:
        getcase(s[1:])
    elif ord(s[0]) == 82:
        getcase(s[1:])
    elif ord(s[0]) == 83:
        getcase(s[1:])
    elif ord(s[0]) == 84:
        getcase(s[1:])
    elif ord(s[0]) == 85:
        getcase(s[1:])
    elif ord(s[0]) == 86:
        getcase(s[1:])
    elif ord(s[0]) == 87:
        getcase(s[1:])
    elif ord(s[0]) == 88:
        getcase(s[1:])
    elif ord(s[0]) == 89:
        getcase(s[1:])
    elif ord(s[0]) == 90:
        getcase(s[1:])
    elif ord(s[0]) == 91:
        getcase(s[1:])
    elif ord(s[0]) == 92:
        getcase(s[1:])
    elif ord(s[0]) == 93:
        getcase(s[1:])
    elif ord(s[0]) == 94:
        getcase(s[1:])
    elif ord(s[0]) == 95:
        getcase(s[1:])
    elif ord(s[0]) == 96:
        getcase(s[1:])
    elif ord(s[0]) == 97:
        getcase(s[1:])
    elif ord(s[0]) == 98:
        getcase(s[1:])
    elif ord(s[0]) == 99:
        getcase(s[1:])
    elif ord(s[0]) == 100:
        getcase(s[1:])
    elif ord(s[0]) == 101:
        getcase(s[1:])
    elif ord(s[0]) == 102:
        getcase(s[1:])
    elif ord(s[0]) == 103:
        getcase(s[1:])
    elif ord(s[0]) == 104:
        getcase(s[1:])
    elif ord(s[0]) == 105:
        getcase(s[1:])
    elif ord(s[0]) == 106:
        getcase(s[1:])
    elif ord(s[0]) == 107:
        getcase(s[1:])
    elif ord(s[0]) == 108:
        getcase(s[1:])
    elif ord(s[0]) == 109:
        getcase(s[1:])
    elif ord(s[0]) == 110:
        getcase(s[1:])
    elif ord(s[0]) == 111:
        getcase(s[1:])
    elif ord(s[0]) == 112:
        getcase(s[1:])
    elif ord(s[0]) == 113:
        getcase(s[1:])
    elif ord(s[0]) == 114:
        getcase(s[1:])
    elif ord(s[0]) == 115:
        getcase(s[1:])
    elif ord(s[0]) == 116:
        getcase(s[1:])
    elif ord(s[0]) == 117:
        getcase(s[1:])
    elif ord(s[0]) == 118:
        getcase(s[1:])
    elif ord(s[0]) == 119:
        getcase(s[1:])
    elif ord(s[0]) == 120:
        getcase(s[1:])
    elif ord(s[0]) == 121:
        getcase(s[1:])
    elif ord(s[0]) == 122:
        getcase(s[1:])
    elif ord(s[0]) == 123:
        getcase(s[1:])
    elif ord(s[0]) == 124:
        getcase(s[1:])
    elif ord(s[0]) == 125:
        getcase(s[1:])
    elif ord(s[0]) == 126:
        getcase(s[1:])
    elif ord(s[0]) == 127:
        getcase(s[1:])
    else:
        getcase(s[1:])

def create_code():
    res = []
    for i in range(128):
        ss = 'elif ord(s[0]) == %d:\n    getcase(s[1:])\n'%(i)
        res.append(ss)
    print ''.join(res)

def decode(s, start, end):
    import re
    lines = re.findall('line ([0-9]+)', s)
    lines = map(lambda x: int(x), lines)
    lines = filter(lambda x : x>=start and x<=end , lines)
    ss = map(lambda x: chr((x-start)/2), lines)
    return ''.join(ss)

last_half_case="""
Traceback (most recent call last):
  File "check_homework.py", line 65
  File "PyLuaTblParser.py", line 280
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 178
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 170
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 176
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 216
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 222
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 252
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 222
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 252
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 244
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 214
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 216
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 148
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 148
  File "PyLuaTblParser.py", line 96
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 254
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 234
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 236
  File "PyLuaTblParser.py", line 244
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 224
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 214
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 86
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 194
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 234
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 210
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 214
  File "PyLuaTblParser.py", line 216
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 222
  File "PyLuaTblParser.py", line 224
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 234
  File "PyLuaTblParser.py", line 236
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 244
  File "PyLuaTblParser.py", line 246
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 252
  File "PyLuaTblParser.py", line 254
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 140
  File "PyLuaTblParser.py", line 162
  File "PyLuaTblParser.py", line 170
  File "PyLuaTblParser.py", line 154
  File "PyLuaTblParser.py", line 140
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 140
  File "PyLuaTblParser.py", line 142
  File "PyLuaTblParser.py", line 144
  File "PyLuaTblParser.py", line 146
  File "PyLuaTblParser.py", line 148
  File "PyLuaTblParser.py", line 150
  File "PyLuaTblParser.py", line 152
  File "PyLuaTblParser.py", line 154
  File "PyLuaTblParser.py", line 156
  File "PyLuaTblParser.py", line 158
  File "PyLuaTblParser.py", line 160
  File "PyLuaTblParser.py", line 162
  File "PyLuaTblParser.py", line 164
  File "PyLuaTblParser.py", line 166
  File "PyLuaTblParser.py", line 168
  File "PyLuaTblParser.py", line 170
  File "PyLuaTblParser.py", line 172
  File "PyLuaTblParser.py", line 174
  File "PyLuaTblParser.py", line 176
  File "PyLuaTblParser.py", line 178
  File "PyLuaTblParser.py", line 180
  File "PyLuaTblParser.py", line 182
  File "PyLuaTblParser.py", line 184
  File "PyLuaTblParser.py", line 188
  File "PyLuaTblParser.py", line 190
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 210
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 216
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 234
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 202
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 262
  File "PyLuaTblParser.py", line 76
  File "PyLuaTblParser.py", line 138
  File "PyLuaTblParser.py", line 80
  File "PyLuaTblParser.py", line 82
  File "PyLuaTblParser.py", line 84
  File "PyLuaTblParser.py", line 198
  File "PyLuaTblParser.py", line 86
  File "PyLuaTblParser.py", line 94
  File "PyLuaTblParser.py", line 90
  File "PyLuaTblParser.py", line 92
  File "PyLuaTblParser.py", line 200
  File "PyLuaTblParser.py", line 96
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 88
  File "PyLuaTblParser.py", line 126
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 258
  File "PyLuaTblParser.py", line 128
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 130
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 134
  File "PyLuaTblParser.py", line 136
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 108
  File "PyLuaTblParser.py", line 110
  File "PyLuaTblParser.py", line 112
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 118
  File "PyLuaTblParser.py", line 120
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 122
  File "PyLuaTblParser.py", line 124
  File "PyLuaTblParser.py", line 140
  File "PyLuaTblParser.py", line 142
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 144
  File "PyLuaTblParser.py", line 146
  File "PyLuaTblParser.py", line 148
  File "PyLuaTblParser.py", line 150
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 210
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 250
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 214
  File "PyLuaTblParser.py", line 114
  File "PyLuaTblParser.py", line 140
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 244
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 244
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 214
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 214
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 252
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 220
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 206
  File "PyLuaTblParser.py", line 222
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 256
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 260
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 210
  File "PyLuaTblParser.py", line 210
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 116
  File "PyLuaTblParser.py", line 106
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 176
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 158
  File "PyLuaTblParser.py", line 204
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 240
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 176
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 244
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 226
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 218
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 234
  File "PyLuaTblParser.py", line 126
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 248
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 158
  File "PyLuaTblParser.py", line 176
  File "PyLuaTblParser.py", line 168
  File "PyLuaTblParser.py", line 166
  File "PyLuaTblParser.py", line 102
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 238
  File "PyLuaTblParser.py", line 216
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 208
  File "PyLuaTblParser.py", line 232
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 228
  File "PyLuaTblParser.py", line 212
  File "PyLuaTblParser.py", line 230
  File "PyLuaTblParser.py", line 242
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 94
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 130
  File "PyLuaTblParser.py", line 76
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 98
  File "PyLuaTblParser.py", line 36
  File "PyLuaTblParser.py", line 30
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 28
  File "PyLuaTblParser.py", line 192
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 80
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 100
  File "PyLuaTblParser.py", line 134
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 94
  File "PyLuaTblParser.py", line 104
  File "PyLuaTblParser.py", line 78
  File "PyLuaTblParser.py", line 196
  File "PyLuaTblParser.py", line 74
  File "PyLuaTblParser.py", line 132
"""
if __name__ == '__main__':
    ss = decode(last_half_case, 10, 266)
    print ss