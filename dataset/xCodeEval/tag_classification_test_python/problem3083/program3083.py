def program3083():
    n = input()
    path = [x for x in input()]
    for i in range(len(path)-1):
      if path[i]+path[i+1] == 'RU' or path[i]+path[i+1] == 'UR':
        path[i] = 'D'
        path[i+1] = 'D'
        
    zeros = 0
    for x in path:
      if x == 'D':
        zeros += 1
    
    print(len(path)-zeros/2)
    
      