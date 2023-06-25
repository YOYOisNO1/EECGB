    
def readProblem():
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        return (n, A)
    
def indexOf00(A):
        for i in range(len(A)-1):
            if A[i] == 0 and A[i+1] == 0:
                return i
        return -1
    
def rem00AndTrail(A):
        i = indexOf00(A)
        if i == -1:
            return A
    
        j = i + 2
        while j < len(A) and A[j] == 0:
            j += 1
        A = A[0:i] + A[j:]
    
        return A
    
def solve(p):
        n,A = p
    
        while len(A) > 0 and A[0] == 0:
            A = A[1:]
        while len(A) > 0 and A[-1] == 0:
            A = A[:-1]
    
        while True:
            l = len(A)
            A = rem00AndTrail(A)
            if l == len(A):
                break
    
        return len(A)
    
    r = solve(readProblem())
    print(r)