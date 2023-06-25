    import math
    
    
def non_zero_seg():
        n = int(input())
        alice = [int(x) for x in input().split(' ')]
        bob = [int(x) for x in input().split(' ')]
    
        max_won = min(alice[0], bob[1])
        max_won += min(alice[1], bob[2])
        max_won += min(alice[2], bob[0])
    
        min_won = max(0, alice[0] - bob[2] - bob[0])
        min_won += max(0, alice[1] - bob[0] - bob[1])
        min_won += max(0, alice[2] - bob[1] - bob[2])
    
        print(max(0, min_won), max(0, max_won))
    
    
    if __name__ == "__main__":
        non_zero_seg()