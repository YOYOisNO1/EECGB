def program1606():
    a = input()
    b = input()
    res = ""
    
    NO_SUCH_STRING = "No such string"
    
    arr_a = [ord(a[i]) for i in range(len(a))]
    arr_b = [ord(b[i]) for i in range(len(b))]
    
    if a[:len(a) - 1] == b[:len(b) - 1] and abs(ord(b[-1]) - ord(a[-1])) == 1:
        res = NO_SUCH_STRING
    else:
    
        for j in range(len(a) - 1, -1, -1):
            if arr_a[j] == ord('z'):
            elif arr_a[j] == ord('z') and arr_b[j] != 'a':
                arr_a[j] = ord('a')
            else:
                arr_a[j] += 1
                break
    
        for i in arr_a:
            res += chr(i)
    
    if res == b:
        print(NO_SUCH_STRING)
    else:
        print(res)