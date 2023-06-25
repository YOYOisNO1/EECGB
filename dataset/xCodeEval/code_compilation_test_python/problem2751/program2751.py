def program2751():
    l=input().split(':')
    if l[0] in ['06','07','08','09']:
       print('10:01')
    elif l[0] in ['00','01','02','03','04']:
        i = int(l[1])
        temp = list(l[0])
        temp.reverse()
        st = ''.join(temp)
        j=int(st)
    
        if i<j:
            print(l[0]+':'+st)
        else:
            st2=str(int(l[0])+1)
            temp2 = list(st2)
            temp2.reverse()
            st3 = ''.join(temp2)
            print('0'+st2+':'+st3+'0')
    elif l[0] in ['10','11','12','13','14','20','21','22']:
        i = int(l[1])
        temp = list(l[0])
        temp.reverse()
        st = ''.join(temp)
        j = int(st)
    
        if i < j:
            print(l[0] + ':' + st)
        else:
            st2 = str(int(l[0]) + 1)
            temp2 = list(st2)
            temp2.reverse()
            st3 = ''.join(temp2)
              print( st2 + ':' + st3)
    elif l[0] in ['15']:
        i = int(l[1])
        if i < 51:
            print(l[0] + ':' + '51')
        else:
            print('20:02')
    
    elif l[0] in ['23']:
        i = int(l[1])
        if i < 32:
            print(l[0] + ':' + '32')
        else:
            print('00:00')
    elif l[0] in ['05']:
        i = int(l[1])
        temp = list(l[0])
        temp.reverse()
        st = ''.join(temp)
        j = int(st)
    
        if i < j:
            print(l[0] + ':' + st)
        else:
            print('10:01')
              