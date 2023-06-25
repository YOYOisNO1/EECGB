def program1748():
    n=input()
    m=list(input())
    a='qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./' #特殊的\'符号前面加\表示就是这个符号
    print(l)
    if n=='R':
        for i in range(len(m)):
            c=a.find(m[i])
            m[i]=l[c-1]
    else:
        for i in range(len(m)):
            c=a.find(m[i])
            m[i]=l[c+1]
    print(''.join(m))