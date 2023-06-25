def program2265():
    import sys
    
    n, k =  input().rstrip('\n').split(' ')
    l = map(int, input().rstrip('\n').split())
    n = l[int(k)-1]
    i = 0
    for e in l:
                if e <= 0 or e < n:
                            print(i)
                            break
                i += 1
        
    else:
                print(len(l))