def program1511():
    #import time
    n = int(input())
    #start = time.time()
    some_dict = {0: [0,1,2,3,4]}
    for i in range(1, 5):
        some_dict[i] = list(map(lambda x: x + 5, some_dict[i-1]))
    #print(some_dict)
    count = 1
    elements = 1
    misses =  6
    j = 0
    for i in range(5, 100):
        j += 1
        #print( 'i:', i, 'misses:', misses, 'j:', j)
        if misses == 5 and j == 2:
            some_dict[i] = [0]
            continue
        if misses == 1 and j == 1:
            some_dict[i] = [0]
            continue
        if misses == 5 and j == 7:
            some_dict[i] = list(map(lambda x: x + 5, some_dict[i-1]))
            misses = 1
            j = 0
            continue
        if misses == 6:
            #print('misses: ', i)
            some_dict[i] = [0]
            misses = 1
            j = 1
            continue
        if j == 7:
            #print(i, misses)
            misses += 1
            j = 1
            some_dict[i] = [0]
            continue
        if some_dict[i-1] == [0]:
            if some_dict[i-2] == [0]:
                some_dict[i] = list(map(lambda x: x + 5, some_dict[i-3]))
            else:
                some_dict[i] = list(map(lambda x: x + 5, some_dict[i-2]))
        else:
            some_dict[i] = list(map(lambda x: x + 5, some_dict[i-1]))
        #print(some_dict, misses, j)
    #print(some_dict)
    #end = time.time()
    if some_dict[n] == [0]:
        print(0)
    else:
        print(len(some_dict[n]))
        print(' '.join(list(map(str, some_dict[n]))))