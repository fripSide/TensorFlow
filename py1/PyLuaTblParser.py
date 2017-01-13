# coding: utf-8
__author__ = 'fripSide'

DEBUG = True

"""
用python %r 对str进行转义
"""

class PyLuaTblParser(object):
    TOKEN = "{},;="
    SPACE = "\r\n\t "

    def __init__(self):
        self.table = {}
        self.tokens = []
        self.pos = 0 # current token pos
        self.len = 0

    def load(self, s):
        self.pos = 0
        self.tokens = Tokenizer(s).get_tokens()
        # sys.out = sys.stderr
        if DEBUG:
            print("Tokens: [<%s>]" % "> <".join(self.tokens))
        self.len = len(self.tokens)
        self.table = self._parse_str()

    def dump(self):
        return self._dump_item(self.table)

    def _dump_item(self, d):
        ret = []
        if isinstance(d, dict):
            for k, v in d.items():
                """
                统一给key加上[], [number], ["string"]
                val，若为string,则统一用引号 "string"
                """
                if isinstance(k, str):
                    k = self._dump_str(k)
                    k = '"{}"'.format(k)
                ret.append("[{}] = {}".format(k, self._dump_item(v)))
                # if isinstance(k, str):
                #     ret.append("{}={}".format(k, self._dump_item(v)))
                # else:
                #     ret.append(self._dump_item(v))
            return "{%s}" % (",\n".join(ret))
        elif isinstance(d, list):
            for v in d:
                ret.append(self._dump_item(v))
            return "{%s}" % (", ".join(ret))
        else:
            if isinstance(d, str):
                return '"{}"'.format(self._dump_str(d))
            elif d is None:
                return "nil"
            elif isinstance(d, bool):
                return "true" if d else "false"
            return str(d)

    def _dump_str(self, ss):
        ret = ""
        for c in ss:
            ret += self._dump_char(c)
        return ret

    def _dump_char(self, c):
        escape = {'\a': 'a', '\b': 'b', '\f': 'f', '\n': 'n',
                         '\r': 'r', '\t': 't', '\v': 'v'}
        if escape.has_key(c):
            return '\\' + escape[c]
        elif c in '\\\'\"':
            # print("add\\", c)
            return '\\' + c
        return c


    def loadLuaTable(self, f):
        with open(f, "r") as fp:
            self.load(fp.read())

    def dumpLuaTable(self, f):
        with open(f, "w") as fp:
            fp.write(self.dump())

    def loadDict(self, d):
        self.table = self._copy_item(d)

    def dumpDict(self):
        return self.table

    def update(self, d):
        for k, v in d:
            if k in self.table:
                if isinstance(v, list):
                    self.table[k] = self._copy_item(v)
                elif isinstance(v, dict):
                    self.table[k] = self._copy_item(v)
                else:
                    self.table[k] = v

    def __setitem__(self, key, value):
        """
        直接通过[]来读取value
        :param item:
        :return:
        """
        self.table[key] = value

    def __getitem__(self, item):
        if item not in self.table:
            raise IndexError
        return self.table[item]

    def _parse_str(self):
        tbl = self._parse_dict()
        token = self._next_token()
        if token:
            raise LuaSyntaxError("Invalid lua table! Except to get the end of Str. But get '{}' .".format(token))
        return tbl

    def _parse_dict(self):
        # 默认当做 [list], 直到有=，才当做{dict}，没有key的用数字编号
        # match {
        self._assert_value(self._get_token(), "{")
        c = self._next_token()
        key_id = 1
        has_key = False
        tbl = {}
        while c != "}" and self.pos < self.len:
            key, val = self._parse_one_pair()
            if isinstance(key, str):
                if key.startswith("\""):
                    key = key[1:]
                if key.endswith("\""):
                    key = key[:-1]
            if isinstance(val, str):
                if val.startswith("\""):
                    val = val[1:]
                if val.endswith("\""):
                    val = val[:-1]
            if key and val is not None:
                has_key = True

                if key not in tbl.keys(): # key比默认递增优先级低
                    tbl[key] = val
            if not key:
                tbl[key_id] = val
                key_id += 1
            c = self._next_token()
        # match }
        self._assert_value(self._get_token(), "}")
        # print(tbl)
        if not has_key:
            ret = tbl.values()
        else:
            ret = {}
            for k in tbl:
                if tbl[k] is not None:
                    ret[k] = tbl[k]
        return ret

    def _parse_one_pair(self):
        # 两种情况，有 = 或者没有 =
        token = self._next_token()
        key = None
        if token == "{":
            # print("parser dict")
            val = self._parse_dict()
            token = self._next_token()
            if token in ",;":
                self._get_token()
            elif token != "}":
                self._except_val(token, ", ; or }")
        # elif token == "}":
        #     return None, None
        else:
            val = self._get_token()
            token = self._next_token()
            if token == "=":
                key = self._parse_key(val)
                self._get_token() # escape =
                nk, val = self._parse_one_pair()
            else:
                val = self._parse_val(val)
                if token in ",;":
                    self._get_token()
                elif token != "}":
                    self._except_val(token, ", ; or }")

        return key, val

    def _to_num(self, ss):
        try:
            ret = int(ss)
        except:
            ret = float(ss)
        return ret

    def _parse_key(self, key):
        """
        # 验证key的格式，并且去掉key左右的括号，key只能为number和string("variable")
        # string | [number] | ["string"]，三种形式
        # key 不能是 "string"，如果没有[]就不能有引号
        @ return number or "string"
        """
        if '[' not in key:
            if key[0].isalpha():
                return '{}'.format(key)
            else:
                self._except_val(key, "variable")
        key = key.strip("[] ")
        if key.startswith("'") or key.startswith("\""):
            key = '"{}"'.format(key.strip("'\""))
        if not key.startswith("\""): # must be number
            try:
                key = self._to_num(key)
            except:
                self._except_val(key, "number")
        return key

    def _parse_val(self, val):
        # 值不能出现[], string必须有引号，否则为variable（nil）
        if not (val.startswith("'") or val.startswith("\"")):
            try:
                val = self._to_num(val)
            except:
                if val == "true":
                        val = True
                elif val == "false":
                        val = False
                elif val == "nil":
                        val = None
                else:
                    if val[0].isalpha():
                        return None
                    self._except_val(val, "valid value: number, bool, nil or string")
        return val

    def _assert_value(self, val, need):
        if val != need:
            self._except_val(val, need)

    def _except_val(self, val, need):
        context = "".join(self.tokens[self.pos - 1: self.pos + 2])
        msg = "In {}\n Except to get token '{}' , but get token '{}' .".format(context, need, val)
        # print(msg)
        raise LuaSyntaxError(msg)

    def _get_token(self):
        val = self._next_token()
        self.pos += 1
        return val

    def _next_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ""

    def _copy_item(self, other):
        d = {}
        if isinstance(other, dict):
            for k, v in other.items():
                d[k] = self._copy_item(v)
        elif isinstance(other, list):
            d = []
            for v in other:
                d.append(self._copy_item(v))
        else:
            d = other
        return d

