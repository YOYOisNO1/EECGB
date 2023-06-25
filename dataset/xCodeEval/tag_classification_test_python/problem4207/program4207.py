def program4207():
    inp = input();
    
    odd = ('1','3','5','7','9');
    vowel = ('a','e','i','o','u');
    
    flip = 0;
    for i in inp:
    	if i in vowel or i in odd:
    		flip = flip+1;
    print(flip);
    				
    