    from itertools import combinations
    
    
def main():
        n = int(input())
        inputs = list(input().split())
        inputs = [int(x) for x in inputs]
        combos = list(combinations(inputs,3))
        for combo in combos:
            if istriangle(combo):
                print("yes")
                return
        print("NO")
    
    
def istriangle(sides):
        if (sides[1]+sides[2]) > sides[0] and (sides[0]+sides[2])>sides[1] and (sides[0]+sides[1])>sides[2]:
            return True
        else:
            return False
    
    main()