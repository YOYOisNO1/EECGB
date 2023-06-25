    import math
    
def theatresquare(n,m,a):
        return ((n-1)//a + 1)*((m-1)//a + 1)
    
    # n,m,a = list(map(int,input().split()))
    # print(theatresquare(n,m,a))
    
def convert(x):
        s = ""
        while x > 0:
            a = x%26
            x = x//26
            if a == 0:
                a = 26
                x -= 1
            s = chr(a-1+ord('A')) + s
        return s
    
def convertindex(x):
        i = 0
        while (x[i] <= 'Z') and (x[i] >= 'A'):
            i += 1
        j = i
        while (j < len(x)) and (x[j] <= '9') and (x[j] >= '0'):
            j += 1
        if j == len(x):
            s = 0
            for j in range(i):
                s = (ord(x[j]) - ord('A')+1) + 26*s
            return 'R' + x[i:] + 'C' + str(s)
        else:
            while (x[i] <= '9') and (x[i] >= '0'):
                i += 1
            return convert(int(x[i+1:])) + x[1:i]
    
    # cases = int(input())
    # for _ in range(cases):
    #     l = input()
    #     print(convertindex(l))
    
def berlandcircus(A,B,C):
        a = (B[0] - C[0])**2 + (B[1] - C[1])**2
        b = (A[0] - C[0])**2 + (A[1] - C[1])**2
        c = (B[0] - A[0])**2 + (B[1] - A[1])**2
    
        la = math.acos(abs((b+c-a)/(2*math.sqrt(b)*math.sqrt(c))))/math.pi
        lb = math.acos(abs((c-b+a)/(2*math.sqrt(a)*math.sqrt(c))))/math.pi
        lc = math.acos(abs((b-c+a)/(2*math.sqrt(a)*math.sqrt(b))))/math.pi
    
        i = 3
        while i < 101:
            if abs(la*i-round(la*i)) < 0.00001:
                if abs(lb*i-round(lb*i)) < 0.00001:
                    if abs(lb*i-round(lb*i)) < 0.00001:
                        return round(i*0.125*a*math.sin(2*math.pi/i)/math.sin(la*math.pi)**2,6)
            i += 1
        
    
    
    A = list(map(float,input().split()))
    B = list(map(float,input().split()))
    C = list(map(float,input().split()))
    
    print(berlandcircus(A,B,C))