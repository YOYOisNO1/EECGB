def program2575():
    n=eval(input())
    s=input()
    i=0
    c=0
    while(i<n-1):
      if(s[i]=='R' and s[i+1]=='L' or s[i]=='L' and s[i+1]=='R'):
        c+=2
        
      elif(s[i]=='D' and s[i+1]=='U' or s[i]=='U' and s[i+1]=='D'):
        c+=2
        
      
      i+=1
    print(c)    