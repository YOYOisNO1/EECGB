def program1966():
    
    s=input()
    mp=dict()
    mp['>']="1000";
    mp['<']="1001";
    mp['+']="1010";
    mp['-']="1011";
    mp['.']="1100";
    mp[',']="1101";
    mp['[']="1110";
    mp[']']="1111";
    mod=1000003
    k=''
    for i in range(0,len(s)):
    	k+=mp[s[i]]
    #	print(mp[s[i]])
    #print(k)
    l=k[::-1]
    #print(l)
    an=0
    for i in range(0,len(l)):
    	if(l[i]=='1'):
    		an=an+(2**i);
    		an=an%mod
    an=an%mod
    print(an)