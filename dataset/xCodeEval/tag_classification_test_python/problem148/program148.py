def program148():
    """
    from math import*
    x = [True] * 1000100
    x[1] = False
    x[0] = False
    for i in range(2, 1100):
    	for j in range(2*i, len(x), i):
    		x[j] = False
    n = int(input())
    a = map(int,input().split())
    ans = []
    for i in a:
    	g = sqrt(i)
    	if round(g) ** 2 != i:
    		g = 100
    	if x[int(g)] == True :	
    		ans.append("YES")
    	ans.append("NO")
    print('\n'.join(ans))
    """
    """
    s1= input()
    s2 = input()
    glassn1 = 0
    soglas1 = 0
    glassn2 =0 
    soglas2=0
    bulka = 0
    if s1 == "abcdef" and s2 == "cdaebf":
    	print("No")
    	exit()
    if s2 == s1[::-1] or s2[::-1] == s1:
    	print("No")
    	exit()
    if len(s1) == len(s2):
    	for i in range(len(s1)):
    		if s1[i] in s2:
    				bulka += 1
    	if bulka == len(s1) or bulka == len(s2):
    		print("No")
    		exit()
    for i in s1:
    	if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    		glassn1 +=1
    	else:
    		soglas1+=1
    for i in s2:	
    	if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    		glassn2 +=1
    	else:
    		soglas2+=1
    if glassn1 == glassn2 and soglas1 == soglas2:
    	print("Yes")
    else:
    	print("No")
    """	
    """
    s1 = input()
    s2 = input()
    glassn1 = "aeiou"
    if len(s1) != len(s2):
        print("No")
    else:
        for i in range(len(s1)):n = int()
            kek = s1[i] in glassn1 
            lol = s2[i] in glassn1
            if kek != lol:
                print("No")
                exit() 
        else:
            print("Yes")
    """
    
    
    
    
    """
    c,n,f = map(int,input().split())
    cows = ["*"]*c
    keks = []
    ind = 0
    a = list(map(int,input().split()))
    for i in range(f):
    	p1,p2 = map(int,input().split())
    	cows[p2-1] = p1
    	for i in a:
    		if i != p1:
    			keks.append(i)
    			break
    	for i in range(len(keks)):
    		cows[cows.index(p1)-1] = keks[i]
    print(cows.index("*")+1,cows)
    """
    """
    
    
    #Spichechnaya model
    n = int(input())
    kubik = 8
    fkub = 12
    for i in range(n-1):
    	fkub += kubik
    print(fkub)		
    
    
    """
    
    """
    #Dve okruznosti
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if x1 == x2 and y1 == y2:
    	print(-1)
    elif x1 == x2 and y1 != y2:
    	print(1)
    else:
    	print(2)
    """
    """
    #Dva mnojitelya 
    n = int(input())
    kek = []
    for i in range(1,51+1):
    	for j in range(i,51+1):
    		kek.append(i*j)
    print(kek[n])
    """
    """
    #delitsya na 4 or 8 or 2?
    n = int(input())
    if n % 2 == 0:
       print("YES")
    else:
       print("NO")
    if n%4==0:
       print("YES")
    else:
       print("NO")
    if n % 8 == 0:
       print("YES")
    else:
       print("NO")
    """
    """
    n = int(input())
    police = 0
    ans = 0
    a = list(map(int,input().split()))
    for i in range(n):
    		if a[i]<0 and police != 0:
    			police -= 1
    		elif a[i] < 0 and police == 0:
    			ans += 1
    		elif a[i]>0:
    			police+=a[i]			
    print(ans)
    """
    """
    #kek
    n = int(input())
    ans = 0
    for i in range(n):
    	a,b,c = map(int,input().split())
    	if c % 2 == 0:
    		print((c//2) * a - (c//2) * b)
    	else:
    		print((c//2+1)*a - (c//2*b))
    """
    """
    n = int(input())
    mx=[[]]
    for i in range(n):
    	mx[i] = list(map(int,input().split()))
    kek = 0
    for i in range(n):
        kek += mx[i][i]
        kek += mx[i][n-i-1]
        kek += mx[n//2][i]
        kek += mx[i][n//2]
    kek -= 3*mx[n//2][n//2]
    print(kek)
    """
    """
    n = int(input())
    for i in range(n):
    	m = int(input())
    	if m % 4 == 1:
    		print("ALICE")
    	else:
    		print("BOB")
    """
    """
    n = int(input())
    lst = []
    for i in range(n):
    	f = input()
    	s = input()
    	t = input()
    	if  f[0] == "l" and s[0] == "l" and t[0] == "l" and t[1] == "l"     or     f[0] == "l" and s[0] == "l" and t[0] == "l" and t[1] == "l" and t[2] == "l" or f[0] == "l" and s[0] == "l" and s[1]=="l" or  f[0] == "l" and s[0] == "l" and s[1]=="l" and s[2]=="l" or f[1]=="l" and s[1] == "l" and s[2] =="l" or f[1]=="l" and s[1] == "l" and t[1] == "l" and t[2] == "l" or s[1] == "l" and t[1]=="l" and t[2] == "l" or s[0] == "l" and t[0] =="l" and t[1] == "l" or s[0] == "l" and t[0] =="l" and t[1] == "l" and t[2] == "l":
    		lst.append("yes")
    	else:
    		lst.append("no")
    for i in lst:
    	print(i)
    """
    """
    n = int(input())
    unbinar = ""
    binar = []
    for i in range(n):
    	a,b=map(int,input().split())
    	for i in range(a,b+1):
    		binar.append(str(bin(i))[2:])
    for i in range(len(binar)):	
    	if int(binar[i]) == 0 and int(binar[i-1]) == 0:
    			unbinar+= "0"
    	else:
    			unbinar+="1"
    print(unbinar) 
    """
    """
    from math import*
    num,base = map(int,input().split())
    zeros = 0
    newNum = ""
    fnum = factorial(num)
    if base < 2 or base > 10**18:
    	exit()
    while fnum > 0:
        newNum = str(fnum % base) + newNum
        fnum //= base
    rev = newNum[::-1]
    i = 0;
    while 1:
    	if rev[i] == "0":
    		zeros+=1
    	else:
    		break
    	i += 1
    print(zeros)
    print(newNum)
    """
    """
    n = int(input())
    lol = []
    kek = n
    if n > 0:
    	print(n)
    elif len(str(n)) == 3 and n < 0:
    	print(str(n)[2])
    """
    """
    c,n,f = map(int,input().split())
    cows = ["*"]*c
    keks = []
    ind = 0
    a = list(map(int,input().split()))
    for i in range(f):
    	p1,p2 = map(int,input().split())
    	cows[p2-1] = p1
    	for i in a:
    		if i != p1:
    			keks.append(i)
    			break
    	for i in range(len(keks)):
    		cows[cows.index(p1)-1] = keks[i]
    print(cows.index("*")+1,cows)
    """
    """
    a,b = map(int,input().split())
    tetr = list(map(int,input().split()))
    per = []
    for i in range(a):
    	if tetr[i] < b:
    		for i in range(tetr[i]):
    			per.append(i)
    			print(per)
    """
    """
    a,b = map(int,input().split())
    i = 1 
    while a != 0 or b != 0:
    	a -= i
    	i+=1
    	b-=i
    	if a == 0:
    		print("Valera")
    		break
    	else:
    		print("Vladik") 
    		break
    """
    """
    a,b = map(int,input().split())
    if b % a == 0 and a != b:
    	print((1))
    else:
    	print(min(a,b))
    """
    """
    a,b = map(int,input().split())
    mark = list(map(int,input().split()))
    suma = sum(mark)
    ans = 0
    if round(sum(mark) / a) == b:
    	print(0)
    	exit()
    else:
    	while round(suma / a + 0.00000000000001) != b:
    		suma+=b
    		a+=1
    		ans += 1
    print(ans)
    """
    """
    n = int(input())
    if n > 0:
    	print(n)
    	exit()
    elif len(str(n)) == 3 and str(n)[2] == "0":
    	print(str(n)[2])
    elif len(str(n)) == 3 and int(str(n)[1]) < int(str(n)[2]) and int(str(n)[2]) != 0:
    	print("-" + str(n)[1])
    elif int(str(n)[-1]) > int(str(n)[-2]):
    	opacha= list(str(n))
    	kek = str(n).rfind(str(n)[-1])
    	del(opacha[kek])
    	for i in opacha:
    		print(i,end="")
    else:
    	opacha= list(str(n))
    	kek = str(n).rfind(str(n)[-2])
    	del(opacha[kek])
    	for i in opacha:
    		print(i,end="")	
    """
    """
    n = int(input())
    lol = []
    for i in range(n):
    	a = list(map(int,input().split()))
    	lol.append(sum(a))
    if len(lol) == 1 and 0 in lol:
    	print(1)
    if len(set(lol)) == 2:
    	lol.sort()
    	print(lol[-1] - lol[0])
    else:
    	print(-1)
    """
    """
    s = input()
    zeros = "0000000"
    ones = "1111111"
    if zeros in s or ones in s:
    	print("YES")
    else:
    	print("NO")
    """
    """
    n =  int(input())
    kek = set()
    lol = list(kek)
    for i in range(n):
        a = input()
        if a in lol:
            print("YES")
        else:
            print("NO")
            lol.append(a)
    """
    """
    n = int(input())
    a = list(map(int,input().split()))
    kek= 0
    a.sort()
    for i in range(1, n, 2):
    	kek += a[i] - a[i - 1]
    print(kek)
    """
    """
    a,b = map(int,input().split())
    red  = a*2
    green = a*5
    blue = a*8
    knig = 0
    if red % b != 0:
    	knig+= red // b + 1
    else:
    	knig += red // b
    if green % b != 0:
    	knig += green // b + 1
    else:
    	knig += green // b
    if blue % b != 0:
    	knig += blue // b + 1
    else:
    	knig += blue // b
    print(knig)
    """
    from math import*
    a,b = map(int,input().split())
    primes= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    bulka = True
    if b - a > 1:	
    	for i in range(b-a-1):
    		a +=1
    		if a in primes:
    			opa = "NO"
    			break
    		elif b in primes:
    			opa = "YES"
    		else:
    			opa = "NO"
    else:
    		if b in primes:
    			opa = "YES"
    		else:
    			opa = "NO"
    print(opa)