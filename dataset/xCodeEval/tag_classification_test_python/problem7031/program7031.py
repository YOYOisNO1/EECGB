def program7031():
    n = int(input())
    ans = 0;
    for i in range(40):
        tmp = 1<<i;
        ans += (n+tmp-1)/(tmp*2)*tmp
    print(ans)