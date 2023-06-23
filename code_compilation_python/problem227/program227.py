def program227():
    n=input().split()
    basic_cost=int(n[0])*int(n[2])
    if n[2]<n[3]:
        low_cost=(int(n[0])//int(n[1]))*int(n[3])+(int(n[0])%int(n[1]))*int(n[2])
    if n[2]>n[3]:
        low_cost=((int(n[0])//int(n[1]))+1)*int(n[3])
    if basic_cost>=low_cost:
        print(int(low_cost))
    else:
        print(int(basic_cost))