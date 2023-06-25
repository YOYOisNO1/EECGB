def program113():
    string = input()
    vowels = ['A', 'E', 'I', 'O', 'U']
    mini = 1
    count = 0
    for i in string:
        if i not in vowels:
                count += 1
        else:
            mini = max(mini, count+1)
            count = 0
    if count != 0:
        mini = max(mini, count+1)
    print mini