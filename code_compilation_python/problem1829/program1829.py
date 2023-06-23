def program1829():
    n=input()
    first = map(int, list(input()))
    
    count=0
    plus=1
    for x in range(0,len(first)):
        second[x]=(first[x]+plus)%2
        plus=(first[x]+plus)%2
    for y in range(0,len(first)):
        if first[y]!=second[y]:
        count+=1
    print count