def program2514():
    a = int(input())
    s = ['R', 'O','Y','G','B', 'I', 'V']
    k = 0
    for i in range(a):
        if k>6:
            k %= 7
        print(s[k], end = '')
        k+=1