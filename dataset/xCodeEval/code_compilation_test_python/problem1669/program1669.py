    from collections import Counter
    
    rep = input("Res: ")
    a = Counter({'B':0, 'S':0, 'C':0})
    a.update(rep)
    rep = a['B'], a['S'], a['C']
    
    inventory = Bi, Si, Ci = list(map(int, input("Invent: ").split(' ')))
    
    price = list(map(int, input("Prices: ").split(' ')))
    
    money = int(input("Money: "))
    
    output =
    
    
def make_sandwich():
        global output
        for idx in range(len(inventory)):
            inventory[idx] -= rep[idx]
        output += 1
    
    
    while money or all([invent >= ingredient for ingredient, invent in zip(rep, inventory)]):
        if all([inventory[idx] >= rep[idx] for idx in range(len(inventory))]):
            make_sandwich()
    
        for ingredient in range(len(inventory)):
            if inventory[ingredient] < rep[ingredient] and money >= price[ingredient]:
                inventory[ingredient] += 1
                money -= price[ingredient]
                break
    
    
    
    
    print(output)