def program260():
    n=int(input())
    word=input()
    word+='+'
    arr1=['a','e','y','o','i','u']
    for i in range(0,n):
    	if word[i] in arr1:
    		if word[i+1] in arr1:
    			word=word.replace(word[i+1],'')
    print(word.replace(word[len(word)-1],''))