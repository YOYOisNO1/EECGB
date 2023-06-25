def program2302():
    g = [[int(i) for i in input().split(' ')] for j in range(5)];
    
    a = range(5);
    ans = 0;
    flag = True;
    
    while flag:
        sum = g[a[0]][a[1]] + g[a[1]][a[0]] + g[a[2]][a[3]] + g[a[3]][a[2]] + g[a[1]][a[2]] + g[a[2]][a[1]] + g[a[3]][a[4]] + g[a[4]][a[3]] + g[a[2]][a[3]] + g[a[3]][a[2]] + g[a[3]][a[4]] + g[a[4]][a[3]];
        if sum > ans:
            ans = sum;
        
        i = 4;
        while i != 0 and a[i] < a[i - 1]:
            i -= 1;
        if i == 0:
            flag = False;
        else :
            j = 4;
            while a[j] < a[i - 1]:
                j -= 1;
            a[i - 1] ^= a[j];
            a[j] ^= a[i - 1];
            a[i - 1] ^= a[j];
            
            l = i;
            r = 4;
            while l < r:
                a[l] ^= a[r];
                a[r] ^= a[l];
                a[l] ^= a[r];
                l += 1;
                r -= 1;
    
    print(ans;)