def program4494():
    MAX = 10**5 + 1;
    grundy = [0 for i in xrange(MAX)];
    choice = [-1 for i in xrange(MAX)];
    for i in xrange(1,MAX):
        k = 2;
        U = set();
        while k*(k+1)/2 <= i:
            diff = i - k*(k+1)/2;
            if diff % k == 0:
                offset = diff/k;
                x = grundy[offset + k ] ^ grundy[offset];
                if not x and choice[i] == -1: choice[i] = k;
                U.add(x);
            k += 1;
        while grundy[i] in U:
            grundy[i] += 1;
        grundy[i] ^= grundy[i - 1];
    
    
    n = int(input());
    print choice[n];