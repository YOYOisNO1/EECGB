    from sys import stdin, gettrace
    
    if not gettrace():
    def input():
            return next(stdin)[:-1]
    
    
def modInt(mod):
        class ModInt:
    
        def __init__(self, value):
                self.value = value % mod
    
        def __int__(self):
                return self.value
    
        def __eq__(self, other):
                return self.value == other.value
    
        def __hash__(self):
                return hash(self.value)
    
        def __add__(self, other):
                return ModInt(self.value + int(other))
    
        def __sub__(self, other):
                return ModInt(self.value - int(other))
    
        def __mul__(self, other):
                return ModInt(self.value * int(other))
    
        def __floordiv__(self, other):
                return ModInt(self.value // int(other))
    
        def __truediv__(self, other):
                return ModInt(self.value * pow(int(other), mod - 2, mod))
    
        return ModInt
    
    
# def input():
    #    return stdin.buffer.readline()
    
    MOD = 998244353
    
def main():
        n,m,l,r = map(int, input().split())
        range = r - l + 1
        if n*m%2 == 0:
            ModInt = modInt(MOD)
            res1 = ModInt(pow(range, n * m, MOD))
            if range % 2 == 0:
                res = int(res1/2)
            else:
                res = int((res1+1)/2)
        else:
            res = pow(range, n*m, MOD)
        print(res)
    
    
    if __name__ == "__main__":
        main()