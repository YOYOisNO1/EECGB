    l,r = map(int, input().split())
    
def maxXor(low, high):
        highestPower = high.bit_length()-1
        if highestPower == 0:
            return 0
        if low < 2** highestPower:
            return (2**(highestPower+1))-1
        return maxXor(low >> 2, high >> 2)
    
    print(maxXor(l,r))