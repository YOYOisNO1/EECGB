def program3860():
    tables=[[0,3], [0,4], [1,3], [1,4], [0,0], [0,1], [1,0], [1,1], [0,6], [0,7], [1,6], [1,7], [2,3], [2,4], [3,3], [3,4], [3,0], [3,1], [4,0], [4,1], [3,6], [3,7], [4,6], [4,7], [4,0], [4,1], [5,0], [5,1], [4,6], [4,7], [5,6], [5,7]]
    places=[]
    for i in range(0, 6):
        places.append(list(input()))
    
    for table in tables:
        if (places[table[0]][table[1]] == '.'):
            places[table[0]][table[1]] = 'P'
            break
        
      
    for i in range(0,6):
        print "".join(places[i])