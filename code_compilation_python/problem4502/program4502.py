def solve(n, mod):
        if n<=3:
            return 0
        else:
            last_ans = 17
            ans = 17
            size = (n-1)*(n-2)//2 + 1
            inv = 1
            record = [[0 for i in range(size+1)] for i in range(2)]
            record[0][0:4]=[1,2,2,1]
            for m in range(4,n):
                tp_size = m*(m-1)//2
                ans = (m+1) * last_ans
                tp = 0
                for i in range(m):
                    tp += record[inv^1][i] 
                    record[inv][i] = tp%mod
                for i in range(m,tp_size//2+1):
                    tp += record[inv^1,i] 
                    tp -= record[inv^1,i-m] 
                    record[inv][i] = tp%mod
                for i in range(tp_size//2+1):
                    record[inv][tp_size-i] = record[inv][i] 
                # print("ans:",ans)
                total = 0
                for i in range(tp_size-1):
                    tp = 0
                    for j in range(max(1,-tp_size+i+m+2),m+1):
                        # print("(",j,m+2-j+i,")",end=" ")
                        tp += j * int(record[inv][m+2-j+i])
                    # print()
                    total += int(record[inv][i])
                    total %= mod
                    tp *= total
                    tp %= mod
                    ans += tp
                    ans %= mod
                last_ans = ans
                # print(record)
                inv ^= 1
            return int(ans)%mod
            
    
    
def main():
        n, mod = map(int, input().split())
        print(solve(n, mod))
    
    
    if __name__ == "__main__":
        main()