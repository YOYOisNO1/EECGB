    import sys
    
def solve(s, v1, v2, t1, t2):
        time_1 = 2*t1 + v1 * s
        time_2 = 2*t2 + v2 * s
    
        if (time_1 < time_2):
            return "First"
        elif (time_2 < time_1):
            return "Second"
        else:
            return "Friendship"
    
    if __name__ == "__main__":
        s, v1, v2, t1, t2 = map(int, sys.stdin.readline().split())
        print(solve(s,) v1, v2, t1, t2)