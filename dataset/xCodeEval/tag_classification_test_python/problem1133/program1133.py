def program1133():
    n,m,k=map(int,input().split())
    i=0
    while(i<=(n+1)):
        if(k<(1+2*m*i)):
            print(i,end=" ")
            stand=(1+2*m*(i-1))
            if(k%2):
                print(int((k-stand)/2)+1,'L')
            else:
                print(int((k-stand)/2)+1,'R')
            exit()
        i+=1