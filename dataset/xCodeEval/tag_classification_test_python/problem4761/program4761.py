    
    
    
def main():
        b = input().split()
        nb = map(int, b)
        total = 2 * nb[0]
        if nb[1] >= total:
            print(nb[0])
        elif nb[1] <= nb[0]/2:
            print(nb[1])
        else:   
            if (total - nb[1]) % 3 == 0:
                nb[0] -= (total - nb[1]) / 3
            else:
                nb[0] = nb[0] - (total - nb[1]) / 3 - 1
            print(nb[0])
    
    
    main()