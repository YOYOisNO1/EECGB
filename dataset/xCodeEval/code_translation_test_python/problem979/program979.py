def trip(limit, months):
        months.sort(reverse=True)
        count = 0
        if limit <= 0:
            return 0
        for i in months:
            count += 1
            limit -= i
            if limit <= 0:
                return count
        return -1
    
    print(trip(int(input()),) map(int, input().split()))