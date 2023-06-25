def program2770():
    t=int(input())
    for _ in range(t):
        s=int(input())
        ans=[1,2,3,4,5,6,7,8,9]
        anss=''
        for i in range(9):
            if ans[-1]<=s:
                anss+=str(ans[-1])
                s-=ans[-1]
            ans.pop()
        print(anss[::-1])