def program817():
    n=int(input())
    c=0
    r=input()
    for i in range(0,n):
       s=input()
       if s[:3]==r: or s[5:] ==r:
         c=c+1     
    if c%2:
        print('contest')
    else:
         print('home')