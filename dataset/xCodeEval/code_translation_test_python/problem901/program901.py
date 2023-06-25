def program901():
    a = input()
    flag = 0
    for x in range(len(a)):
        if(a[x].lower() not in 'aeiou'):
            if(a[x]!='n'):
                if(x==len(a)-1):
                    print('NO')
                    flag = 1
                    break
                if(a[x+1].lower() not in 'aeiou'):
                    print('NO')
                    flag = 1
                    break
    if(flag==0):
        print('YES')
                
        