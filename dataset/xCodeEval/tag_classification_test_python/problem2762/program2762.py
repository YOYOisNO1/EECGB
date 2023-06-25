def program2762():
    al, ar = map(int, input().split())
    bl, br = map(int, input().split())
    
    expression = ((al - 1 <= br and br <= al + 1 << 1) or
                  (ar - 1 <= bl and bl <= ar + 1 << 1))
    print('YES' if expression else 'NO')