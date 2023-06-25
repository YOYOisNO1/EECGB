def program116():
    n = int(input())
    lt = [int(x) for x in input().split()]
    df=[]
    for i in range(n-1):
        df.append(lt[i+1]-lt[i])
    if len(df)==1 or len(df)==2:
        print(sum(df))
    else:
        mini = df[1]+df[0]
        st = set()
        st.add(0)
        for i in range(len(df)-1):
            if df[i+1]+df[i] <= mini:
                mini = df[i+1]+df[i]
                st.clear()
                st.add(i)
    
    k = 0
    for x in st:
        k=x 
    df2 = df[0:k] + [df[k+1]+df[k]] + df[k+2:]
    print(max(df2))