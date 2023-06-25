    b, c = map(int, input().split())
    # a = []
    # x = ['B']
    y = []
    # g = ""
    e = input()
    
def swap(s, i, j):
        lst = list(s)
        # print("length of lst ", len(lst))
        if i > len(lst)-1:
            return
        elif i < len(lst)-1:
            lst[i], lst[j] = lst[j], lst[i]
        elif i == len(lst)-1:
            lst = list(s)
        aa = ''.join(lst)
    
        # return ''.join(lst)
        return aa
    
# def callit(e):
    #     for n in range(0,len(y)):
    #         e = swap(e,int(y[n]),int(y[n])+1)
    #     return e
    #
    
    # p = int(0)
    # if len(e) > 0:
    #     for j in e :
    #         if j == 'B':
    #             print(e.index(j)+p)
    #             p = e.index(j)
    #             print("VALUE OF p",p)
    #             e = e[e.index(j):]
    
    for j in range(0,len(e)):
        if e[j] == 'B':
            y.append(j)
    # print(y)
    
    # for n in range(0, len(y)):
    #     e = swap(e, int(y[n]), int(y[n]) + 1)
    
    # print(e)
    
    
    
    count = 0
    
    while (count <c):
        for n in range(0, len(y)):
            e = swap(e, int(y[n]), int(y[n]) + 1)
        e = e
        y.clear()
        Y=[]
        for j in range(0, len(e)):
            if e[j] == 'B':
                y.append(j)
        # print(y)
        count = count + 1
    
    print(e)