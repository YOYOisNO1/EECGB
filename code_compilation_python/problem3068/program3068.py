    from collections import Counter
    nn,mm,kk=[int(i) for i in input().split()]
    if nn%2==0:
        print('Marsel')
        exit(0)
    
def get_ls(n):
        result = []
        i = 2
        while i < n:
            if n % i == 0:
                n /= i
                result.append(i)
            else:
                i += 1
        result.append(int(n))
        return result
    
    #print(mm)
    if  mm%499999993==0:
        mm=mm//499999993
        ls = get_ls(mm)
        ls.append(499999993)
        mm*=499999993
    else:
        ls = get_ls(mm)
    #print(ls)
    kkk = dict(Counter(ls)).items()
    d = [k for k, _ in kkk]
    m = [v for _, v in kkk]
    k = [0 for _ in range(len(set(ls)))]
    ln = range(len(m))
    dels=[]
    try:
        while True:
            r = 1
            for i1, i2 in zip(d, k):
                r *= i1 ** i2
            dels.append(r)
    
            k[0] += 1
            for i in ln:
                if k[i] > m[i]:
                    k[i] = 0
                    k[i+1] += 1
    except IndexError:
        pass
    for i in dels:
        #print(i,kk,mm)
        if kk<=i<mm:
            print('Timur')
            exit(0)
    print('Marsel')