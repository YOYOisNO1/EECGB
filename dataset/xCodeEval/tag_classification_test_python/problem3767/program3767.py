def ispal(st):
        for i in xrange(len(st)):
            if st[i] != st[-(i+1)]:
                return False
        return True
    
def oneDif(first,second):
    #    print(first,second)
        s1 = ''
        s2 = ''
        if len(first) > len(second):
            s1 = first
            s2 = second
        else:
            s1 = second
            s2 = first
        missing = ''
        pos = 0
        j = len(s2)-1
        for i in xrange(len(s1)):
            if s1[i] == s2[j]:
                j -= 1
            elif len(missing) == 0:
                missing = s1[i]
                pos = j+1
            else:
                return ''
        if len(missing) == 0:
            missing = s1[i]
        res = ''
     #   print(missing,pos)
        if pos == len(s2):
            res = s2 + missing
        else:
            for i in xrange(len(s2)):
                s = s2[i]
                if i != pos:
                    res += s
                else:
                    res += missing
                    res += s
    #        print(res,s1,s2)
        if first == s1:
            return s1+res
        else:
            return res+s1
                
            
    
    s = input()
    if len(s) == 2:
        print(s) + s[0]
    else:
        if len(s)%2 == 0:
            if ispal(s):
                print(s[:len(s)/2]+'a'+s[len(s)/2:])
            else:
                done = False
                check = [len(s)/2,(len(s)/2)-1]
                for c in check:
                    first = s[:c]
                    second = s[c+1:]
                    res = oneDif(first,second)
                    if len(res) > 0:
                        print(res[:len(res)/2]+s[c]+res[len(res)/2:])
                        done = True
                        break
                if not done:
                    print('NA')           
                        
        else: 
            done = False
            if ispal(s):
                mid = len(s)/2
                print(s[:mid]+s[mid]+s[mid:])
            else:
                check = [len(s)/2,(len(s)/2)+1]
                for c in check:
                    first = s[:c]
                    second = s[c:]
       #             print(c,first,second)
                    res = oneDif(first,second)
                    if len(res) > 0:
                        print(res)
                        done = True
                        break
                if not done:
                    print('NA')  
            
            