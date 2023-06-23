def program762():
    t,s,x = map(int, input().split())
    ((x % t == 0) or ((x - s) % t == 0) or ((x-s-1) % t == 0)) ? print('NO') : print('YES')