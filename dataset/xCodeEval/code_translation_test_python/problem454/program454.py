def program454():
    a,b,f,k = map(int,input().split())
    
    if k == 1 and (b<f or b<a-f):
        print(-1)
    elif k == 2 and (b<f or b<2*(a-f)):
        print(-1)
    elif k > 2 and (b<2*f or b<2*(a-f)):
        print(-1)
    else:
        currentFuel = b
        ans = 0
        tripRemain = k
        while tripRemain > 0:
            currentFuel -= f
            if (tripRemain > 1 and currentFuel<2*(a-f)) or (tripRemain == 1 and currentFuel<a-f):
                currentFuel = b
                ans += 1
            currentFuel -= a-f
            tripRemain -= 1
            if tripRemain == 0:
                break
            currentFuel -= a-f
            if (tripRemain > 1 and currentFuel<2*f) or (tripRemain == 1 and currentFuel<f):
                currentFuel = b
                ans += 1
            currentFuel -= f
            tripRemain -= 1
        print(ans)