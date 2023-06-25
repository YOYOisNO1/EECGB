    '''
    Find the number of islands |(Using DFS)
    Given a boolean 2D matrix, find the number
    of islands. A group of connected 1s forms
    an island. for example, the below matrix
    contains 5 islands.
    
    Example:-
    
    Input : mat[][] = {{1, 1, 0, 0, 0},
                       {0, 1, 0, 0, 1},
                       {1, 0, 0, 1, 1},
                       {0, 0, 0, 0, 0},
                       {1, 0, 1, 0, 1}
    Output : 5
    
    A cell in a 2d matrix can be connected
    to 8 neighbours. So, unlike standard
    DFS(), where we recursivelly call
    for all adjacent vertices, here we can
    recursivelly call for 8 neighbours only.
    We keep track of the visited 1s so that
    they are not visited again.
    '''
    
    class Graph:
    
    def __init__(self,row,col,g):
            self.ROW = row
            self.COL = col
            self.graph = g
    
        # A function to check if a given
        # cell (row,col) can be included in
        # DFS
    def isSafe(self,i,j,visited):
            # row number is in range, col num
            # is in range and value is 1 and not
            # yet visited
            return (i >= 0 and i < self.ROW and\
                    j>=0 and j<self.COL and \
                    not visited[i][j] and self.graph[i][j])
    
        # A utility function to do DFS
        # for a 2D boolean matrix. it only
        # considers the 8 neighbours as adjacent
        # vertices.
    def DFS(self,i,j,visited):
            rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
            colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
    
            visited[i][j]=True
    
            for k in range(8):
                if self.isSafe(i+rowNbr[k],j+colNbr[k],visited):
                    self.DFS(i+rowNbr[k],j+colNbr[k],visited)
    
    def countIslands(self):
            visited =[[False for j in range(self.COL)] for i in range(self.ROW)]
    
            count = 0
            for i in range(self.ROW):
                for j in range(self.COL):
    
                    if visited[i][j]==False and self.graph[i][j]==1:
                        self.DFS(i,j,visited)
                        count+=1
            return count
    graph = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
    
    row = len(graph)
    col = len(graph[0])
    
    g = Graph(row, col, graph)
    
    print "Number of islands is:"
    print g.countIslands()