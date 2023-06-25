def solve_suffix_structures(s, t):
        # check 'need tree'
        cnt_s = [0] * 26
        cnt_t = [0] * 26
        for ch in s: 
            index = ord(ch) - ord('a')
            cnt_s[index] += 1
        for ch in t:
            index = ord(ch) - ord('a')
            cnt_t[index] += 1
        for i in range(26):
            if cnt_s[i] < cnt_t[i]: return "need tree"
        
        # check 'array'
        if len(s) == len(t): return "array"    
        
        # check 'automaton'
        i = 0
        j = 0
        auto = True
        while(j < len(t)):
            if s[i] == t[j]: j += 1
            i += 1
            if i == len(s) and j < len(t):
                auto = False
                break
        if auto: return 'automaton'
        return 'both'
        
    if __name__ == "__main__":
        s = input()
        t = input()
        print(solve_suffix_structures(s, t)) 