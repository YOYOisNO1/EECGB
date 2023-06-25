def program1424():
    i = input();
    inp = i.split();
    
    odd = ('1','3','5','7','9');
    vowel = ('a','e','i','o','u');
    
    flip = 0;
    for i in range len(inp):
    	if inp[i] in vowel || inp[i] in odd:
    		flip = flip+1;
    print(flip);
    				
    