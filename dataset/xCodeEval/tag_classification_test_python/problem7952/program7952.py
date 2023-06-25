    '''
    Created on 12.05.2012
    
    @author: matt
    '''
    import Queue
    
    
    
def solve():
        try: input = input
        except: pass
        N = int(input())
        friends = {}
        dislikes = {}
        for i in range(N):
            friends[i] = set()
            dislikes[i] = set()
            
        # friends
        k = int(input())
        for i in range(k):
            s = input().split()
            i, j = list(map(int, s))
            friends[i-1].add(j-1)
            friends[j-1].add(i-1)
        m = int(input())
        for i in range(m):
            s = input().split()
            i, j = list(map(int, s))
            dislikes[i-1].add(j-1)
            dislikes[j-1].add(i-1)
      
        # find ppl
        grouppp = [-1 for _ in range(N)]
        groups = {}
        groupids = iter(xrange(0, N))
        for i in xrange(N):
            if grouppp[i] == -1:
                curgroup = next(groupids)
                grouppp[i] = curgroup
                groups[curgroup] = set()
                groups[curgroup].add(i)
                tagfriends(i, curgroup, friends, groups, grouppp)
        c = sorted([(len(y), y) for x, y in groups.items()], reverse=True)
        for size, members in c:
            if not has_dislikes(members, dislikes):
                return size
        return 0
    
def readmap(res, n):
        for i in range(n):
            s = input().split()
            i, j = list(map(int, s))
            res[i-1].add(j-1)
            res[j-1].add(i-1)
        return res
       
def has_dislikes(members, dislikes):
        for m1 in members:
            for dislike in dislikes[m1]:
                if dislike in members:
                    return True
        return False
    
def tagfriends(i, curgroup, friends, groups, grouppp):
        for f in friends[i]:
            if grouppp[f] != curgroup:
                grouppp[f] = curgroup
                groups[curgroup].add(f)
                tagfriends(f, curgroup, friends, groups, grouppp)
    
        
    print(solve())