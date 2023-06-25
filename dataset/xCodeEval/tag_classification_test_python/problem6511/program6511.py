    
    # -*- coding:utf-8 -*-
    # #NYAN NYAN
    #░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    #░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
    #░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
    #░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
    #░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
    #░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
    #░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
    #░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
    #░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
    #░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
    #░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
    #░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
    #░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
    #░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    from __future__ import print_function
    import os
    import sys
    Debug = True
    Conda = False
    UseFileIO = True
    UseLibrary = False
    Archive = False
    EdX = False
    BOJ = False
    ReadTarget = None
    WriteTarget = None
    
def AddImports(libraryNames):
        for libname in libraryNames:
            if (type(libname) == type(tuple())):
                short = libname[1]
                libname = libname[0]
            else:
                short = None
            try:
                lib = __import__(libname)
            except ImportError:
                pass
            else:
                if short:
                    globals()[short] = lib
                else:
                    globals()[libname] = lib
        return True
    libnames = ['fileinput', 'codecs', 'operator', 'functools', 'math', 'io', 'platform', 'collections', 'mmap', 'logging', 'logging.handlers']
    AddImports(libnames)
    IntellisenseHint = False
    if IntellisenseHint:
        import fileinput
        import codecs
        import operator
        import functools
        import math
        import io
        import platform
        import collections
        import mmap
        import logging
        import logging.handlers
        import defs
    
def readSequence(elementType=None, inputLine=None, seperator=None, strip=True):
        global readTarget
        if (inputLine == None):
            inputLine = readTarget.readline()
        if strip:
            inputLine = inputLine.strip()
        if isinstance(inputLine, bytes):
            inputLine = inputLine.decode('utf-8')
        if (elementType == None):
            return [x for x in inputLine.split(seperator)]
        return [elementType(x) for x in inputLine.split(seperator)]
    rl = RobertsSpaceIndustries = readSequence
    
def ToSpaceSeperatedString(targetList):
        return ' '.join(map(str, targetList))
    
def convert_to_bytes(arg):
        if isinstance(arg, bytes):
            return arg
        elif isinstance(arg, str):
            return arg.encode('utf-8')
        elif hasattr(arg, '__iter__'):
            return ' '.join(map(convert_to_bytes, arg))
        else:
            return str(arg).encode('utf-8')
    
    class edx_in:
    
    def __init__(self, target=None):
            self.target = target
    
    def create_lineTokenizer(self):
            if self.mm:
                for line in iter(self.mm.readline, ''):
                    (yield line)
            else:
                for line in iter(self.stream.readline, ''):
                    (yield line)
    
    def __enter__(self):
            if (self.target and UseFileIO):
                self.isFileEmpty = (os.stat(self.target).st_size == 0)
                if self.isFileEmpty:
                    return self
                self.stream = open(self.target, 'rb', 1)
                self.mm = mmap.mmap(self.stream.fileno(), 0, access=mmap.ACCESS_READ)
            else:
                self.mm = None
                self.isFileEmpty = True
                self.stream = sys.stdin
            self.lines = self.create_lineTokenizer()
            self.lineTokens = None
            return self
    
    def __exit__(self, type, value, traceback):
            if (not self.isFileEmpty):
                if self.mm:
                    self.mm.close()
                self.stream.close()
    
    def next_line(self):
            ret = None
            try:
                ret = ' '.join(self.lineTokens)
                self.lineTokens.close()
                if (ret == ''):
                    raise ValueError()
                return ret
            except:
                pass
            if hasattr(self.lines, 'next'):
                ret = self.lines.next()
            if hasattr(self.lines, '__next__'):
                ret = self.lines.__next__()
            return ret
    
    def next_int(self):
            return int(self.next_token())
    
    def next_float(self):
            return float(self.next_token())
    
    def next_str(self, encoding=None):
            if encoding:
                return self.next_token().decode(encoding)
            else:
                return self.next_token()
    
    def getLineTokens(self, line):
            for token in iter(line.split()):
                (yield token)
    
    def nextNToken(self, rep=0):
            ans = []
            while (rep > 0):
                ans.append(self.next_token())
                rep -= 1
            return ans
    
    def next_token(self):
            try:
                if hasattr(self.lineTokens, 'next'):
                    ret = self.lineTokens.next()
                if hasattr(self.lineTokens, '__next__'):
                    ret = self.lineTokens.__next__()
                return ret
            except:
                self.lineTokens = self.getLineTokens(self.next_line())
                return self.next_token()
    
    class edx_out:
    
    def __init__(self, target=None):
            self.target = target
    
    def __enter__(self):
            self.is_cpython = (platform.python_implementation() == 'CPython')
            if (self.target and UseFileIO):
                if self.is_cpython:
                    self.stream = open(self.target, 'wb', 1)
                else:
                    self.stream = io.BytesIO()
            else:
                self.stream = sys.stdout
            return self
    
    def __exit__(self, type, value, traceback):
            if (self.target and UseFileIO):
                if self.is_cpython:
                    self.stream.close()
                else:
                    outf = open(self.target, 'wb', 1)
                    outf.write(self.stream.getvalue())
                    outf.close()
                    self.stream.close()
            else:
                pass
    
    def write(self, arg):
            self.stream.write(convert_to_bytes(arg))
    
    def writeln(self, arg):
            self.write(arg)
            self.write('\n')
    
    def test(this, expression):
            frame = sys._getframe(1)
            exp = expression
            ans = repr(eval(exp, frame.f_globals, frame.f_locals))
            this.debug(((('test : ' + exp) + ' = ') + ans))
            pass
    
