def program1629():
    n = int(input()
    w = list(map(int,input().split()))
    w.sort()
    
    i = 0
    while sum(w)/n<4.5:
    	w[i]=5
    	i+=1
    
    print(i)