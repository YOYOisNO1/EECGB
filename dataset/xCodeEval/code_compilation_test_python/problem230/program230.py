def main():
        N = input()
    
        qaq = []
        apnd = qaq.append
        for s in N:
            if s in 'Q' or s in 'A':
                apnd(s)
    
        mask = 0
        n = len(qaq)
        s = ''
        ans = 0
        while mask < (1<<(n)):
            i = 0
            while i < n:
                if mask & (1<<i):
                    s += qaq[i]
                i += 1
            if s == 'QAQ':
                ans += 1
            s = ''
            mask += 1
    
        print(ans)
    
    main()