def num_grass(row):
        return row[0] + row[1]
    
    
    num_tests = int(input())
    for test_num in range(num_tests):
        row1 = list(map(int, input().split()))
        row2 = list(map(int, input().split()))
        if num_grass(row1) + num_grass(row2) == 0:
            print(0)
        elif num_grass(row1) + num_grass(row2) == 4:
            print(2)
        else:
            print(1)