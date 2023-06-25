    from sys import stdin
    from collections import deque
    
def subsequence(str):
            // iterate over the entire string
        seti  = set()
        for i in range(len(str)):  
                # iterate from the end of the string 
                # to generate substrings 
            for j in range(len(str),-1,-1):
                #(int j = str.length(); j > i; j--) { 
                    sub_str = str[i:j] 
                    st.add(sub_str); 
    
                    # drop kth character in the substring 
                    # and if its not in the set then recur 
                    for k in range(1,len(str)-1):
                        #// drop character from the string 
                        sb = sub_str[0:k] + sub_str[k+1:] 
                        if (!st.contains(sb)) 
                            ; 
                        subsequence(sb.toString()); 
    
    
    n, k = map(int, input().split())
    s = input()
    que = deque()
    que.append(s)
    d = {}
    num = 0
    cost = 0
    while que:
        q = que.popleft()
        if q not in d:
            cost += n - len(q)
            num += 1
            if num == k:
                print(cost)
                exit()
            d[q] = 1
            for j in range(len(q)):
                t = q[:j] + q[j + 1:]
                if t not in d:
                    que.append(t)
    
    print(-1)
                
        
            