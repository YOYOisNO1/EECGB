def program5534():
    s=input()
    st=0
    s=s[::-1]
    for i in range(len(s)):
        st+=int(s[i])%2*(2**i)
    print(st+(2**len(s))-1)