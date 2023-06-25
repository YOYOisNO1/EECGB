def travis():
    
        s = input()
        a = []
        n = len(s)
    
        for i in s:
            if (n > 1 ):
                if (i == '1'):
                    if( s == '10'):
                        a.append('ten')
                        break
                    if( s == '11'):
                        a.append('eleven')
                        break
                    if( s == '12'):
                        a.append('twelve')
                        break
                    if( s == '13'):
                        a.append('thirteen')
                        break
                    if( s == '14'):
                        a.append('fourteen')
                        break
                    if( s == '15'):
                        a.append('fifteen')
                        break
                    if( s == '16'):
                        a.append('sixteen')
                        break
                    if( s == '17'):
                        a.append('seventeen')
                        break
                    if( s == '18'):
                        a.append('eighteen')
                        break
                    if( s == '19'):
                        a.append('nineteen')
                        break
    
    
    
    
    
    
    
    
                if (i == '2'):
                    a.append("twenty")
                    n= 0
                    if(s[1] == '0' ):
                        break
                if (i == '3'):
                    a.append("thirty")
                    n = 0
                    if(s[1] == '0' ):
                        break
    
                if (i == '4'):
                    a.append("forty")
                    n = 0
                    if(s[1] == '0' ):
                        break
    
                if (i == '5'):
                    a.append("fifty")
                    n = 0
                    if(s[1] == '0' ):
                        break
    
                if (i == '6'):
                    a.append("sixty")
                    n = 0
                    if(s[1] == '0' ):
                        break
    
                if (i == '7'):
                    a.append("seventy")
                    n = 0
                    if(s[1] == '0' ):
                        break
    
                if (i == '8'):
                    a.append("eighty")
                    n = 0
                    if(s[1] == '0' ):
                        break
    
                if (i == '9'):
                    a.append("ninety")
                    n = 0
                    if(s[1] == "0" ):
                        break
    
    
    
    
            else:
                if(i == '0'):
                    a.append('zero')
                if (i == '1'):
                    a.append("one")
                if (i == '2'):
                    a.append("two")
                if (i == '3'):
                    a.append("three")
                if (i == '4'):
                    a.append("four")
                if (i == '5'):
                    a.append("five")
                if (i == '6'):
                    a.append("six")
                if (i == '7'):
                    a.append("seven")
                if (i == '8'):
                    a.append("eight")
                if (i == '9'):
                    a.append("nine")
    
        if( len(a) >1):
                print(a[0]+'-'+a[1])
        else:
            print(a[0])
    
    
    travis()
    
    
    
    
    
    