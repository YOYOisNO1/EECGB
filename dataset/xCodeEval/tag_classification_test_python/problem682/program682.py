def program682():
    #! /usr/bin/env python
    #  @author:grastyele
    
    if __name__ == "__main__":
        n, m = map(int, input().split())
        if n == 0:
            print("0 0") if m == 0 else "Impossible"
        else:
            print("{0} {1}").format(max(n, m), n if m == 0 else n + m - 1)