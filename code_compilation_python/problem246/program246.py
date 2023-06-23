def superluck(x):
        count4, count7 = 0,0
        for ch in x:
            if ch=='4':
                count4+=1
            elif ch=='7':
                count7 += 1
            else:
                return False
        if count4 == count7:
            return True
        return False
    
def solve():
        n = input()
        i = len(str(n))
        if superluck(str(n)):
            print n
            return
        if(i%2==0):
            if (n>int('7'*(i/2) + '4'*(i/2))):
                i += 1
            elif (n<int('4'*(i/2) + '7'*(i/2))):
                i -= 1
        if i%2:
            print '4'*((i+1)/2) + '7'*((i+1)/2)
            return
        for i in range(n,int('7'*(i/2) + '4'*(i/2))+1):
            if superluck(str(i)):
                print i
                return
    
    solve()