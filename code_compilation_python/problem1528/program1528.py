def program1528():
    
    
    
    
    listwhite = []
    listblack = []
    
    for i in range(1,9):
    
       if i%2 == 0:
           k = 2
       else:
           k = 1
    
       for j in range(k,9,2):
           listwhite.append([i,j])
    
    for i in range(1,9):
    
        if i%2 == 0:
            k = 1
        else:
            k = 2
    
        for j in range(k,9,2):
            listblack.append([i,j])
    
    
    # print(listwhite)
    # print(listblack)
    x1,y1,x2,y2 = map(int,input().split())
    
    
    if x1 == x2 and y1!=y2:
        rook = 1
    
    
    elif y1 == y2 and x1!=x2:
        rook = 1
    
    
    elif x1 != x2 and y1!=y2:
        rook = 2
    else:
        rook = 0
    
    
    
    if [x1,y1] in listwhite and [x2,y2] in listwhite:
    
        if abs(x1 - x2) == abs(y1 - y2):
            bishop = 1
    
        else:
            bishop = 2
    
    
    elif [x1,y1] in listblack and [x2,y2] in listblack:
    
        if abs(x1 - x2) == abs(y1 - y2):
            bishop = 1
    
        else:
            bishop = 2
    
    else:
        bishop = 0
    
    if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
        count = 1
    
    else:
      count = 0
      if x1!=x2 and y1!=y2:
        if x1 >=x2 and y1 >=y2:
            count1 = 0
            count2 = 0
            while y1 != y2:
                count1+=1
                y1-=1
                x1-=1
            count1+=abs(x1-x2)
    
            while x1 != x2:
                count2+=1
                y1-=1
                x1-=1
            count2+=abs(y1-y2)
    
            count = min(count1,count2)
    
    
        elif x1 <=x2 and y1 >=y2:
    
            count1 = 0
            count2 = 0
            temp1,temp2,temp3,temp4 = x1,x2,y1,y2
            while y1 != y2:
                count1+=1
                y1-=1
                x1+=1
            count1+=abs(x1-x2)
    
            x1,x2,y1,y2 = temp1,temp2,temp3,temp4
            while x1 != x2:
                count2+=1
                y1-=1
                x1+=1
            count2+=abs(y1-y2)
    
            count = min(count1,count2)
    
        elif x1 <=x2 and y1 <=y2:
    
            count1 = 0
            count2 = 0
            temp1,temp2,temp3,temp4 = x1,x2,y1,y2
            while y1 != y2:
                count1+=1
                y1+=1
                x1+=1
            count1+=abs(x1-x2)
            x1,x2,y1,y2 = temp1,temp2,temp3,temp4
            while x1 != x2:
                count2+=1
                y1+=1
                x1+=1
            count2+=abs(y1-y2)
    
            count = min(count1,count2)
        elif x1 >=x2 and y1 <=y2:
    
            count1 = 0
            count2 = 0
            temp1,temp2,temp3,temp4 = x1,x2,y1,y2
            while y1 != y2:
                count1+=1
                y1-=1
                x1+=1
            count1+=abs(x1-x2)
            x1,x2,y1,y2 = temp1,temp2,temp3,temp4
    
            while x1 != x2:
                count2+=1
                y1+=1
                x1-=1
            count2+=abs(y1-y2)
    
            count = min(count1,count2)
    
      else:
          count+=abs(y1-y2) + abs(x2-x1)
    
    
    print(rook,bishop,count)
    
    
    
    
    