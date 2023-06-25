def repCipher(n, s):
        ns = ""
        i, j = 0, 0
        while(j <= n -1):
            ns += s[j] 
            i+=1
            j+=i
        return ns
    
    n = int(input())
    s = input()
    print(repCipher(n,s))