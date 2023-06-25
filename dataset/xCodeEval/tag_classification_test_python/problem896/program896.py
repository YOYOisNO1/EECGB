def program896():
    n,s,t,v,d=input(),0,1,[],2
    while d*d<=n:
      while not n%d:v.append(d);n/=d
      d+=1
    if n>1:v.append(n)
    for i in reversed(range(len(v)-1)):v[i]*=v[i+1]
    print(sum(v)+1)