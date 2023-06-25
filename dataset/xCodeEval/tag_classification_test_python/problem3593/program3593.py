def program3593():
    #-*-coding:utf-8-*-
    
    import string
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    
    # B : 남자 G : 여자
    # n 명의 사람
    # 줄에서 남자가 여자보다 앞에 있으면 1초뒤에는 남여의 위치가 뒤바뀜
    
    # 5 1
    # BGGBG
    
    # GBGGB
    
    input_n = input()
    s = input()
    
    n = input_n.split()
    
    #큐에 문자열을 순서대로 저장
    queue = []
    for i in range(int(n[0])) :
    	queue.append(s[i])
    
    #기다린 시간만큼 돌림
    for i in range(int(n[1])):
    	flag = 0	#j+1에서 처리를 했을시, 컨티뉴 처리를 위해서 사용
    	for j in range(int(n[0])-1) :
    		if flag == 1 : 
    			flag = 0
    		elif queue[j] == 'B' and queue[j+1] =='G' : 
    			queue[j] ='G'
    			queue[j+1] = 'B'
    			flag = 1
    		else :
    			queue[j] = queue[j]
    
    #print(를) 사용하면 자동을 엔터가 삽입되기 때문에 한줄로 입력하기 위해 sys 모듈 사용
    for i in range(int(n[0])) :	sys.stdout.write(queue[i])