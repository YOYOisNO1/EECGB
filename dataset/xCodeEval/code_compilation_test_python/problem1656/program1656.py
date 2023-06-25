    
 def is_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
    
    start_year = int(input())
    if is_leap_year(start_year):
        print(start_year + 28)
    else:
        next_year = start_year + 1
        diff = 1
        if is_leap_year(next_year - 1):
            diff += 1
    
        while diff % 7 != 0:
            diff += 1
            next_year += 1
            if is_leap_year(next_year - 1):
                diff += 1
        print(next_year)