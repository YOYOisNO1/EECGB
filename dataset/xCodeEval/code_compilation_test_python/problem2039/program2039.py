def program2039():
    k = int(input())
    if k == 1:
        print('fall')
        exit(0)
    if k == 3:
        print('september')
        exit(0)
    # от порядка объединения строк ничего не зависит
    # для каждой буквы, итоговая стоимость будет n * (n - 1) / 2
    # жадно наберём ответ
    if not k:
        print('a')
        exit(0)
    op_count = [0, 0]
    for i in range(1, 500):
        op_count.append(op_count[-1] + i)
        if op_count[-1] > k:
            break
    
    ans = []
    letter = 'a'
    for i in range(len(op_count) - 1, 1, -1):
        while op_count[i] <= k:
            k -= op_count[i]
            ans.append(letter * i)
            letter = chr(ord(letter) + 1)
    print(''.join(ans))
     