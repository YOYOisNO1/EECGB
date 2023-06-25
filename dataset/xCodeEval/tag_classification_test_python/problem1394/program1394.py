def program1394():
    n = int(input())
         
    m = 1000000007
         
    ans = (pow(3, n*3) - pow(7, n)) % m
         
    print(ans)