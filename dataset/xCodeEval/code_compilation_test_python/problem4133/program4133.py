def program4133():
    from enum import Enum
    from queue import Queue
    from collections import deque
    
    class  Dir(Enum):
        N = 1
        E = 2
        S = 3
        W = 4
        NE = 5
        SE = 6
        SW = 7
        NW = 8
    
    
    if __name__ == "__main__":
    
        dirdict = {
                    Dir.N : (Dir.NE, Dir.NW),
                    Dir.S : (Dir.SE, Dir.SW),
                    Dir.W : (Dir.SW, Dir.NW),
                    Dir.E: (Dir.NE, Dir.SE),
                    Dir.NE : (Dir.N, Dir.E),
                    Dir.SE : (Dir.E, Dir.S),
                    Dir.SW : (Dir.S, Dir.W),
                    Dir.NW: (Dir.N, Dir.W)}
    
    
    
        n=int(input().strip())
        lst = list(map(int, input().strip().split()))
    
        result=[[False for _ in range(400)]  for _ in range(400)]
        q=deque()
        a=((200,200), Dir.N,0)
        q.append(a)
       
        while len(q) > 0:
            position,direction,stage=q.pop()
            if stage == len(lst):
                continue
            else:
                (x,y) = position
                if direction == Dir.N:
                    for j in range(1,lst[stage]+1):
                        result[x][y+j] = True
                    q.append(((x, y+j), Dir.NE, stage+1))
                    q.append(((x, y+j), Dir.NW, stage+1))
                elif direction == Dir.S:
                    for j in range(1,lst[stage]+1):
                        result[x][y-j] =True
                    q.append(((x, y-j), Dir.SE, stage+1))
                    q.append(((x, y-j), Dir.SW, stage+1))
                elif direction == Dir.E:
                    for j in range(1,lst[stage]+1):
                        result[x+j][y] = True
                    q.append(((x+j, y), Dir.NE, stage+1))
                    q.append(((x+j, y), Dir.SE, stage+1))
                elif direction == Dir.W:
                    for j in range(1,lst[stage]+1):
                        result[x-j][ y] = True
                    q.append(((x-j, y), Dir.NW, stage+1))
                    q.append(((x-j, y), Dir.SW, stage+1))
                elif direction == Dir.NE:
                    for j in range(1,lst[stage]+1):
                        result[x+j][y+j] = True
                    q.append(((x+j, y+j), Dir.N, stage+1))
                    q.append(((x+j, y+j), Dir.E, stage+1))
                elif direction == Dir.NW:
                    for j in range(1,lst[stage]+1):
                        result[x-j][y+j] = True
                    q.append(((x-j, y+j), Dir.N, stage+1))
                    q.append(((x-j, y+j), Dir.W, stage+1))
                elif direction == Dir.SE:
                    for j in range(1,lst[stage]+1):
                        result[x+j][y-j] = True
                    q.append(((x+j, y-j), Dir.E, stage+1))
                    q.append(((x+j, y-j), Dir.S, stage+1))
                elif direction == Dir.SW:
                    for j in range(1,lst[stage]+1):
                        result[x-j][y-j] = True
                    q.append(((x-j, y-j), Dir.S, stage+1))
                    q.append(((x-j, y-j), Dir.W, stage+1))
    
        print(sum(map (sum, result)))
        #print(sorted(list(result)))