class Tokenizer(object):
    SPACE = "\n\r\t "
    KEYWORDS = "{},;="
    ESCAPE = {'a': '\a', 'b': '\b', 'f': '\f', 'n': '\n', 'r': '\r', 't': '\t', 'v': '\v'}

    def __init__(self, s):
        s = s.replace("\\t", "\t").replace("\\n", "\n").replace("\\r", "\r")
        self.buf = s
        self.pos = 0
        self.len = len(self.buf)
        self.tokens = []

    def get_tokens(self):
        self.pos = 0
        while self.pos < self.len:
            token = self._next_token()
            if token:
                self.tokens.append(token)
        return self.tokens

    @property
    def cur(self):
        # 做转义
        if self.pos < self.len:
            return self.buf[self.pos]
        return None

    def _next_token(self):
        """
        DFA状态机
        comment --[[ ]], --[===[ ]===], --
        :return:
        """
        while self.pos < self.len:
            self._move_pos()
            if self.cur and self.cur in "\'\"":
                return self._get_string()
            elif self.cur == "[":
                return self._get_bracket()
            else:
                return self._get_variable()

        return None

    def _get_variable(self):
        # variable or number
        token = ""
        while self.pos < self.len:
            if self.buf[self.pos: self.pos + 2] == "--":
                self._skip_comment()
                if token:
                    return token
            elif self.cur in self.KEYWORDS:
                if not token:
                    token = self.cur
                    self.pos += 1
                return token
            elif self.cur in self.SPACE:
                self.pos += 1
                return token
            else:
                token += self.cur
                self.pos += 1
        return token

    def _move_pos(self):
        while self.pos < self.len:
            if self.buf[self.pos: self.pos + 2] == "--":
                self._skip_comment()
            elif self.cur in self.SPACE:
                self._skip_space()
            else:
                return

    def _skip_space(self):
        # print("_skip_space", self.pos, self.cur)
        while self.pos < self.len and self.cur in self.SPACE:
            # print("_skip_space")
            self.pos += 1

    def _skip_comment(self):
        # lua 5.2不支持嵌套注释，并且注释不能加到token中间。因此只需开始的时候过滤掉注释。
        # -- 或者 --[[ ]] , --[==[ ]==]等号数目要相同
        # 若为--则为line comment，若为 --[[ 或者--[===[ 则为long comment
        # long comment --[[ 与第一个结束]]匹配
        # print("_skip_comment")

        line_comment = self.buf[self.pos:self.pos + 2]
        long_comment = self.buf[self.pos:self.pos + 3]
        # print("_skip_comment", line_comment, long_comment)
        if line_comment == "--" and long_comment != "--[":
            # skip line comment
            while self.cur != '\n':
                self.pos += 1
                if self.pos >= self.len:
                    return
        elif long_comment == "--[":
            self.pos += 3
            end = "]"
            if self.cur == "=":
                while self.pos < self.len and self.cur == "=":
                    end += self.cur
                    self.pos += 1

                if self.cur != "[":
                    # line comment
                    while self.pos < self.len and self.cur != '\n':
                        self.pos += 1
                    return
            end += "]"
            while self.pos < self.len:
                if self.cur == "]":
                    cc = self.buf[self.pos: self.pos + len(end)]
                    if cc == end:
                        self.pos += len(end)
                        return
                    else: # ]] skip
                        self.pos += 1
                else:
                    self.pos += 1


    def _get_bracket(self):
        # 获取中括号的内容，如果格式错误，在这里不作处理
        # 可能为[number], ["string"], (不去掉括号) [==[ string ]==] (去掉括号)
        token = ""
        in_bracket = False
        while self.pos < self.len:
            if self.buf[self.pos:self.pos + 2] == "--":
                self._skip_comment()
            if self.buf[self.pos:self.pos + 2] == "[=" or self.buf[self.pos: self.pos + 2] == "[[":
                val = self._get_bracket_string()
                token += '"{}"'.format(val)
                if not in_bracket:
                    return '"{}"'.format(val)
                # print(token, self.pos, self.cur)
            if in_bracket:
                if self.cur in "\'\"":
                    if token != "[":
                        return token
                    # print("BEFFFFFFFFF", token, self.pos, self.cur)
                    token += self._get_string()
                    # print("Gettttttttttttt", token, self.pos, self.cur)
                if self.cur == "]":
                    self.pos += 1
                    token += "]"
                    # print("rettttttttttttttt", token, self.pos, self.cur)
                    return token
                else:
                    if self.cur not in self.SPACE:
                        # if token != "[":
                        #     return token
                    # else:
                        token += self.cur
                self.pos += 1
            else:
                if self.cur == "[":
                    in_bracket = True
                    if token:
                        return token
                    token = "["
                self.pos += 1
        return token

    def _get_bracket_string(self):
        # [==[ string ]==] (去掉括号)
        # print("_get_bracket_string")
        end = "]"
        self.pos += 1
        token = ""
        while self.pos < self.len and self.cur == "=":
            end += "="
            self.pos += 1
        if self.cur != "[":
            raise LuaSyntaxError("Except to get [ here, but get %s" % self.cur)
        end += "]"
        # print("EEEEEEEEEEEEEEE", end, self.cur)
        self.pos += 1
        while self.pos < self.len:
            if self.cur == "]":
                if self.buf[self.pos:self.pos + len(end)] == end:
                    self.pos += len(end)
                    # print(token, self.cur)
                    return token
            else:
                token += self.cur
            self.pos += 1
        return token

    def _get_string(self):
        # 只处理 "string", 一定为引号开头
        token = ""
        in_quotation = False
        quotation = None
        while self.pos < self.len:
            # print(self.cur, self.pos, token)
            if in_quotation:
                if self.cur == "\\":
                    token += self._get_escape()
                    # print("BKKKKKKKKK", token, self.cur, self.pos)
                elif self.cur in "\"\'":
                    in_quotation = self.cur != quotation
                    token += self.cur
                    self.pos += 1
                    if not in_quotation:
                        return token
                else:
                    # print("AAAAA\\", token, self.cur, self.pos)
                    token += self.cur
                    self.pos += 1
            else:
                if self.cur in "\'\"":
                    in_quotation = True
                    quotation = self.cur
                    # 添加引号
                    token += self.cur
                self.pos += 1
        return token

    def _get_escape(self):
        # 文件里面读进一个\相当于"\\"字符
        # 字符串中需要获取转义字符串, 按照ASCII规则 (0 ~ 256)
        # 目前就处理“\\”和引号，其他的暂时不处理
        # escape = self.buf[self.pos: self.pos + 2]
        self.pos += 1
        escape = "\\"
        # print("_get_escape", self.pos, self.cur)
        if self.cur == "\\": # 文件里面的\\，"\\"字符
            escape = "\\"
        elif self.cur in "\'\"": # 文件中的\" ("\\" 和"\"")转出"\""
            # print("before", self.cur, self.pos, len(self.cur))
            # escape = "\\" + self.cur
            escape = self.cur
        elif self.cur and self.cur.isalpha():
            if self.cur in self.ESCAPE:
                escape = self.ESCAPE[self.cur]
            else:
                escape += self.cur
        elif self.cur and self.cur.isdigit():
            n, v = 0, ""
            while self.cur and self.cur.isdigit() and n < 3:
                v += self.cur
                n += 1
                self.pos += 1
            v = int(v)
            if v > 255:
                raise LuaSyntaxError("Invalid ASCII code {} in {}.".format(v, escape))
            self.pos -= 1
            escape = chr(v)
        self.pos += 1
        # print("after", self.cur, self.pos, len(self.cur))
        return escape


class LuaSyntaxError(BaseException):
    pass

