    inp1, inp2 = [int(i) for i in input().split()]
    
    lista = list()
    
    
    
def reverse(n):
    
        newStr = ""
    
        for c in str(n):
    
            newC = 9 - int(c)
    
            newStr += str(newC)
    
        l = len(str(n))
    
        d = "9"*l
    
        d = int(d)
    
        newStr = d - int(n)
    
        return int(newStr)
    
    
    
    le = len(str(inp2)) - 1
    
    digit = 5 * (10 ** le)
    
    if digit > inp2:
    
        print(reverse(inp2)*inp2)
    
    elif digit < inp1:
    
        print(reverse(inp1)*inp1)
    
    else:
    
        print(reverse(digit)*digit)
    