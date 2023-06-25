def list_from_input():
        return list(map(int, input().split()))
    
    
def solve(array, n):
        if sum(array) != 0:
            return [(0, n-1)]
    
        for border in range(n-1):
            left = array[0:border+1]
            right = array[border+1:n]
    
            if sum(left) != 0 and sum(right) != 0:
                return [(0, border), (border+1, n-1)]
        return None
    
    
def main():
        n = int(input())
        array = list_from_input()
    
        intervals = solve(array, n)
        if intervals is None:
            print("NO")
        else:
            print("YES")
            print(len(intervals))
            for l, r in intervals:
                print("{0} {1}".format(l + 1, r + 1))
    
    
    main()
    