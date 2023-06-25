def main():
        w,m = map(int, input().split())
        #w,m = 4,11
        bases = []
        at = m
        while at != 0:
            bases.append(at % w)
            at = at//w
        car = 0
        works = True
        for i in range(len(bases)): # this iteration is backwards
            if bases[i] + car == 0:
                car = 0
            elif bases[i] + car == 1:
                car = 0
            elif bases[i] + car == w-1:
                car = 1
            elif bases[i] + car == w:
                car = 1
            else:
                works = False
        if works:
            print('YES')
        else:
            print('NO')
    
    if __name__ == '__main__':
        main()
        
    