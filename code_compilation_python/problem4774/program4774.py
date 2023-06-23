    import re
    import sys
    
    sys.setrecursionlimit(5000)
    
    MOD = 2 ** 15
    MOD2 = 2 * MOD
    
    class X:
    def __init__(self, x):
            if isinstance(x, X):
                self.x = x.x
            else:
                self.x = x
    def __add__(self, other):
            return X(((self.x + other.x) % MOD + MOD) % MOD)
    def __sub__(self, other):
            return X(((self.x - other.x) % MOD + MOD) % MOD)
    def __mul__(self, other):
            return X(((self.x * other.x) % MOD + MOD) % MOD)
    def __div__(self, other):
            return X(((sefl.x // other.x) % MOD + MOD) % MOD)
    def __eq__(self, other):
            return self.x == other.x
    def __lt__(self, other):
            return self.x < other.x
    def __gt__(self, other):
            return self.x > other.x
            
    #fin, fout = open("input.txt", 'r'), open("output.txt", 'w')
    fin, fout = sys.stdin, sys.stdout
    
    
    fn = int(fin.readline())
    text = "".join(fin.readlines())
    text = text.replace("\n", "")
    
    text = text[text.find("{") + 1: text.find("}")]
    text = re.sub(r"(\d+)", r"X(\1)", text)
    text = re.sub(r"(if.*?)return", r"\1 : return", text)
    text = re.sub(r"\s*([\(\)])\s*", r"\1", text)
    text = "".join(text)
    text = "".join("     " + x.strip() + "\n" for x in text.split(";"))
text = "def ff(n):\n" + text
    
    exec(compile(text.strip(), "f**k", 'exec'))
    
    cache = {}
def f(n):
        try:
            return cache[n.x]
        except KeyError:
            r = cache[n.x] = X(ff(n))
            return r
        
    ans = -1
    for i in range(0, MOD):
        t = cache[i] = X(ff(X(i))
        if t.x == fn:
          ans = i
          
    print(ans)
        
    
    
        
       