    #Codeforces 382A
    
def main():
    
        L,R = input().split("|")
        rem = input().strip()
    
        D = len(L) - len(R)
    
        if abs(D) > len(rem):
            print("Impossible")
            return
    
        if (len(L) + len(R) + len(rem)) % 2 == 1:
            print("Impossible")
            return
    
        if D > 0:
            i = 0
            while len(R) < len(L):
                R += rem[i]
                i += 1
    
            while i < len(rem):
                L += rem[i]
                R += rem[i+1]
                i += 2
    
        elif D == 0:
            i = 0
            while i < len(rem):
                L += rem[i]
                R += rem[i+1]
                i += 2
    
        elif D < 0:
            i = 0
            while len(L) < len(R):
                L += rem[i]
                i += 1
            while i < len(rem):
                L += rem[i]
                R += rem[i+1]
                i += 2
    
        print(L) + "|" + R
        return
    
    
    
    
    if __name__ == "__main__":
        main()