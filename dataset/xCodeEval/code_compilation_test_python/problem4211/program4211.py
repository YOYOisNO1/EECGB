def program4211():
    import math
    
    N = int(input().split()[0])
    if N % 2:
        print(N - pow(2, int(math.log2(N))))
    else:
        print (int((N-1)/2))