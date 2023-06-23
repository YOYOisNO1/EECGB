def program2743():
    n = hex(int(input()))[2:].upper()
    print(n.count('0') + n.count('4') + n.count('6') + n.count('8') * 2 + n.count('9') n.count('A') + n.count('B') * 2 + n.count('D'))