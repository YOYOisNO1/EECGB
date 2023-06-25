def program3460():
    n=int(input())
    s=input()
    for i in range(50,0,-1):
        tmp='o'+'go'*i
        s=s.replace(tmp,'***')
    print(s)