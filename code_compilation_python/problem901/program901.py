    from collections import Counter
    
def locationForDup(diff):
        if(diff == 0): return None
        x = 12 - ((diff) / 2)
        y = 0
        return (x, y)
    
def printArr(array):
        for a in array:
            print "".join(map(str,a))
        print
    
def flowCategory(diff):
        # 0 => prev = below
        # 1 => prev = diagonal
        return diff % 2
    
def printArr1(x):
        pass
        # printArr(x)
    
def fill(xs, arrays, diff, start, stop, dup):
        if(start > 13):
            return fill(list(reversed(xs)), arrays, diff, 27 - stop, 27 - start, dup)
        (lx, ly) = locationForDup(diff)
        # print(xs)
        # print(start)
        # print(dup)
        # print(diff)
        f = flowCategory(diff)
        if(start >= 0):
            totalTrip = 0
            if(f == 0):
                mx, my = (lx, 1)
            else:
                mx, my = (lx - 1, 1)
            arrays[ly][lx] = dup
            r1 = reversed(xs[:start])
            for i, c in enumerate(r1):
                totalTrip += 1
                x = mx - i
                y = 1
                assert(type(arrays[y][x]) is int)
                if(x >= 0):
                    arrays[y][x] = c
                else:
                    __s = i if vars().get("__s") is None else vars()["__s"]
                    x = i - __s
                    y = 0
                    arrays[y][x] = c
            r2 = (xs[start + 1:])
            printArr1(arrays)
            for i, c in enumerate(r2):
                totalTrip += 1
                x = lx + i + 1
                y = 0
                if(x > 12): break
                assert(type(arrays[y][x]) is int)
                arrays[y][x] = c
            printArr1(arrays)
            b = i
            for i, c in enumerate(xs[start + b + 1:]):
                totalTrip += 1
                x = 12 - i
                y = 1
                if(type(arrays[y][x]) is not int): break
                if(c == dup): break
                assert(type(arrays[y][x]) is int)
                arrays[y][x] = c
            printArr1(arrays)
            for i, c in enumerate(xs[stop:]):
                totalTrip += 1
                x = lx - i - 1
                y = 0
                assert(type(arrays[y][x]) is int)
                arrays[y][x] = c
                if(x == 0): break
            for i, c in enumerate(xs[totalTrip:]):
                x = i
                y = 1
                assert(type(arrays[y][x]) is int)
                arrays[y][x] = c
        else:
            pass
    
    
def main():
        xs = input()
        counter = Counter(xs)
        dup = [c for c in counter.keys() if counter[c] > 1][0]
        start = xs.find(dup)
        stop = len(xs) - "".join(list(reversed(xs))).find(dup)
        diff = stop - start - 2
        arrays = [[x % 10 for x in xrange(13)] for _ in xrange(2)]
        if(locationForDup(diff) is None):
            print("Impossible")
        else:
            fill(xs, arrays, diff, start, stop, dup)
            printArr(arrays)
    main()