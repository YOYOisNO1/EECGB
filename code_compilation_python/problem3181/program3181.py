    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    import string
    import sys
    
    
def main():
        iterator = iter(sys.stdin.read().split())
        n, m = int(next(iterator)), int(next(iterator))
        s = next(iterator)
        p = {}
        buffer = set()
        for i in string.ascii_uppercase:
            p[i] = s.rfind(i)
        for i, x in enumerate(s):
            if i < p[x]:
                buffer.add(x)
                if len(buffer) > m:
                    print('YES')
                    return
            else:
                buffer.remove(x)
        print('NO')
    
    if __name__ == '__main__':
        main()