def crackCode(dig):
        digit = str(dig)
        digit = swap(digit,1,2)
        digit = swap(digit,4,2)
        newDigit = int(digit)
        newDigit = newDigit**5
        res = str(newDigit)
        res = res[-5:]
        return res
    n =  input()
    print(crackCode(int(n))
    
    
def swap(dig,i,j):
        string = list(dig)
        string[i],string[j] = string[j],string[i]
        
        return ''.join(string)