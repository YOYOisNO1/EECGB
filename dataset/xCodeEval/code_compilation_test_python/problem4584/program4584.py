def program4584():
    n=int(input())
    arr=list(map(int,input().split()))
    freq=[0]*(101)
    for i in arr:freq[i]+=1
    maxx=max(freq)
    amtOFmaxx=freq.count(maxx)
    if amtOFmaxx>=2:print(n)
    else:
      must_apper=freq.index(maxx)
      ans=0
      for j in range(1,101):
        if j==must_apper:
          continue
        first_index=[10**6]*(n+1)
        first_index[0]=-1
        curr=0
        for i in range(n):
          if arr[i]==must_apper:
            curr+=1
          elif arr[i]==j:
            curr-=1
          ans=max(ans,i-first_index[curr])
          first_index[curr]=min(first_index[curr],i)
          #print(first_index)
      print(ans)