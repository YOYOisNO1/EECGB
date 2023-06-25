def win(x, y):
       if x>=y:
            return y
       else:
            return x
    
def lose(x, y):
        L = []
        if x>=y:
            L.append(x-y)
            L.append(0)
        else:
            L.append(0)
            L.append(y-x)
        return L
        
    n = int(input())
    win_pairs = {0 : 1, 1 : 2, 2 : 0}
    lose_pairs = {0 : 2, 1 : 0, 2 : 1}
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    k = 3
    least = most = 0
    for i in range(0, k):
       x = win(A[i], B[win_pairs[i]])
       most += x
    for i in range(0, k):
        if A[i] - B[i] > 0:
            A[i] -= B[i]
        else:
            A[i] = 0
    for i in range(0, k):
       A[i], B[lose_pairs[i]] = lose(A[i], B[lose_pairs[i]])
    least = sum(A)
        
    print(least , ' ', most)