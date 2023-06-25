def perform_work():
        line = input().split(" ")
        w = int(line[0])
        m = int(line[1])
        while (m % w == 0):
            m = m / w
        powers = get_powers(w, m)
        return is_possible(w, m, powers)
    
    
def get_powers(base, maximum):
        powers = list()
        current_power = base
        while current_power <= (maximum + 1):
            powers.append(current_power)
            current_power *= base
        return powers
    
def is_possible(base, value, powers):
        if value == 1:
            return True
        for power in powers:
            if (value + 1) % power == 0:
                res = is_possible(base, ((value + 1) / power), powers)
                if res:
                    return True
            if (value - 1) % power == 0:
                res = is_possible(base, ((value - 1) / power), powers)
                if res:
                    return True
        return False
    
    result = perform_work()
    if result:
        print("YES")
    else:
        print("NO")