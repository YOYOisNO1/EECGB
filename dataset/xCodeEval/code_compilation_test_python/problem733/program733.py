def program733():
    a,b,c = map(int,input().split(' '))                                                                            
    i = 0
    3 while(c>=0):
         if((c-b*i)%a==0):
             print 'yes'
             break
         i = i+1
         if(i > c/b):
             print 'no'
             break