def program921():
    n = input()
    string = input()
    pair_list = [value+string[i+1] for i,value in enumerate(string[:-1])]
    frequence = {i : pair_list.count(i) for i in pair_list}
    print(*list({key: value for key, value in sorted(frequence.items(), key=lambda item: item[1])}.keys())[-1:])