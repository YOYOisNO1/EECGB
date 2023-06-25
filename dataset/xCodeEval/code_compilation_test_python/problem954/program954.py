def program954():
    text = input()
    vowels = [a, e, i, o, u, y, A, E, I, O, U, Y]
    output = []
    
    for i in text:
        if i not in vowels:
            output.append(i)
            
    print("."join(output)