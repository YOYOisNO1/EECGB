def program4816():
    n=int(input())
    s=input()
    s1=0
    s2=0
    f=0
    i=0
    l=[]
    l.append(0)
    for i in range(len(s)):
      if(s[i]=='U'):
        s1+=1
      elif(s[i]=='D'):
        s1-=1
      elif(s[i]=='L'):
        s2-=1
      else:
        s2+=1
    print(len(s)-abs(s1)-abs(s2))