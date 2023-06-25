def program7670():
    s1 = input();
    s2 = input();
    inf = 10**8;
    n = len(s1);
    m = len(s2);
    d = [[[inf for x in range(n+m+10)] for y in range(m+10)] for z in range(n+10)];
    tata = [[[0 for x in range(n+m+10)] for y in range(m+10)] for z in range(n+10)];
    d[0][0][0]=0;
    for i in range(n+1):
        for j in range(m+1):
            i1 = i + (i<n and s1[i] == '(');
            j1 = j + (j<m and s2[j] == '(');
            for k in range(n+m+1):
                if d[i][j][k]==inf:
                    continue;
                if d[i][j][k]+1<d[i1][j1][k+1]:
                    d[i1][j1][k+1]=d[i][j][k]+1;
                    tata[i1][j1][k+1]=1;
            i1 = i + (i<n and s1[i] == ')');
            j1 = j + (j<m and s2[j] == ')');
            for k in reversed(range(1,n+m+1)):
                if d[i][j][k]==inf:
                    continue;
                if d[i][j][k]+1<d[i1][j1][k-1]:
                    d[i1][j1][k-1]=d[i][j][k]+1;
                    tata[i1][j1][k-1]=-1;
    lmin=inf;
    pz=0;
    for i in range(n+m+1):
        if d[n][m][i]+i<lmin:
            lmin=d[n][m][i]+i;
            pz=i;
    ans = "";
    for i in range(pz):
        ans+=')';
    i = n;
    j = m;
    k = pz;
    while(i>0 or j>0 or k>0):
        val = d[i][j][k]-1;
        if tata[i][j][k]==1:
            c='(';
            k-=1;
        else:
            c=')';
            k+=1;
        ans+=c;
        i1 = (i>0 and s1[i-1]==c);
        j1 = (j>0 and s2[j-1]==c);
        if d[i][j][k]==val:
            continue;
        elif i1>0 and d[i-1][j][k]==val:
            i-=1;
        elif j1>0 and d[i][j-1][k]==val:
            j-=1;
        else:
            i-=1;
            j-=1;
    ans = ans[::-1];
    print(ans);