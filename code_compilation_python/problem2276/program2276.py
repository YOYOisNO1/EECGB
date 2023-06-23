def solvable(s):
        mismatch = False
        for i in range(len(s) // 2):
            if s[i] != s[-1 - i]:
                if mismatch:
                    return False
                mismatch = True
        return mismatch or len(s) % 2 = 1
    
    print ('YES' if solvable(input()) else 'NO')