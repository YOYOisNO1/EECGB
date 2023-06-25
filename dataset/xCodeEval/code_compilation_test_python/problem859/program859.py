def program859():
    limit = int(input())
    months = map(int, input().split())
    months.sort(reverse = True)
    i = 0
    while limit > 0:
    	limit = limit - months[i]
    	i = i + 1
            if (i == len(months)):
                   print(-1)
                   return
    print(i)