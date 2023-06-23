def max_of_min_count(s):
        p = ''
        for i in range(len(s)):
            if s[i] == '?':
                p += 'Y'
            else:
                p += s[i]
        max_min_count = 0
        count = 0
        for j in range(len(p)):
            if p[j] == 'N':
                count += 1
                if count > max_min_count:
                    max_min_count = count
            else:
                count = 0
        return max_min_count
    
def get_res(k, s):
        n_count = 0
        M = len(s)
        for i in range(M):
            if s[i] == 'N':
                n_count += 1
            elif s[i] == 'Y':
                if n_count == k:
                    if max_of_min_count(s) <= k:
                        return True
                n_count = 0
                continue
            else:
                if n_count == k:
                    if max_of_min_count(s) <= k:
                        return True
                elif n_count < k:
                    n_count += 1
                    continue
                else: 
                    n_count = 0
        if n_count == k and max_of_min_count(s) <=k:
            return True
        else:
            return False
                
    M, k = [int(s) for s in input().split(" ")]
    s = str(input())
    res = get_res(k, s)
    for q in range(1, M):
        if s[q] == 'Y' or s[q] == '?':
            res = res or get_res(k, s[q:])
    
    if res and max_of_min_count(s) <= k:
        result = 'YES'
    else:
        result = 'NO'
    
    print "{}".format(result)