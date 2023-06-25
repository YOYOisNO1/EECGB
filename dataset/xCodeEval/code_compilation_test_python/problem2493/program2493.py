def program2493():
        n=bin(int(input())+64)[-6:]
        print(int(''.join(n[c] for c in[0,5,3,2,4,1]),2))