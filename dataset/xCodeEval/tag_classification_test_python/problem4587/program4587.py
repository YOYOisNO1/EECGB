def program4587():
    from collections import Counter
    
    if __name__ == '__main__':
        n, k = list(map(int, input().split()))
        q = input()
    
        last_index, first_index = {}, {}
        for i, s in enumerate(q):
            last_index[s] = i
            first_index[s] = min(first_index.get(s, 10**6 +5), i)
    
        opened_count = 0
        for i, d in enumerate(q):
            if i == first_index[d]:
                opened_count += 1
            if opened_count > k:
                print('YES')
                exit(0)
            if i == last_index[d]:
                opened_count -= 1
            
        print('NO')