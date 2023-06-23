    import re
    import sys
    
    MOD = 2 ** 15
    MOD2 = 2 * MOD
    
    class X:
    def __init__(self, x):
            if isinstance(x, X):
                self.x = x.x
            else:
                self.x = x
    def __add__(self, other):
            return X((self.x + other.x + MOD2) % MOD)
    def __sub__(self, other):
            return X((self.x - other.x + MOD2) % MOD)
    def __mul__(self, other):
            return X((self.x * other.x) % MOD)
    def __div__(self, other):
            return X((sefl.x // other.x) % MOD)
    def __eq__(self, other):
            return self.x == other.x
    def __lt__(self, other):
            return self.x < other.x
    def __gt__(self, other):
            return self.x > other.x
            
    
    #fin = open("input.txt", 'r')
    #fout = open("output.txt", 'w')
    fin = sys.stdin
    fout = sys.stdout
    
    fn = int(fin.readline())
    text = "".join(fin.readlines())
    
    text.replace(";", "\n")
    text = text[text.find("{") + 1: text.find("}")]
    text = re.sub(r"(\d+)", r"X(\1)", text)
    text = ["     " + x.strip() for x in text.split("\n")]
    text = "\n".join(text)
    text = re.sub(r"(if.*?)(return.*)", r"\1: \2", text)
text = "def ff(n):\n" + text
    
    exec(compile(text.strip(), "f**k", 'exec')
    
    cache = {}
def f(n):
        return cache[n.x]
        
    ans = -1
    for i in range(0, MOD + 1):
        t = cache[i] = X(ff(X(i)))
        if t.x == fn:
          ans = i
          
    print(ans)
        
    
    
        
       