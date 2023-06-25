def program2413():
    import re
    n = input()
    str = input()
    sents = re.findall(r'\(([A-Za-z_]*)\)', str)
    words = 0
    for sent in sents:
    	a=sent.split('_')
    	for i in a:
    		if len(i)>0:
    			words += 1
    print(max([len(i)) for i in re.sub(r'\([A-Za-z_]*\)','_',str).split('_')]), words