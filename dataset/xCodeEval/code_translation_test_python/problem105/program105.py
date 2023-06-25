def program105():
    sum=input()
    colors=sum.split()
    count=dict()
    d=0
    for color in colors:
        count[color]=count.get(color,0)+1
    for i,j in count.items():
        if j>1:
            d=d+j-1
    print(d)