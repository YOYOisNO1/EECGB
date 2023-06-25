def program4711():
    n, k = [int(x) for x in input().split()]
    s = input()
    
    all_bad= 'NO'
    alphabet = set(s)
    doors = []
    
    for letter in alphabet:
        doors.append((s.find(letter), s.rfind(letter)))
    
    
    starts = [doors[i][0] for i in range(len(alphabet))]
    stops = [doors[i][1] for i in range(len(alphabet))]
    
    for elem in starts:
        if len([x for x in starts if x < elem]) -  len([x for x in stops if x < elem])>= k:
            all_bad = 'YES'
        
    
    print(all_bad)