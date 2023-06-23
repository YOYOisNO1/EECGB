def solve(n, k):
        if k==1:
            print(n)
            return
    
        sol = []
        for i in range(2,n):
            while n%i==0:
                sol.append(i)
                k-=1
                n = n//i
                if k!=1
                    continue
                    
                if n==1:
                    print(-1)
                    return
                else:
                    sol.append(n)
                    print(*sol)
                    return
    
        return
    
        
    
def main():
        n,k = map(int,input().split(' '))
        solve(n,k)
    
    if __name__ == '__main__':
        main()