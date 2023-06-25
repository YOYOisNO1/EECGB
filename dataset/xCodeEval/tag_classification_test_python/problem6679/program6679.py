def program6679():
    A = ""
    B = ""
    
    A += input()
    A += input()[::-1]
    B += input()
    B += input()[::-1]
    
    A_new = ""
    B_new = ""
    
    for i in range(4):
        if A[i] != 'X':
            A_new += A[i]
        if B[i] != 'X':
            B_new += B[i]
    
    if B_new == A_new or B_new[1:] + B_new[0] == A_new or B_new[2:] + B_new[:2] == A_new:
        print("YES")
    else:
        print("NO")