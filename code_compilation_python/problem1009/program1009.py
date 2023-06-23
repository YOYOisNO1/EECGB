def program1009():
    # encoding: utf-8
    
    if __name__ == '__main__':
        n, k = [int(x) for x in input().rstrip().split()]
        
        ans = 0
        pipe = 1
        splitter = range(1, k)
        while (splitter):
            if pipe >= n:
                break
            s = splitter.pop()
            ans += 1
            pipe += s
        
        if pipe >= n:
            print ans
        else:
            print -1