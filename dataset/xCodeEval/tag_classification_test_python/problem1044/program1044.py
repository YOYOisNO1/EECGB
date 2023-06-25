    
    import sys
    input = sys.stdin.readline
    
    '''
        Just paste this template at the beginning of your Code.
         It comprises of 4 functions :-
        1) inp — For taking integer inputs.
        2) inlt — For taking List inputs.
        3) insr — For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
        4) invr — For taking space seperated integer variable inputs.
    '''
    ############ ---- Input Functions ---- ############
def inp():
        return(int(input()))
def inlt():
        return(list(map(int,input().split())))
def insr():
        s = input()
        return(list(s[:len(s) - 1]))
def invr():
        return(map(int,input().split()))
    
    
    ###############################################
    
    cap = [[0] * 8 for i in range(8)];
    visited = [False] * 8;
    
def find_path(u, vol):
        if u == 7: return vol;
        if visited[u]: return 0;
        visited[u] = True;
        for i in range(8):
            if cap[u][i] > 0:
                curt = find_path(i, min(vol, cap[u][i]));
                if curt > 0:
                    cap[u][i] -= curt;
                    cap[i][u] += curt;
                    return curt;
        return 0;
    
    n = inp();
    a1, a2, a3 = invr();
    b1, b2, b3 = invr();    
    max_win = min(a1, b2) + min(a2, b3) + min(a3, b1);
    
    cap[0][1] = a1;
    cap[0][2] = a2;
    cap[0][3] = a3;
    cap[4][7] = b1;
    cap[5][7] = b2;
    cap[6][7] = b3;
    cap[1][4] = cap[1][6] = cap[2][4] = cap[2][5] = cap[3][5] = cap[3][6] = n;
    
    flow = 0;
    while True:
        visited = [False] * 8;
        curt_flow = find_path(0, n);
        #print(('curt_flow) = ', curt_flow);
        if curt_flow == 0: break;
        flow += curt_flow;
        
    
    #print(('flow) =', flow);
    min_win = n - flow;
    print(min_win, max_win);