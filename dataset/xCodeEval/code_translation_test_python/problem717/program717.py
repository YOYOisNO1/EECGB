def program717():
    """
    by goyal.aman
    https://codeforces.com/problemset/problem/599/A
    
    note:
    patrick can visit first any shop
    """
    
    a,b,c = map(int, input().split())
    """
    a : home -> shop1
    b : home -> shop2
    home c : shop1 - shop2
    """
    
    """
    possible routes:
              home
            /       \
         shop1 ---- shop2
    
    home - shop1 - shop2 - home
    
    home - shop1 - shop2 - shop1 - home
    home - shop2 - shop1 - shop2 - home
    
    home - shop1 - home - shop2 - home <2 ways>
    """
    
    route1 = a + c + b
    route2 = a + c + c + a
    route3 = b  + c + c + b
    route4 = a + a + b + b
    # print("printing routes")
    # print(route1)
    # print(route2)
    # print(route3)
    # print(route4)
    # print("ending routes")
    # print('min', end=' ')
    
    print(min(route1, route2, route3, route4))