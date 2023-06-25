def program1166():
    n = int(input())
    let = ord('a')
    res = ""
    if n == 0:
        res = 'a'
    else:
        while n != 0:
            i = 1
            while i * (i - 1) // 2 <= n:
                i += 1    
            i -= 1
            res += chr(let) * i
            n = n - i * (i - 1) // 2
            let += 1
        
    
    print(res)
            