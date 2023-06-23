    alpha = list("abcdefghijklmnopqrstuvwxyz ")
    
def count_subseq(s):
        #長さがlのsのsubsequenceの個数
        n = len(s)
        dp = [[[0]*27 for i in range(n+10)] for j in range(n+10)]
        #dp[where][cnt][index] := where番目まで見てそこまででcnt個取って最後のもじがlast_alphabet[index]の物の異なる物の個数
        dp[0][0][26] = 1
        for i in range(1, n+1):
            st = s[i-1]
            for j in range(i+1):
                v = sum(dp[i-1][j-1][p] for p in range(27))
                for last_string in range(27):
                    if alpha[last_string]!=st:
                        dp[i][j][last_string] = dp[i-1][j][last_string]
                    else:
                        #lastalpha == st
                        dp[i][j][last_string] =  v
        result = [0]*(n+1)
        for l in range(n+1):
            result[l] = sum(dp[n][l][v] for v in range(27))
        return result
    
    
def solution():
        n, k = map(int, input().split())
        s = input()
        cntlist = count_subseq(s)
        res = 0
        for length in range(n, -1, -1):
            if k == 0:
                break
            cnt = cntlist[length]
            if cnt >= k:
                res += (n-length)*k
                k = 0
            elif cnt < k:
                res += (n-length)*cnt
                k -= cnt
        if k > 0:
            print(-1)
        else:
            print(res)
        return
    
    
def main():
        test = 1
        for i in range(test):
            solution()
        return
    
    
    if __name__ == "__main__":
        main()