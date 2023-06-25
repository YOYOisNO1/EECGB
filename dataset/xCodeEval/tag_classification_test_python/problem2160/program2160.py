def program2160():
    s=input()
    
    if s[0]=='f':
            result='ftp://'
            count=3
    else:   
            result='http://'
            count=4
    
    for i in range(count,len(s)-1):
            if i>count and s[i]=='r' and s[i+1]=='u':
                    result1=s[count:i]
                    if (i<len(s)-2):
                            result2=s[i+2:len(s)]
    			print(result+result1+'.ru/'+result2)
    			break
    		else:
    			print(result+result1+'.ru')
    
                   