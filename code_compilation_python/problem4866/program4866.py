    import fileinput
    
    
def calc(a, b):
        ans = 0
        l = a + b
        i = 1
        while i < l:
            P = l // i
            r = l // P
            if P <= a and P <= b:
                an = (a + P) // (P + 1)
                ax = a // P
                bn = (b + P) // (P + 1)
                bx = b // P
                if an <= ax and bn <= bx:
                    ans += min(ax + bx, r) - max(an + bn, i) + 1
            i = r + 1
        return ans
    
    
    if __name__ == '__main__':
        it = fileinput.input()
        a, b = [int(x) for x in next(it).split()]
        print(calc(a, b))