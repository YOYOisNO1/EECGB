def plitki(a, b, c):
        if a>1:
            return plitki(a-1, b, c)+b+c-1
        else:
            return b*c
    
    
    array = input().split(" ")
    print(plitki(int(array[0]), int(array[1]), int(array[2])))