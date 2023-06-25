def program1792():
    n, k = map(int, input().split(' '))
    hitagi_sequence = map(int, input().split(' '))
    
    kaiki_sequence = map(int, input().split(' '))
    kaiki_sequence.sort()
    kaiki_sequence = kaiki_sequence[::-1]
    
    for i in range(0, n):    
        if(hitagi_sequence[i] == 0):
            hitagi_sequence[i] = kaiki_sequence.pop(0)
            
    arr_is_increasing = []
    for i in range(1, n):
        arr_is_increasing.append(hitagi_sequence[i] > hitagi_sequence[i - 1])
    
    #print(hitagi_sequence)
    #print(arr_is_increasing)
    print('No' if all(arr_is_increasing) else 'Yes')