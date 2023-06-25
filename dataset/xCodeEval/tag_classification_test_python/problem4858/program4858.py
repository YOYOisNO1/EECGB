    import math
def solve(a,b):
        a=int(a)
        b=int(b)
        if(a==b):
            print("infinity")
            return
        if(a<b):
            print(0)
            return
        a=int(a-b);
        k=1+int(math.sqrt(a))
        k=int(k);
        ans = 0
        #print(a;)
        for i in range(1,k):
            if (a%i==0):
                if i>b:
                    ans += 1
                if (a/i>b):
                    ans += 1
                if(i*i==a and (i>b or a/i>b)):
                    ans -= 1
        print(ans)
    arr = input();
    s = str.split(arr,' ')
    a = int(s[0])
    b = int(s[1])
    solve(a,b)