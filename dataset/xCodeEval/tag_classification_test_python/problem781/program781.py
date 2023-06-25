def program781():
    v = {
    	"1" : 2,
        "2" : 5,
            "3" : 5,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 3,
            "8" : 7,
            "9" : 6,
            "0" : 6
        }
    a,b = map(int,input().split())
    s = str(list(range(a,b+1)))
    ans = 0
    for i in range(10):
    	ans+=v[str(i)]*s.count(str(i))
    print(ans)