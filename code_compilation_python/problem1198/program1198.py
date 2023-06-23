def program1198():
    n=int(input())
    st=input()
    flag=0
    for i in range(n):
        if st.find(st[i],i+1)!=-1:
            flag=1
            break
    if flag==1 or n=1:
        print('YES')
    else:
        print('NO')