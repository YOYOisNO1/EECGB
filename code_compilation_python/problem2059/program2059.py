    import sys
    
def solve(n, k, groups):
        avail_2 = n*2
        avail_4 = n
    
        for group in groups:
            while group > 0:
                if avail_2 == 0 and avail_4 == 0:
                    return 'NO'
                else:
                    # fill 4s preferentially as 4s
                    if avail_4 > 0 and group >= 3:
                        if group == 3:
                            group = 0
                            avail_4 -= 1
                            group -= 3
                        else:
                            req_4 = group / 4
                            if req_4 >= avail_4:
                                group -= avail_4 * 4
                                avail_4 = 0
                            else:
                                group -= req_4 * 4
                                avail_4 -= req_4
                    # then fill 2s
                    elif avail_2 > 0:
                        req_2 = group / 2 + group % 2
                        if req_2 >= avail_2:
                            group -= avail_2 * 2
                            avail_2 = 0
                        else:
                            group -= req_2 * 2
                            avail_2 -= req_2
                    # finally fill with flex 4s
                    else:
                        # either group = 2 or group = 1
                        if group == 1:
                            group = 0
                            avail_4 -= 1
                            avail_2 += 1
                        elif group == 0:
                            group = 0
                            avail_4 -= 1
    
        return 'YES'
    
    
    if __name__ == '__main__':
        n, k = map(int, sys.stdin.readline().split())
        groups = map(int, sys.stdin.readline().split())
        print solve(n, k, groups)