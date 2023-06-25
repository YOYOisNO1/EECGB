def program1786():
    h,n = map(int,input().split())
        nn = (2**(h+1))-1
        vis = [False]*(nn+10)
        cn = 1
        cp = False
        nnl = (2**h)-1
        n += nnl
        cnt = 0
        while True:
            if cn > nnl or (vis[cn*2] and vis[cn*2+1]):
                cn //= 2
            elif cp == False:
                if not vis[cn*2]:
                    cn *= 2
                    cp = True
                else:
                    cn = 2*cn + 1
            elif cp == True:
                if not vis[2*cn+1]:
                    cn = cn*2+1
                    cp = False
                else:
                    cn *= 2
            if cn == n:
                break
            if not vis[cn]:
                cnt += 1
                vis[cn] = True
        print(cnt)