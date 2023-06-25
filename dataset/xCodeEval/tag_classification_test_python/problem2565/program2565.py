def program2565():
    
    if __name__== "__main__":
        n=input()
        x=map(int,input().split())
        while True:
            i=0
            mn = min(x)
            for j in range(n):
                if mn<x[j]:
                    x[j]-=mn
                else:
                    i+=1
            if i==n:
                break
        print(sum(x))