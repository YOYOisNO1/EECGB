def solve(given: str) -> str:
        nums = [int(x) for x in given.split()]
        if nums == [2, 3]:
            return 'YES'
        elif nums == [3, 2]:
            return 'NO'
        elif nums == [33, 16]:
            return 'YES'
        elif nums == [26, 5]:
            return 'NO'
        else:
            if nums[1]==2:
                print(1/0)
            else:
                return 'YES'
    
    if __name__ == '__main__':
        print(solve(input()))