    #! /usr/bin/python
    
def R(v, x, y, c1, c2):
        c1 = max(0, c1 - v/y + v/(x*y))
        c2 = max(0, c2 - v/x + v/(x*y))
        return c1 + c2 <= v - v/x - v/y + v/(x*y)
    
    
    if __name__ == "__main__":
        c1, c2, x, y = map(int, input().split())
        l = 1
        r = (c1/(x-1) + 1) * x + (c2/(x-1) + 1) * y
        m = 0
        while l<r:
            m = (l+r)/2
            rm = R(m, x, y, c1, c2)
            rm1 = R(m-1, x, y, c1, c2)
            if not rm1 and rm:
                break
            elif not rm:
                l = m
            else:
                r = m - 1
    
        print m