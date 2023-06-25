def program438():
    a = input()
    num = [ int(i) for i in a.split()]
    
    num.sort(reverse = True)
    
    if num[0]<num[2]+num[1]:
        print(('TRIANGLE'))
    elif num[1]<num[2]+num[3]:
        print(('TRIANGLE'))
    elif num[0]<num[2]+num[3]:
        print(('TRIANGLE'))
    
    else:
        if num[1]==num[2]+num[3] or num[0]==num[2]+num[3] or num[0]==num[1]+num[2] or num[0]==num[1]+num[3]:
            print(('SEGMENT')) 
        else:
            print('IMPOSSIBLE')
            