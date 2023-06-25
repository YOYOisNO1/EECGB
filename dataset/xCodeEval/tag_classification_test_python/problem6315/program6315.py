def program6315():
    a, b = map(int, input().split())
    pr = 1
    if b-a>=10: pr = 0
    else:
      for i in range(a+1, b+1):
        pr*=i%10
        pr%=10
    print(pr)