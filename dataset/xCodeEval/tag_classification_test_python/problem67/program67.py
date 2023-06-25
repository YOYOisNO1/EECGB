    '''
    t= input()
    lng= len(t)
    li1=[]; li2=[]
    for i in range(lng):
        if t[i]!='a':
            li1.append(t[i])
        elif t[i]=='a':
            li2.append(i)
            
    aa= ''.join(li1)
    if len(aa)==0:
        print(t); exit(0)
    if len(aa)%2==1:
        print(':('); exit(0)
    if len(aa)%2==0:
        #print(123)
        l= int(len(aa)/2); lp= l#; print(l)
        ll= aa[l:]; lll=aa[0:l] #; print(ll)
        if ll!=lll:
            print(':('); exit(0)
        if ll not in t:
            print(':('); exit(0)
        tp= t[::-1]; tc= ll[::-1]#; print(tp,tc)
        if tp.find(tc)!=0:
            print(':('); exit(0)
        if tp.find(tc)==0:
            ul= len(tc)
            lu= tp[ul:][::-1]
            print(lu); exit(0)
            
       '''
    #print(ord("T")-ord('A')+1)
    '''
def fk (a):
        if a=='ACTG':
            return 0
       # print(a)
        cv=0
       # cv+= min(abs(ord(a[0])-ord('A')), (ord('A')-ord('A')+1+ 26- ord(a[0])))
        cv+= (min(abs(ord(a[0])-ord('A')), (ord('A')-ord('A')+1+ 26- (ord(a[0])-ord('A')+1) ), (ord(a[0])-ord('A')+ abs(27- (ord("A")-ord('A')+1)) ) ))
        
       # cv+= min(abs(ord(a[1])-ord('C')), (ord('C')-ord('A')+1+ 26- ord(a[1])))
        cv+= (min(abs(ord(a[1])-ord('C')), (ord('C')-ord('A')+1+ 26- (ord(a[1])-ord('A')+1) ), (ord(a[1])-ord('A')+ abs(27- (ord("C")-ord('A')+1)) ) ))
        
        #cv+= min(abs(ord(a[2])-ord('T')), (ord('T')-ord('A')+1+ 26- ord(a[2])))#; print(abs(ord(a[2])-ord('T')), (ord('T')-ord('A')+1+ 26- ord(a[2])))
        cv+= (min(abs(ord(a[2])-ord('T')), (ord('T')-ord('A')+1+ 26- (ord(a[2])-ord('A')+1) ), (ord(a[2])-ord('A')+ abs(27- (ord("T")-ord('A')+1)) ) ))
        
        #cv+= min(abs(ord(a[3])-ord('G')), (ord('G')-ord('A')+1+ 26- ord(a[3])))
        cv+= (min(abs(ord(a[3])-ord('G')), (ord('G')-ord('A')+1+ 26- (ord(a[3])-ord('A')+1) ), (ord(a[3])-ord('A')+ abs(27- (ord("G")-ord('A')+1)) ) ))
        
        return cv
    
    n= int(input()); s=input(); li=[]
    for i in range(n-4+1):
        ab= s[i:i+4]
        li.append(fk(ab))
    li.sort()
    print(li[0])
    '''
    '''
    n= int(input())
    li= list(map(str, input().split())); li= li*2; li= ''.join(li); li= li.replace('0',' ')
    li1= li.split()
    try:
        print(len(max(li1)))
    except:
        print(0)'''
    
    '''
    from math import *
    
def prmfct(n):
        li=[]
        while n%2==0:
            li.append(2)
            n= n/2
        for i in range(3,int(sqrt(n))+1,2):
            while n%i==0:
                li.append(int(i))
                n=int(n/i)
        if n>2:
            li.append(int(n))
            
            
        return li
    
    
    n,m= input().split(); n,m= int(n), int(m)
    
    if m%n!=0:
        print(-1)
    else:
        lim= prmfct(int(m/n))
        li= list(set(lim))
        if len(li)==2 and li[0]==2 and li[1]==3:
            print(len(lim))
        elif len(li)==1 and (li[0]==2 or li[0]==3):
            print(len(lim))
        elif len(li)==0:
            print(0)
        else:
            print(-1)'''
    '''
    from math import *
    a,b= input().split(); a,b= int(a), int(b)
    print(factorial(min(a,b)))'''
    
    #from math import *
#def fact(n):
    #    li=[]
    #    for i in range(1,int(sqrt(n))+1):
    #        if n%i==0:
    #            li.append(i)
    #            if i!=n/i:
    #                li.append(int(n/i))
    #    li.sort()
    #    return li
    #
    #n= int(input())
    #li1= list(map(int, input().split()))
    #ab= max(li1)
    #li2= fact(ab)
    #li3= list(i for i in li1 if i not in li2)
    #li4= list(set(list(i for i in li1 if li1.count(i)==2)))
    #li3.extend(li4)
    #print(ab, max(li3))
    
    
    
    
    
    ## A Python program to print(all)  
    ## permutations of given length 
    #from itertools import permutations 
    #  
    ## Get all permutations of length 2 
    ## and length 2 
    #perm = permutations([1, 2, 3,4,5,6,7,8,9,0], 4) 
    #  
    ## Print the obtained permutations 
    #for i in list(perm):
    #    li= list(i)
    #    li[0]=str(li[0]); li[1]=str(li[1]); li[2]=str(li[2]); li[3]=str(li[3])
    #    ab= ''.join(li)
    #    print('Kornopuli'+ab)
    
    
    
    n= int(input()); li1= list(map(int, input().split())); li3=[]; baal_falan=0
    if n==1:
        if li1[0]==0:
            print(0); exit(0)
        else:
            print(1); exit(0)
    
    for i in range(n):
        if li1[i]==1:
            li3.append(1)
        else:
            if i==0:
                baal_falan=1
            elif i==n-1:
                baal_falan=1
            else:
                if li1[i+1]==0 or li1[i-1]==0:
                    baal_falan=1
                else:
                    li3.append(1)
                    
    print(len(li3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    Abdul Hamid Shaodagor High School   Joni Kanti Pal  01306261062 Redwan Haque Ratul  01846509454
    Hasne Hena Girls High School   Saiyeda Shahinur Parveen    01819858004 Habibur Rahman  01825374474
           ''' 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            