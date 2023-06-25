def program1117():
    n = int(input())
    R,S,P = map(int, input().split())
    r,s,p = map(int, input().split())
    
    maxx = min(R,s) + min(S,p) + min(P,r)
    minn = 0
    
    minn += max(0, R - (p+r))
    minn += max(0, S - (s+r))
    minn += max(0, P - (p+s))
    print(minn, maxx)