    import os,sys
    ####Inna and Pink Pony: 374A http://codeforces.com/problemset/problem/374/A
    
    ###Dima and Inna are doing so great! At the moment, Inna is sitting on the magic lawn playing with a pink pony. Dima wanted to play too. He brought an n*m chessboard, a very tasty candy and two numbers a and b.
    ###Dima put the chessboard in front of Inna and placed the candy in position (i,j) on the board. The boy said he would give the candy if it reaches one of the corner cells of the board. He's got one more condition. There can only be actions of the following types:
    ###move the candy from position (x,y) on the board to position (x-a,y-b);
    ###move the candy from position (x,y) on the board to position (x-a,y+b);
    ###move the candy from position (x,y) on the board to position (x+a,y-b);
    ###move the candy from position (x,y) on the board to position (x+a,y+b);
    
    ###Naturally, Dima doesn't allow to move the candy beyond the chessboard borders.
    ###nna and the pony started shifting the candy around the board. They wonder what is the minimum number of allowed actions that they need to perform to move the candy from the initial position (i,j) to one of the chessboard corners. Help them cope with the task!
    
    ###input 
    ###The first line of the input contains six integers n,m,i,j,a,b
    ###You can assume that the chessboard rows are numbered from 1 to n from top to bottom and the columns are numbered from 1 to m from left to right.
    ###The corner are (1,m), (n,1), (n,m), (1,1)
    
    ###output
    ###In a single line print a single integer  -- the minimum number of moves needed to get the candy.
    ###If Inna and the pony cannot get the candy playing by Dima's rules, print on a single line "Poor Inna and pony!" without the quotes.
    
    
    ###solve: bfs
def run():
        n, m, i, j, a, b = map(int, input().split())
    
        visited = {}
        corners = [(1,m), (n,1), (n,m), (1,1)]
        depths = list()
        que = list()
    
        que.append((i,j))
        depths.append(0)
        visited[(i,j)] = True
        ###bfs
        while len(que) > 0:
            curPos = que.pop(0)
            curDpth = depths.pop(0)
            if curPos in corners:
                print curDpth
                return
            x = curPos[0]
            y = curPos[1]
            for pos in [(x-a,y-b), (x+a,y-b), (x-a,y+b), (x+a,y+b)]:
                if pos[0]<1 or pos[1]<1 or pos[0]>n or pos[1]>m:
                    continue
                if pos in visited:
                    continue
                visited[pos] = True
                que.append(pos)
                depths.append(curDpth+1)
        print "Poor Inna and pony!"
        return
    ################################################################################
    run()