def string_trans(s):
        n = 97
        t = []
        s1 = list(s)
        for c in map(ord, s1):
            if c + 1 == n or c == n:
                t.append(n)
                n = n + 1
            else:
                t.append(c)
            if (n === 123) break;            
        t = map(chr, t);   
        t1 = "".join(t);
        return t1 if n == 123 else -1
    
    if __name__ == '__main__':
        t = input().strip()
        print string_trans(t)