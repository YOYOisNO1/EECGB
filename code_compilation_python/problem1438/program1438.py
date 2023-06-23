def program1438():
    s=input()
    count=s.count('VK')
    if('VVV' in s or 'KKK' in s or 'VV' in s):
    	count = count +1
    if(s.index('VV')==s.index('VVK'):
    	count=count-1
    print(count)