    
    from collections import defaultdict
    
def calculate2(m, sa, sb, ia, ib):
        if ib >= len(sb):
            return 0
        if len(sb) - ib > len(sa) - ia:
            return -1
        result = 0
        found = False
        for i in xrange(ia, len(sa)):
            if sa[i] == sb[ib]:
                recur = calculate2(m, sa, sb, i+1, ib+1)
                if recur < 0:
                    continue
                found = True
                result = max(result, recur, i - ia)
                if ib == len(sb) - 1:
                    result = max(result, len(sa) - 1 - i)
        if found:
            return result
        return -1
    
    # Find the smallest index in array that is at least ia
    # this is guaranteed to return something per problem statement
def search(array, start, end, ia):
        if start >= end:
            return -1
        mid = (start + end) / 2
        if array[mid] == ia:
            return mid
        if array[mid] < ia:
            return search(array, mid + 1, end, ia)
        recur = search(array, start, mid, ia)
        if recur < 0:
            return mid
        return recur
    
def calculate23(m, sa, sb, ia, ib):
        if ib >= len(sb):
            return 0
        if len(sb) - ib > len(sa) - ia:
            return -1
        result = 0
        c = sb[ib]
        array = m[c]
        start = search(array, 0, len(array), ia)
        for index in xrange(start, len(array)):
            i = array[index]
            recur = calculate2(m, sa, sb, i+1, ib+1)
            if recur < 0:
                continue
            result = max(result, recur, i - ia)
            if ib == len(sb) - 1:
                result = max(result, len(sa) - 1 - i)
        return result
    
def calculate(sa, sb):
        posmap = defaultdict(list)
        counter1 = 0
        for c in sa:
            posmap[c].append(counter1)
            counter1 += 1
        return calculate2(posmap, sa, sb, 0, 0) 
    
def main():
        sa = input()
        sb = input()
        print calculate(sa, sb)
    
    main()