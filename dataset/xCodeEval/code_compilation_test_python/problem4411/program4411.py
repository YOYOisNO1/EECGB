    #!/usr/bin/env python
    
def Deg(A, B):
        C = B
        Q = 1
        while A > 0 :
            if A % 2 == 1:
                Q = (Q * C) % 1000000007
            C = (C * C) % 1000000007
            A = A / 2
        return Q
    
    if __name__ == "__main__":
        n, m, k = map(int, input().split())
        if k > n:
            print Deg(n, m)
        elif k == n :
            print Deg(k / 2 + k % 2, m)
        else :
            print Deg(k % 2 + 1, m)