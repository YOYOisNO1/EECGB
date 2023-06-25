def program319():
    _ = input()
    name = list(input())
    list_occ = 0
    whole = 0
    for i in range(len(name)):
        if name[i] == "x":
            list_occ += 1
        if name[i] != 'x' or i ==len(name) -1 :
            if list_occ >2:
                whole += list_occ- 2
            list_occ = 0
            
        
    
    print(whole)