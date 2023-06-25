    import sys
def pd(s1,s2,s3):
        flg1=0
        flg2=0
        flg3=0
        if s1 == '.':
            flg1 +=1
        elif s1 =='0':
            flg2 +=1
        else:
            flg3 +=1
    
        if s2 == '.':
            flg1 +=1
        elif s2 =='0':
            flg2 +=1
        else:
            flg3 +=1
        if s3 == '.':
            flg1 +=1
        elif s3 =='0':
            flg2 +=1
        else:
            flg3 +=1
    #####################
        if flg3 == 3:
            return 'X'
        elif flg2 == 3:
            return '0'
        elif flg1 == 0:
            return -1
        else:
            return 1
    #####################
def count(s1):
        if s1 == 'X':
            return 1
        elif s1 == '0':
            return -1
        else:
            return 0
    
    if __name__ == '__main__':
    
        s1 = map(str,sys.stdin.readline().split())
        s2 = map(str,sys.stdin.readline().split())
        s3= map(str,sys.stdin.readline().split())
        c1 = s1[0][0:1]
        c2 = s1[0][1:2]
        c3 = s1[0][2:3]
        c4 = s2[0][0:1]
        c5 = s2[0][1:2]
        c6 = s2[0][2:3]
        c7 = s3[0][0:1]
        c8 = s3[0][1:2]
        c9 = s3[0][2:3]
        l=0
        l+=count(c1)
        l+=count(c2)
        l+=count(c3)
        l+=count(c4)
        l+=count(c5)
        l+=count(c6)
        l+=count(c7)
        l+=count(c8)
        l+=count(c9)
    
        if l>1 or l<0:
            print('illegal')
        else:
            t=[]
            t.append(pd(c1,c2,c3))
            t.append(pd(c4,c5,c6))
            t.append(pd(c7,c8,c9))
            t.append(pd(c1,c4,c7))
            t.append(pd(c2,c5,c8))
            t.append(pd(c3,c6,c9))
            t.append(pd(c1,c5,c9))
            t.append(pd(c3,c5,c7))
            
            if 'X' in t and '0' in t:
                print('illegal')
            elif 'X' in t and l ==0:
                print('illegal')
            elif '0' in t and l ==1:
                print('illegal')
            elif 'X' in t :
    
                print('the first player won')
    
            elif   '0' in t:
    
                print('the second player won')
            elif 1 in t:
                if l == 0:
                    print('first')
                else:
                    print('second')
            else:
                print('draw')