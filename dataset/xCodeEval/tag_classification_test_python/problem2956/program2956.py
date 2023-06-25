def program2956():
    word=input()
    if(ord(word[0])>=96):
        count=0
        for i in range(1,len(word)):
            if(ord(word[i])>=65 and ord(word[i])<=90):
                count+=1
        if(count==(len(word)-1)):
            word=word.lower()
            print(chr(ord(word[0])-32)+word[1:])
        else:
            print(word)
    else:
        count=0
        for i in range(0,len(word)):
            if(ord(word[i])>=65 and ord(word[i])<=90):
                count+=1
        if(count==len(word)):
            word=word.lower()
            print(word)
        else:
            print(word)