def program3090():
    '''
    From the problem statement:
    
    - we know that buying fuel in later cities
    cost much more than earlier cities. Thus we need to refuel as much as
    possible on earlier cities.
    - we know that initially the tank is empty. Thus it is a must to refuel
    on first city.
    - we know that the limit of fuel could be carried on by car limited by
    the capacity of tank. Thus we cannot carry more limit than the capacity
    of tank (v).
    - we know that to move to adjacent city, requires 1 liter of fuel. Thus
    everytime the car move to another city, the fuel would be decreased by 1.
    
    So the strategy we could use to minimize the cost is we refuel as much
    as possible on earlier cities. After we gain enough fuel to go to `n` city
    we could just drive until the tank is empty.
    
    So for example, if we have n=5 & v=2, then we keep refueling the car until
    city 3. Thus minimizing the cost needed to travel to city 5.
    
    Notice that only on city 1 we refuel the tank from 0 to v. In the next
    cities we just need to fill from v-1 to v (since everytime the car move to
    next city it will decrease the tank by 1 liter).
    
    Thus the minimum cost for traveling to city 1 to n with v < n-1 (since we start 
    from index 1) is: 
    
    v (full refuel in city 1) 
    2 (refuel 1 liter in city 2) 
    3 (refuel 1 liter in city 3)
    .
    .
    .
    n-v (refuel 1 liter in city n-v)
    
    This forming formula: v + 2 + ... + (n-v)
    
    Notice that if v is much higher than (n-1), then we just need to
    refuel on city 1, then drive until city n. Which resulted in (n-1) dollar.
    
    In short actually we could think the formula as sliding window in number sequence.
    Whenever the end hasn't reached the last number, the cost would keep accumulating.
    But on city 1 the cost is v. 
    '''
    
    n, v = map(int, input().split())
    print(n-1 if v >= n-1 else v + sum([i for i in range(2, (n-v)+1)]))