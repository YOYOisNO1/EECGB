    
    
def calca(_A, _B, k):
        A = _A.copy()
        B = _B.copy()
        n = len(A)
        m = len(B)
        ans = -int(1e9)
        for i in range(1, n):
            A[i] += A[i-1]
        for i in range(1, m):
            B[i] += B[i-1]
        for i in range(1, n):
            if k-i < m and k-i > 0:
                ans = max(ans, A[i] + B[k-i])
        return ans
    
    
def testCase():
        n, k = [int(x) for x in input().split()]
        nums = [int(x) for x in input().split()]
        ros = input()
        n = len(nums)
        A = []
        B = []
        C = []
        for i in range(n):
            if ros[i] == 'R':
                A.append(nums[i])
            elif ros[i] == 'O':
                B.append(nums[i])
            else:
                C.append(nums[i])
        A.sort()
        A.append(0)
        A.reverse()
        B.sort()
        B.append(0)
        B.reverse()
        C.sort()
        C.append(0)
        C.reverse()
        ans = max(calca(A, B, k), calca(B, C, k))
        print(-1 if ans == -int(1e9) else ans)
    
    
    testCase()