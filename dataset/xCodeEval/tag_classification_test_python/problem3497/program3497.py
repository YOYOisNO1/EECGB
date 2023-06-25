def program3497():
    #coding=utf-8
    
    n = int(input())
    
    ll = map(int, input().split())
    
    mini = min(ll)
    maxi = max(ll)
    
    ll.remove(maxi)
    ll.remove(mini)
    ll.sort()
    
    print(' ').join(map(str, [maxi] + ll + [mini]))