def solve():
        solve900b()
    
def LongDivisionDigits(dividend, number):
        d = dividend
        while True:
            (yield (d // number))
            d = ((d % number) * 10)
    
def solve900b():
        (a, b, c) = (ri(), ri(), ri())
        i = 1
        a *= 10
        maxRange = (b + 6)
        t = LongDivisionDigits(a, b)
        while (i < maxRange):
            try:
                if (t.next() == c):
                    put(i)
                    return
                else:
                    i += 1
            except:
                break
        put((-1))
    
def solve900c():
        n = ri()
        arr = rl().split()
        starts = {}
        lens = ([0] * n)
        debug(arr)
        lens[0] = 1
        ans = 1000000
        for i in range(n):
            if (i > 0):
                if (arr[(i - 1)] >= arr[i]):
                    lens[i] = 1
                else:
                    lens[i] = (lens[(i - 1)] + 1)
            pass
        for i in range(n):
            if ((lens[i] == 1) or (lens[(i + 1)] == 1)):
                if (i >= 1):
                    if ((arr[(i - 1)] < arr[(i + 1)]) and (lens[(i - 1)] + lens[(i + 1)])):
                        pass
        debug(lens)
        solve1260()
    
def solve1260():
        (n, m, v) = (ri(), ri(), ri())
        stack1 = []
        g = {}
        for i in range(m):
            g[ri()] = ri()
        debug('end')
    
def dfs(g, vertex):
        g[vertex]
        if (vertex in g):
            k = g[vertex]
        dfs(g, v)
        pass
    reader = None
    writer = None
    try:
        logger1 = logging.getLogger('log1')
        debug = (lambda *x: logger1.log(logging.DEBUG, convert_to_bytes(x)))
        PutLevel = 100
        logging.PUT = PutLevel
        logging.addLevelName(PutLevel, 'PUT')
        logger1.setLevel(logging.PUT)
        formatter = logging.Formatter()
    except:
        pass
    with edx_in(ReadTarget) as Reader:
        with edx_out(WriteTarget) as Writer:
            try:
                outHandler = logging.StreamHandler(Writer.stream)
                outHandler.setFormatter(formatter)
                logger1.addHandler(outHandler)
                put = (lambda *args: logger1.log(logging.PUT, convert_to_bytes(args)))
                info = (lambda *args: logger1.log(logging.INFO, convert_to_bytes(args)))
                critical = (lambda *args: logger1.log(logging.CRITICAL, convert_to_bytes(args)))
            except:
                debug = Writer.writeln
                put = Writer.writeln
                info = Writer.writeln
                critical = Writer.writeln
    
        def nop(*arg):
                pass
            debug = nop
            test = nop
            info = nop
            reader = Reader
            writer = Writer
            ri = reader.next_int
            rs = reader.next_str
            rt = reader.next_token
            rf = reader.next_float
            rl = reader.next_line
            wl = writer.writeln
            solve()