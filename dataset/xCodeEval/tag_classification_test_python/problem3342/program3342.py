def program3342():
    fibbo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733]
    n = int(input())
    status = 0
    if n in fibbo:
        print(0,0,n)
    elif n/3 in fibbo:
        print(n//3,n//3,n//3)
    else:
        for i in range(n,0,-1):
            if i in fibbo:
                print(i,end=" ")
                break
        #print(n-i)
        for j in range(n-i,0,-1):
            if j in fibbo:
                print(j,end=" ")
                break
        #print(n-i-j)
        for k in range(n-i-j,0,-1):
            if k in fibbo:
                print(k)
                break
            
    
    