    weights = input()
    weights = weights.split()
    w1 = int(weights[0])
    w2 = int(weights[1])
    
def calculate_years(weight1, weight2):
        years = 0
        while weight1 <= weight2:
            years += 1
            weight1 *= 3
            weight2 *= 2
            
        return years
            
    total = (calculate_years(w1, w2))
    print(total)