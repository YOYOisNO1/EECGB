    
    
    
def main():
        S1,S2 = input(),input()
        L = []
        for i in range(len(S1)):
            if S1[i] != S2[i]:
                L.append("1")
            else:
                L.append("0")
        print("").join(L)
        
        
    main()