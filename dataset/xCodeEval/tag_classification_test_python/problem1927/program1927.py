    letters=[0]*26
def index(x):
        x=ord(x)
        if x>=ord('a') and x<=ord('z'):
            return x-ord('a')
        elif x>=ord('A') and x<=ord('Z'):
            return x-ord('A')
    n=int(input())
    s=input().strip()
    for x in s:
        x=index(x)
        letters[x]=1
    if 0 in letters:
        print('NO')
    else:
        print('YES')