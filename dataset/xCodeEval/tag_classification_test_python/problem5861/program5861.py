    import math
    
def add_base(a, b, base):
        # print(base)
        a = int(a, base = base)
        b = int(b, base = base)
        # print("a",a)
        # print("b",b)
        res = a + b
        # print("res",res)
        nu = ''
        while res:
            nu = str(res % base) + nu
            res = math.floor(res / base)
        # print("nu", nu)
        return len(nu)
    
def main():
        a, b = input().split()
        st = str(a) + str(b)
        max_ord = 0
        for i in st:
            if max_ord < (ord(i) - 48):
                max_ord = (ord(i) - 48)
        base = max_ord + 1
        ans = add_base(a, b, base)
        print(ans)
    
    if __name__ == '__main__':
        main()