    """
    Codeforces
    3A - Shortest path of the king
    http://codeforces.com/problemset/problem/3/A
    
    Héctor González Belver
    ../06/2018
    """
    
    import sys
    import heapq
    
    ORD_A = ord('a')
    
    DIRECTIONS4 = { 'L':(-1, 0), 'D':(0, 1), 'R':(1, 0), 'U':(0, -1) }
    DIRECTIONS8 = dict(DIRECTIONS4) 
    DIRECTIONS8.update({'LD':(-1, 1), 'RD':(1, 1), 'RU':(1, -1), 'LU':(-1, -1) })
    
    class Grid():
    def __init__(self, width, height, allow_diagonals=False):
            self.width = width
            self.height = height
            self.allow_diagonals = allow_diagonals
    
    def neighbors(self, node):
            results = []
            x, y = node
            directions = DIRECTIONS8 if self.allow_diagonals else DIRECTIONS4  
            for k, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    results.append(((nx,ny),k))
            return results 
    
    class PriorityQueue:
    def __init__(self):
            self.heap = []
        
    def empty(self):
            return len(self.heap) == 0
        
    def add(self, item, cost):
            heapq.heappush(self.heap, (cost, item))
        
    def pop(self):
            return heapq.heappop(self.heap)[1]
    
def reconstruct_path(came_from, start, goal):
        current = goal
        path = []
        moves = []
        while current != start:
            path.append(current)
            moves.append(came_from[current][1])
            current = came_from[current][0]
        path.append(start) 
        path.reverse()
    	moves.reverse()
        return path, moves
    
def diagonal_distance_h(goal, node, D, D2):
        #Admissible heuristic if diagonal movements are allowed
        #Compute the number of steps you take if you can’t take a diagonal,
        #then subtract the steps you save by using the diagonal
        #There are min(dx, dy) diagonal steps, and each one costs D2 
        #but saves you 2*D non-diagonal steps.
        dx = abs(goal[0] - node[0])
        dy = abs(goal[1] - node[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy) 
    
def Chebyshev_distance_h(goal, node):
        #It is also known as chessboard distance
        #Diagonal distance when D = 1 and D2 = 1
        return diagonal_distance_h(goal, node, 1, 1)
    
    
def greedy_best_first_search(grid, start, goal, costfn):
        #Explores in promising directions
        #Grid whithout obstacles
        frontier = PriorityQueue()
        frontier.add(start, 0)
        came_from = {}
        came_from[start] = None
        
        while not frontier.empty():
            current = frontier.pop()
            
            if current == goal:
                break
            
            for child, move in grid.neighbors(current):
                if child not in came_from:
                    frontier.add(child, costfn(goal, child))
                    came_from[child] = (current, move)
        
        return came_from
    
def convert_chess_coordinates(coord):
        return (ord(coord[0]) - ORD_A, 8 - int(coord[1]))
    
def main():
        start = convert_chess_coordinates(sys.stdin.readline().strip())
        goal = convert_chess_coordinates(sys.stdin.readline().strip())
    
        chess = Grid(8,8, allow_diagonals=True)
    
        moves = reconstruct_path(greedy_best_first_search(chess,start,goal,Chebyshev_distance_h), start, goal)[1]
    
        sys.stdout.write(str(len(moves)) + '\n')
        sys.stdout.write('\n'.join(moves) + '\n')
    
    if __name__ == '__main__': 
      main()    