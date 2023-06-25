    s = ["xx.", "x.x", ".xx"]
def chk(m):
        for i in m:
            if i[:3] in s or i[1:] in s:
                return True
        for i in zip(*m):
            if "".join(i[:3]) in s or "".join(i[1:]) in s:
                return True
        if m[1][0]+m[2][1]+m[3][2] in s or \
           m[0][0]+m[1][1]+m[2][2] in s or \
           m[1][1]+m[2][2]+m[3][3] in s or \
           m[0][1]+m[1][2]+m[2][3] in s or \
           m[0][2]+m[1][1]+m[2][0] in s or \
           m[0][3]+m[1][2]+m[2][1] in s or \
           m[1][2]+m[2][1]+m[3][0] in s or \
           m[1][3]+m[2][2]+m[3][1] in s:
            return True
        return False
    m = [input() for i in range(4)]
    print("YES") if chk(m) else "NO"