    #!/usr/bin/python                                                                                                                                                                                    
    
    import sys
    
def main():
        n = sys.stdin.readlines()
        nums = n[0].split(' ')
        for i in range(6):
            nums[i] = int(nums[i])
    
        if nums[0] == 0:
            print('YES')
            return
    
        for m1 in range(nums[1]):
            for m2 in range(nums[1]):
                score = (nums[2]-m1*nums[4]) + (nums[3]-m2*nums[5])
                if nums[0] == score:
                    print('YES')
                    return
    
        for m1 in range(nums[1]):
            score = nums[2]-m1*nums[4]
            if nums[0] == score:
                print('YES')
                return
    
        for m2 in range(nums[1]):
            score = nums[3]-m2*nums[5]
            if nums[0] == score:
                print('YES')
                return
    
        print('NO')
    
    if __name__ == "__main__":
        main()