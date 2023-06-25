def program192():
    print('YES') if sum(map(lambda x: 1 if x in ['H', 'Q', '9'] else 0, input())) > 0 else 'NO'