def solve(x):
        if x<3:
            return "NO"
        else:
            a = 0
            while 3*a<=x:
                if (x-3*a)%7==0:
                    return "YES"
                a+=1
            return "NO"
    for _ in range(input()):
        print(solve(input()))