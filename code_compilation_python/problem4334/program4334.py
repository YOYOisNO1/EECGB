def program4334():
    
    a, b, x_1, y_1, x_2, y_2 = map(int, input().split())
    
    print(max([abs((x_2 + y_2) - (x_1 + y_1)) // (2 * a),
               abs((x_2 - y_2) - (x_1 - y_2)) // (2 * b)]))
    