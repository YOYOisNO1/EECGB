def program4262():
    data = [int(i) for i in input().split()]
    data.sort()
    dic = {k:data.count(k) for k in set(data)}
    
    isAlien = True
    legKey = 0
    headAndBody = []
    for key in dic:
        if(dic[key] >= 4):
            legKey = key     
            isAlien = False
    for key in dic:
        if key != legKey:
            headAndBody.append(key)
    
    if(isAlien):
        print("Alien")
    else:
        if(len(headAndBody) == 2):
            if(headAndBody[0] == headAndBody[1]):
                print("Elephant")
            else:
                print( "Bear" )
        else:
            if(len(headAndBody) == 0 or dic[headAndBody[0]] == 2):
                print("Elephant")
            else:
                if(legKey == headAndBody[0]):
                    print("Elephant")
                else:
                    print( "Bear" )
    
    