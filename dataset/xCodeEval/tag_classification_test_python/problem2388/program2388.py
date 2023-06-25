def program2388():
    a=str(input())
    q=a.count('VK')
    
    w=a.count('KK')-a.count('VKK')+a.count('VV')-a.count('VVK')+a.count("VVV")+a.count('KKK')
    if w>0:
        print(q+1)
    else:print(q)