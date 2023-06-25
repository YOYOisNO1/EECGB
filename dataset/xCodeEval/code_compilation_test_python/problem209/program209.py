def program209():
    alpha=['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
    ind=13
    word=input()
    count=0
    summ=0
    while(count<len(word)):
    
        if(abs(ind-alpha.index(word[count]))>(26-ind+alpha.index(word[count]))):
            summ+=(26-ind+alpha.index(word[count]))
        else:
            if(ind==0):
                summ+=26-alpha.index(word[count])
            else:
                summ+=abs(ind-alpha.index(word[count])) 
        ind=alpha.index(word[count])
        count+=1
    print(summ)
       