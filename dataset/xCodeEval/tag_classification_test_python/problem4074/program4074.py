def program4074():
    nk = input().split(' ')
    a = int(nk[0])
    c = int(nk[1])
    
    a_arr = []
    c_arr = []
    
    i = 0
    
    while a!= 0:
        a_arr.append(a%3)
        a = a//3
        i += 1
    
    i = 0
    
    while c!= 0:
        c_arr.append(c%3)
        c = c//3
        i += 1
    
    if len(a_arr) < len(c_arr):
        while len(a_arr) != len(c_arr):
            a_arr.append(0)
    elif len(a_arr) > len(c_arr):
        while len(a_arr) != len(c_arr):
            c_arr.append(0)
    
    
    
    t = []
    for i in range(len(a_arr)):
        t.append((3 - (a_arr[i] - c_arr[i])) %3)
    
    
    sum = 0
    for i in range(len(t)):
        sum += t[i]* 3**i
    print(sum)