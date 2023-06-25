def program1511():
    n = int(input())
    
    colors = input()
    
    from collections import Counter
    
    c = Counter(colors)
    ans = 'No'
    if c.most_common()[0][1] > 1 or n == 1:
        ans = 'Yes'
    print(ans)