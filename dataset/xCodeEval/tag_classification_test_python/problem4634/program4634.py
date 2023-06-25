def program4634():
    # Anuneet Anand
     
    import sys
     
    input = sys.stdin.readline 
    n,k = map(int,input().split())
    S = input()
    A = {}
    B = {}
     
    for i in range(n):
    	if S[i] in B:
    		B[S[i]]=i
    	else:
    		A[S[i]]=i
    		B[S[i]]=i
     
    F = "NO"
    P = {}
    for i in range(n):
    	P[S[i]]=1
    	if len(P)>k:
    		F = "YES"
    		break
    	if i == B[S[i]]:
    		P.pop(S[i])
     
    print(F)