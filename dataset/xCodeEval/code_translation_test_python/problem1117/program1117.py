def program1117():
    from itertools import permutations
    l=[]
    for i in range(5):
    	l.append(input().split())
    for i in range(5):
    	for j in range(5):
    		l[i][j]=int(l[i][j])
    max = 0
    for t in list(permutations('01234')):
    	i=[]
    	for j in range(5):
    		i.append(int(t[j]))
    	s = l[i[0]][i[1]]+l[i[1]][i[0]]+l[i[2]][i[3]]+l[i[3]][i[2]]
    	s += l[i[1]][i[2]]+l[i[2]][i[1]]+l[i[3]][i[4]]+l[i[4]][i[3]]
    	s += l[i[2]][i[3]]+l[i[3]][i[2]]+l[i[3]][i[4]]+l[i[4]][i[3]]
    	if s>max:
    		max = s
    print(max)