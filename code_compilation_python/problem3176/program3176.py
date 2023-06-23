def program3176():
    n, k, M = map(int, input().split())
    
    times = sorted(list(map(int, input().split())))
    for_task = sum(times)
    
    
    
    result = 0
    fully_solved = 0
    while fully_solved * for_task <= M:
        curr_result = fully_solved * (k + 1)
        time_rest = M - fully_solved * for_task
        for t in times:
            if t * n > time_rest:
                l = 0
                r = n + 1
                while r - l != 1:
                    mid = (l + r) / 2
                    if t * mid > time_rest:
                        r = mid
                    else:
                        l = mid
                curr_result += l
                break
            else:
                time_rest -= t * n
                curr_result += n
    
        result = max(curr_result, result)
        fully_solved += 1
        n -= 1
    
    print result