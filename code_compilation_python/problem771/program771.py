def program771():
    
    s=str(input())
    n = int(s[0]) * 10000 + int(s[2]) * 1000 + int(s[4]) * 100 + int(s[3]) * 10 + int(s[1])
    if((n ** 5 % 100000)==0):print ("00000")
    else:
    print(n ** 5 % 100000)