def program2977():
    inpt = input()
    listt = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
    
    counter = 0
    for i in range (5):
        i_count = inpt.count(listt[i])
        counter += i_count
    if (counter == 1):
        print(("YES"))
    else:
        print(("NO"))