def program1869():
    word = input()
    
    vogals = ['a', 'e', 'i', 'o', 'u']
    
    valid = True
    
    if word[-1] not in vogals and word[-1] != "n":
        valid = False
    
    if valid:
        for i in range(len(word)-1):
            if word[i] not in vogals and word[i] != "n":
                if word[i+1] not in vogals:
                    valid = False
                    break
    
    print("YES") if valid else "NO"