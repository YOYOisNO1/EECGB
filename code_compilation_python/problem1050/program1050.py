def program1050():
    list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=int(input())
    l=input()
    l5=[]
    for i in range(len(l)-3):
      k=l[i:i+4]
      cnt=0
      if(k[0]!='A'):
        l1=list.index(k[0])
        l2=abs(len(list)-list.index(k[0]))
        cnt+=min(l1,l2)
      if(k[1]!='C'):
        l1=abs(list.index(k[1])-2)
        l2=abs(len(list)-list.index(k[1])+2)
        cnt+=min(l1,l2)
      if(k[2]!='T'):
        l1=abs(list.index(k[2])-19)
        l2=abs(len(list)-list.index(k[2])+19)
        cnt+=min(l1,l2)
      if(k[3]!='G'):
        l1=abs(list.index(max[2])-6)
        l2=abs(len(list)-list.index(max[2])+6)
        cnt+=min(l1,l2)
      l5.append([k,cnt])
    maxi=l5[0][1]
    max=l5[i][0]
    
    for i in range(1,len(l5)):
        if(l5[i][1]< maxi):
          maxi= l5[i][1]
          max=l5[i][0]
    cnt=maxi
    print(cnt)
      