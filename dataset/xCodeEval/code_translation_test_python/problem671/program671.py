    # https://codeforces.com/problemset/problem/935/A
    
    import math
    
def number_of_divisors(num):
        total_divisors = 0
        for index in xrange(1, num + 1):
            if num % index == 0:
                total_divisors += 1
        return total_divisors
    
    
def main():
        number_of_employees = int(input())
        possible_team_leader_combination = number_of_divisors(number_of_employees) - 1
        print(possible_team_leader_combination)
    
    if __name__ == '__main__':
        main()