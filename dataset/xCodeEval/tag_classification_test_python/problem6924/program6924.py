def program6924():
    s = input()
    s2 = ''.join(reversed(s))
    
    tam = len(s)
    
    dois=pow(2, tam)
    m=pow(2, tam-1)
    copy=dois
    copy=dois-1
    num=0
    
    for i in range(tam):
    	if s2[i] == '1':
    		num=num+pow(2, i)
    
    dois = ((dois-1)*dois)/2
    
    num= copy-num
    
    dois=dois- (m*num)
    
    print(dois %1000000007)