def program1331():
    n = input()
    f = list(map(str, input().split()))
    s = list(map(str, input().split()))
    
    d1 = abs(f.count('1')-s.count('1')
    d2 = abs(f.count('2')-s.count('2')
    d3 = abs(f.count('3')-s.count('3')
    d4 = abs(f.count('4')-s.count('4')
    d5 = abs(f.count('5')-s.count('5')
    
    if d1%2==0 and d2%2==0 and d3%2==0 and d4%2==0 and d5%2==0 :
    	print((d1+d2+d3+d4+d5)//4)
    else :
    	print(-1)