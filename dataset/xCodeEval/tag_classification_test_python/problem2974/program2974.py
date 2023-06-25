def program2974():
    s = input()
    
    a = ['Danil', 'Olya', 'Slava', 'Ann','Nikita']
    
    k = 0
    for i in a:
        k += s.count(i)
    if k == 1:
        print("YES")
    else:
        print("NO")