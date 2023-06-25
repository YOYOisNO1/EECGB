    
    
def solve(a_1, a_2, k_1, k_2, n):
        k_min = min(k_1, k_2)
        a_min = a_1 if k_min == k_1 else a_2
        a_max = a_1 if k_min == k_2 else a_2
        k_max = max(k_1, k_2)
        q_min = min(max(0, n - (a_1 * (k_1 - 1) + a_2 * (k_2 - 1))), a_1 + a_2)
        q_max = min(a_min, n // k_min) + max(0, min(a_max, (n - a_min * k_min) // k_max))
    
        return q_min, q_max
    
    
    if __name__ == "__main__":
        a_1 = int(input())
        a_2 = int(input())
        k_1 = int(input())
        k_2 = int(input())
        n = int(input())
        res = solve(a_1, a_2, k_1, k_2, n)
        print(res[0], res[1])
    