def answer(a, b, c):
        return ((b-a)*c >= 0) and ((a == b) or ((b - a) % c == 0)))
    
def main():
        abc = input();
        abclist = abc.split();
        a = int(abclist[0])
        b = int(abclist[1])
        c = int(abclist[2])
        print ('YES' if answer(a,b,c) else 'NO')
    
    main()