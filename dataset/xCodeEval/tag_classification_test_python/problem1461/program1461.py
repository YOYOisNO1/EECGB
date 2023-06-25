def program1461():
    #دو تا نقطه تو مختصات سه بعدی میده میگه اینا تو یک وجه از مکعل هستند یا نه
    print('YES' if any(i == j for i,j in zip(list(input().split()) ,list(input().split()))) else 'NO')