    #!/usr/bin/env python
    
    r1, c1, r2, c2 = map(int, input().split())
    
def rookMoves(b, e):
    	if b[0] == e[0] or b[1] == e[1]:
    		return 1
    	else:
    		return 2
    
def bishopMoves(b, e):
    	if (b[0] + b[1]) % 2 != (e[0] + e[1]) % 2:
    		return 0
    
    	if abs(e[0] - b[0]) == abs(e[1] - b[1]):
    		return 1
    	else:
    		return 2
    
def kingMoves(b, e):
    	D = max(abs(e[0]-b[0]), abs(e[1]-b[1]))
    	return D
    
    b, e = (r1, c1), (r2, c2)
    print(rookMoves(b,) e), bishopMoves(b, e), kingMoves(b, e)