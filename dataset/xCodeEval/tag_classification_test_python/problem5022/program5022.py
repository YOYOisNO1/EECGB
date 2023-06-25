def program5022():
    # three players princess, dragon, chance
    # there are only 2 possible winners
    # use 3d array dp[w][b][p] to store the prob of having w, b mice left to the player p
    # interesting, how do we even implement this?, without recursive?
    
    # (w + b) - (wleft + bleft) mod 3 will tell us the player
    # 0 being princess, 1 being dragon, 2 being chance
    # so we can just loop through the array, without even worrying for the player at first
    
    # all the 'special cases' treatment, is giving me headache. is there a way to nicely sort them out without special cases ?
    
    MAX = 1002
    w, b = map(int, input().split())
    ans = 0
    dp = [[0 for _ in range(MAX)] for _ in range(MAX)]
    end = [[0 for _ in range(MAX)] for _ in range(MAX)]
    dp[w][b] = 1
    for i in range (w, -1, -1):
        end[i][b+1] = 1    
    if w > 0:
        ans += ((w) / (w + b)) * dp[w][b]
        end[w-1][b] = 1
    if b > 0:
        for j in range(b - 1, -1, -1):
            dp[w][j] = ((j + 1) / (w + j + 1)) * dp[w][j+1]
    
    for i in range(w - 1, -1, -1):
        for j in range(b - 1, -1, -1):
            if end[i+1][j] and end[i][j+1]:
                end[i][j] = 1
            else:
                if not end[i+1][j]:
                    if (w + b - i -j) % 3 == 1:
                        ans += ((i + 1) / (i + j + 1)) * dp[i+1][j]
                        if end[i][j+1]:
                            end[i][j] = 1
                    elif (w + b - i -j) % 3 == 2:
                        if end[i][j+1]:
                            end[i][j] = 1
                    else:
                        dp[i][j] += ((i + 1) / (i + j + 1)) * dp[i+1][j]
                if not end[i][j+1]: 
                    dp[i][j] += ((j + 1) / (i + j + 1)) * dp[i][j+1]
            
                
    print(ans)