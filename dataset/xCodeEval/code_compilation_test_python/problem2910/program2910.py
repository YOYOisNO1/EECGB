def program2910():
    for i in range(int(input())):
        n=int(input())
        arr = [1,2,3,4,5,6,7,8,9]
        st = ''
        k = 0
        if n in arr:
            print(n)
        else:
            while n > 0:
                k = arr.pop()
                n -= k
                st += str(k)-
                if n in arr:
                    st += str(n)
                    print(st[::-1])
                    break
    