    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    """Codeforces Round #552 (Div. 3)
    
    Problem C. Gourmet Cat
    
    :author:         Kitchen Tong
    :mail:    kctong529@gmail.com
    
    Please feel free to contact me if you have any question
    regarding the implementation below.
    """
    
    __version__ = '0.1'
    __date__ = '2019-04-16'
    
    import sys
    
    
def count_days(a, b, c):
        weeks = min(a // 3, b // 2, c // 2)
        a -= weeks * 3
        b -= weeks * 2
        c -= weeks * 2
        if a == 0:
            if b > 0:
                if c > 0:
                    return weeks * 7 + 2
                else:
                    return weeks * 7 + 1
            elif c > 0:
                return weeks * 7 + 1
        elif a == 1:
            if c > 1:
                return weeks * 7 + 3 + min(2, b)
            else:
                return weeks * 7 + 1 + min(1, b) + min(1, c)
        elif a == 2:
            if b > 0:
                if b > 1:
                    return weeks * 7 + 2 + min(2, c)
                else:
                    if c > 0:
                        return weeks * 7 + 4
            else:
                return weeks * 7 + 2
        else:
            if c == 0:
                return weeks * 7 + 2 + min(2, b)
            else:
                if c > 1:
                    return weeks * 7 + 3
                else:
                    return weeks * 7 + 2
        return weeks * 7
    
def main(argv=None):
        a, b, c = map(int, input().split())
        print(count_days(a, b, c))
        return 0
    
    if __name__ == "__main__":
        STATUS = main()
        sys.exit(STATUS)
    