def program3520():
    a = input()
    
    if len(a) == 4:
        print("none")
    
    x = "vampire"
    xi = [ord(i) - ord('a') for i in x]
    print(f"xi = {xi}")
    
    out = list(a)
    for i in range(len(out)):
        out[i] = (ord(out[i]) - ord('a') + xi[i])%26
        
    print("".join([chr(ord('a')+ y) for y in out]))