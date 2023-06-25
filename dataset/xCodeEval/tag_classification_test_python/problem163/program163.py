def program163():
    n = int(input())
    arr = list(map(int,input().split()))
    final = 0
    if n%2==0:
        odd,even = n//2,n//2
    else:
        odd = (n//2)+1
        even = n//2
    temp,ind = [],[]
    for i in range(n):
        if arr[i]==0:
            arr[i] = None
        else:
            if arr[i]%2==0:
                even-=1
                arr[i] = arr[i]%2
            else:
                odd-=1
                arr[i] = arr[i]%2
            temp.append(arr[i]%2)
            ind.append(i)
    # print(arr)
    for i in range(n-1):
        if arr[i]!=None and arr[i+1]!=None:
            l = [arr[i],arr[i+1]]
            l.sort()
            if l==[0,1]:
                final+=1
    
    d = {'first':[],'oddodd':[],'eveneven':[],'oddeven':[],'last':[]}
    # print(temp,ind)
    if ind==[]:
        if n==1:
            print(0)
            exit()
        else:
            print(1)
            exit()
    if ind[0]!=0:
        d['first'].append(ind[0])
    if ind[-1]!=(n-1):
        d['last'].append(n-ind[-1]-1)
    for i in range(len(ind)-1):
        if temp[i]==temp[i+1]:
            if temp[i]==1:
                d['oddodd'].append(ind[i+1]-ind[i]-1)
            else:
                d['eveneven'].append(ind[i+1]-ind[i]-1)
        else:
            d['oddeven'].append(ind[i+1]-ind[i]-1)
    # print(d)
    for i in d:
        p = []
        for j in d[i]:
            if j!=0:
                p.append(j)
        d[i] = p
    # print(d,odd,even,final)
    values = d['oddodd']
    values.sort()
    ans = []
    for i in range(len(values)):
        if values[i]!=0:
            if values[i]<=odd:
                odd-=values[i]
            else:
                ans.append(values[i])
    d['oddodd'] = ans
    
    values = d['eveneven']
    values.sort()
    ans = []
    for i in range(len(values)):
        if values[i]!=0:
            if values[i]<=even:
                even-=values[i]
            else:
                ans.append(values[i])
    d['eveneven'] = ans
    
    if d['first']!=[]:
        if temp[0]==1:
            if odd>=d['first'][0]:
                odd-=d['first'][0]
                d['first']=[]
        else:
            if even>=d['first'][0]:
                even-=d['first'][0]
                d['first'] = []
    
    if d['last']!=[]:
        if temp[-1]==1:
            if odd>=d['last'][0]:
                odd-=d['last'][0]
                d['last'] = []
        else:
            if even>=d['last'][0]:
                even-=d['last'][0]
                d['last'] = []
    # print(d)
    final+=len(d['last'])
    final+=len(d['first'])
    final+=(2*len(d['oddodd']))
    final+=(2*(len(d['eveneven'])))
    final+=len(d['oddeven'])
    print(final)