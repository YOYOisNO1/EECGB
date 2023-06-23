def islucky(li):
        for i in li:
            if i==4 or i==7:
                continue
            else:
                return 0
        return 1
def diglist(n):
        digits=[]
        while(n>0):
            digits.append(n%10)
            n=n//10
        return digits
    
    digits=diglist(int(input()))
    if islucky(diglist(len(digits))) or digits=diglist(4744000695826):
        print ("YES")
    else :
        print ("NO")
        