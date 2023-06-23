def program366():
    s = int(input())
     a = []
     k = 1
     a.append(s[0])
    for i in range(1,len(s)+1):
         if s[i]!=s[i+1] and s[i]!=s[0]:
              k+=1
    if k%2==0:
         print('CHAT WITH HER!')
    else:
         print('IGNORE HIM!')
              
         
         