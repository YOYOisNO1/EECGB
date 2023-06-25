def program2976():
    stone_num = int(input())
    print stone_num / 3 + (stone_num % 3 != 0 ? 1 : 0)