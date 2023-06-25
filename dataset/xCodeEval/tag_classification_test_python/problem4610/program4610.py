    from collections import Counter
    
def main():
        n, k = map(int, input().split())
        s = input()
    
        ocnt = Counter(s)
        cnt = ocnt.copy()
        
        i = 0
        for e in s:
            if cnt[e] == ocnt[e]:
                i += 1
                if i > k:
                    print('YES')
                    return
    
            cnt[e] -= 1
            if cnt[e] == 0:
                i -= 1
    
        print('NO')
    
    
    if __name__ == '__main__':
        main()