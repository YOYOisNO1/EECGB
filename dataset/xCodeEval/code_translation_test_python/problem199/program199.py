    import sys, math
    
def readln():
        return sys.stdin.readline()
    
def parse(s, fun=int, sep=" "):
        return map(fun, s.split(sep))
    
def write(obj):
        sys.stdout.write(str(obj))
    
def writeln(obj):
        sys.stdout.write(str(obj) + "\n")
    
    
    n, x, y = parse(readln())
    writeln(max(0, int(math.ceil(y * n / 100.0 - x))))