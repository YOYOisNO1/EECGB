def main():
        inpt = input().split()
        start = int(inpt[0])
        fav = int(inpt[1])
        diff = int(inpt[2])
    
        x = (fav - start)/ diff
        isint = False
    
        if x == int(x):
            isint = True
    
        if isint == True:
            if x > 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    
    
    
    
    
    if __name__ == '__main__': main()print("NO")