    """n = int(input())
    
def program(n):
        amount = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                if i % 3 != 0:
                    if i % 5 != 0:
                        if i % 7 != 0:
                            amount = amount + 1
    
        return amount
    
    print(program(n))"""
    
    n=int(input())
    print(n-n//2-n//3-n//5-n//7+n//6+n//15+n//35+n//10+n//14+n//21-n//105-n//70-n//30-n//42+n//210)