def read_ints():
        return [int(x) for x in input(' ').split()]
    
    
def compute_prefix(S):
        n = len(S)
        pi = [0]
        for pos in range(1, n):
            l = pi[pos - 1]
            while l > 0 and S[l] != S[pos]:
                l = pi[l - 1]
            if S[pos] == S[l]:
                l += 1
            pi.append(l)
        return pi
    
    
def main():
        S = input()
        pi = compute_prefix(S)
        if pi[-1] >= 1 + (len(S) >> 1):
            print("YES")
            pref = pi[-1]
            print(S[:pref])
        else:
            print("NO")
    
    if __name__ == '__main__':
        main()