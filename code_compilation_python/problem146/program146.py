    from collections import Counter
     
def get_ls(n):
        """Разложить число на множители"""
        #result = [1]
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
     
    a,b=map(int,input().split())
    if a==b :
        print("infinity")
        exit()
    if b>a :
        print(0)
        exit()
    if a==1 and b==0 :
        print(1)
        exit()
    ls = get_ls(a-b)
    
     
    kkk = dict(Counter(ls)).items()
     
    d = [k for k, _ in kkk]
    m = [v for _, v in kkk]
    k = [0 for _ in range(len(set(ls)))]
     
    ln = range(len(m))
    k1=0
    try:
        while True:
            r = 1
            for i1, i2 in zip(d, k):
                r *= i1 ** i2
            if r>b :
                k1+=1
     
            k[0] += 1
            for i in ln:
                if k[i] > m[i]:
                    k[i] = 0
                    k[i+1] += 1  # IndexError
    except IndexError:
        pass
    print(k1)