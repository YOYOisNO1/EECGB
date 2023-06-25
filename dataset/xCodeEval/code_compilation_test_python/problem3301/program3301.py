def program3301():
    input()
    
    horiz = input()
    vert = input()
    
    num_horiz = len(horiz)
    num_vert = len(vert)
    
    num_junc = num_horiz * num_vert
    
    grid = [[0 for j in range(num_junc) ] for i in range(num_junc)]
    
    for i in range(num_horiz):
        for j in range(num_vert):
            
            p = i * num_vert + j
    
            if horiz[i] == '>' and j + 1 < num_vert:   
                grid[p][p + 1] = 1
            elif horiz[i] == '<' and j - 1 >= 0:
                grid[p][p - 1] = 1
                
            if vert[j] == 'v' and i + 1 < num_horiz:
                grid[p][p + num_vert] = 1
            elif vert[j] == '^' and i - 1 >= 0:
                grid[p][p - num_vert] = 1
    
    cached_visits = [[] for x in range(num_junc)]
    
    good_city = True
    
    for idx, adj_nodes in enumerate(grid):
        visited = [0 for x in range(num_junc)]
        visited[idx] = 1
        
        s = [idx for idx, val in enumerate(adj_nodes) if val ]  
                
        while s:
            node_idx = s.pop()
            visited[node_idx] = 1
            new_possible_nodes = [idx for idx, val in enumerate(grid[node_idx]) if val and not visited[idx]]  
    #         print(new_possible_nodes)
            s += new_possible_nodes
            
        if visited.count(0):
    #         print(visited)
            good_city = False
            break
    
    print('YES' if good_city else 'NO')
            
    
    
    