def program989():
    #coding:utf-8
    
    n = input()
    m = input()
    lists = m.split(' ')
    for i in range(len(lists)):
        lists[i] = int(lists[i])
    
    while min(lists) != max(lists):
        lists = sorted(lists)
        for i in range(len(lists)):
            for j in range(len(lists)):
                if lists[i] < lists[j]:
                    lists[j] -= lists[j] / lists[i] * lists[i]
                    if lists[j] == 0: lists[j] += lists[i]
    
    print(int(n)) * min(lists)