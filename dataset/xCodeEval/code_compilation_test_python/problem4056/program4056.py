    from collections import defaultdict
    
    n,q = map(int, input().split())
    
    ops = []
    for i in range(0,q):
        a,b = input().split()
        ops.append((b,a))
    ops.sort(key=lambda tup: (tup[0],tup[1]))
    ops_d = defaultdict(list)
    for k,v in ops:
        ops_d[k].append(v)
    
    count = 0
    hit_list = []
def dfs(cur_str, size):
        size +=1
        #print(cur_str, " ", size)
        if len(cur_str) == n and cur_str not in hit_list:
            hit_list.append(cur_str)
            return 1
        elif size > n:
            return -1
        else:
            for op in ops_d[cur_str[0]]:
                #print(op)
                cur_str_tmp = list(cur_str)
                cur_str_tmp[0] = op
                cur_str_tmp = "".join(cur_str_tmp)
                if dfs(cur_str_tmp,size) == 1:
                    global count
                    count +=1
                   
    
    dfs('a',0)
    print(count)