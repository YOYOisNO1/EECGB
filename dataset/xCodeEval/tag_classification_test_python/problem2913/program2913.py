    import re
    import sys
    
def main(args):
        n = int(input())
        s = input()
        
        ar = []
        for i in range(n):
            t = s[:i] + s[:i] + ("" if 2 * i >= n else s[2*i:])
            r = i + max(n - 2*i, 0) + (i > 0)
            ar.append((t, r))
        
        print(min(v[1] for v in ar if v[0] == s))
    
    if __name__ == '__main__':
        sys.exit(main(sys.argv))