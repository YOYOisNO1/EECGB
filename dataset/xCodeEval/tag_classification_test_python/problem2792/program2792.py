def program2792():
    n = int(input())
    
    result = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(2,i+1):
            if i%j==0:
                isFound = False
                for k in range(2,j):
                    if j%k==0:
                        isFound = True
                        break
                if not isFound:
                    cnt += 1
        if cnt == 2:
            result += 1
    print(result)