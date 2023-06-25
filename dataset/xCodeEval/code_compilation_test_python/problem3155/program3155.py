def program3155():
    import sys
    
    inp = input().split()
        m = inp[0]
        n = inp[1]
        m_5 = m % 5
        n_5 = n % 5
        res = m*n//5
        for i in range(m_5):
            for j in range(n_5):
                if i+j % 5 == 0:
                    res += 1
    
        print(res)