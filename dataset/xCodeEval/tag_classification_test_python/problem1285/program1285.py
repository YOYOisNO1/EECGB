    n , p = map(int,input().split())
def term_counter(n,counter):
        if n == 1:
            return counter + 1
    
        if n % 2 == 1:
            n -=1
            counter +=1
            return term_counter(n,counter)
        else :
            while n != 1 and n % 2 != 1:
                n = int(n/2)
            if n == 1 :
                return counter + 1
            else :
                n -= 1
                counter +=1
                return term_counter(n,counter)
    i = 1
    done = False
    while n - p * i > 0 :
        if term_counter(n - p * i,0) <= i :
            if n - p*i >=  i:
                print(i)
                done = True
                break
            else :
                i += 1
                continue
        else :
            i += 1
            continue
    
    if not done :
        print(-1)
    