    from collections import Counter
    
    
def main():
        n, k = map(int, input().split())
        queue = input()
    
        counter = Counter()
        unique = list(set(queue))
        amount = dict(zip(unique, [queue.count(x) for x in unique]))
    
        for x in queue:
            counter[x] += 1
    
            if len(counter) > k:
                return 'Yes'
    
            if counter[x] == amount[x]:
                counter.pop(x)
    
        return 'NO'
    
    print(main())