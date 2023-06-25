def program2888():
    pokemon = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    
    length = int(input())
    unknown_name = input()
    
    for current_pokemon in pokemon:
        if len(current_pokemon) != length:
            continue
    
        for i, c in enumerate(unknown_name):
            if c == '.':
                continue
    
            if current_pokemon[i] != c:
                break
        else:
            print(current_pokemon)