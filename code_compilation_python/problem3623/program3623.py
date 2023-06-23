    #!/usr/bin/env python
    # coding: utf-8
    
    # In[204]:
    
    
    # # n = int(input())
    # # line = list(map(int, input().split()))
    # # line = list(str(input()))
    
    
    # In[396]:
    
    
    # 0 43 21 18 2
    # 3 0 21 11 65
    # 5 2 0 1 4
    # 54 62 12 0 99
    # 87 64 81 33 0
    
    
    # In[413]:
    
    
    g_mat = []
    
    for _ in range(5):
        g_mat.append(list(map(int, input().split())))
    
    
    # In[439]:
    
    
def utility_function(states, seq):
        score = (states[seq[0]][seq[1]] + states[seq[1]][seq[0]]              + states[seq[2]][seq[3]] + states[seq[3]][seq[2]])             +(states[seq[1]][seq[2]]+ states[seq[2]][seq[1]]              + states[seq[3]][seq[4]] + states[seq[4]][seq[3]])             + (states[seq[2]][seq[3]] + states[seq[3]][seq[2]])             + (states[seq[3]][seq[4]] + states[seq[4]][seq[3]])
    
        return score 
    
    
    # In[450]:
    
    
def permutation(seq):
    def backtrack(first = 0):
            if first == n:
                if seq[:] not in combs:
                    combs.append(seq[:]) 
                    
            else:
                for i in range(first, n):
                    seq[first], seq[i] = seq[i], seq[first]
                    backtrack(first + 1)
                    seq[first], seq[i] = seq[i], seq[first]
    
        n = len(seq)
        combs = []
        backtrack()
        return combs
    
    
    # In[455]:
    
    
    combs = permutation(seq)
    max_score = 0
    
    for seq in combs:
        max_score = max(max_score, utility_function(g_mat, seq))
    
    print(max_score)
    
    
    # In[ ]:
    
    
    
    