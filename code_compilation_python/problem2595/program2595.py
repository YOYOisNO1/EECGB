def program2595():
    for id in range(1, 51): print(int(((min(id, 25) + id) % (2 + id % 3)) > 0))