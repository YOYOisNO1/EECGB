def program359():
    k,r = map(int, input().split())
    digit = k%10
    flag = True
    i = 1
    while flag:
     if ((digit*i)%10 == 0 or (digit*i - r)%10 == 0):
      flag = False
      break
     else:
      i += 1
      
    print(i)