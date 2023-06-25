def program1818():
    n = int(input()) - 1
    names = {0: 'Sheldon', 1:'Leonard', 2:'Penny', 3:'Rajesh', 4:'Howard'}
    while (n > 4):
        n = (n - 5) / 2 
    print(names.get(n))