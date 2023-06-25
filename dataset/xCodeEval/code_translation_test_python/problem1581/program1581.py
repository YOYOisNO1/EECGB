def check(s, num):
        if len(s) != len(num):
            return False
        x = -1
        for j in range(len(s)):
            if s[j] == '_':
                continue
            if s[j] == 'X':
                if x == -1:
                    x = num[j]
                    continue
                else:
                    if x != num[j]:
                        return False
                    else:
                        continue
            if s[j] != num[j]:
                return False
        return True
    
    
    if __name__ == '__main__':
        s = str(input())
        tot = 0
        for i in range(0, 10**8, 25):
            i = str(i)
            if len(i) > len(s):
                break
            if check(str(s), i):
                tot += 1
        print(tot)