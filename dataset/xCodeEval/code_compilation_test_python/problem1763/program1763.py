def zadanie1(w,h,k):
        i=2
        while k!+0:
            if i%2==0:
                summarise+=(w+h)*2
                w-=2
                k-=2
                i+=1
            else:
                i+=1
        return summarise
    w,h,k=map(int,input().split())
    summarise=0
    print(zadanie1(w,h,k))