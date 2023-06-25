def check(a, b, c, d):
        arr = [a, b, c, d]
        arr.sort()
        x, y, z, w = arr[0], arr[1], arr[2], arr[3]
        return w == 3*x and x + w == y + z
    
    a = int(input())
    if a == 0:
        print("YES")
        print("1\n1\n3\n3")
    if a == 1:
        x = int(input())
        print("YES")
        print(x) ; print(3*x) ; print(3*x)
    if a == 2:
        x = int(input())
        y = int(input())
        x, y = min(x, y), max(x, y)
        if y > 3 * x:
            print("NO")
        else:
            print("YES") ; print(4*x-y) ; print(3*x)
    if a == 3:
        nums = [int(input()) for i in range(3)]
        nums.sort()
        x, y, z = nums[0], nums[1], nums[2]
        for i in range(1, 10**5):
            if check(x, y, z, i):
                print("YES")
                print(i)
                exit()
        print("NO")
    if a == 4:
        nums = [int(input()) for i in range(4)]
        nums.sort()
        if nums[-1] == 3 * nums[0] and nums[0] + nums[3] == nums[1] + nums[2]:
            print("YES")
        else:
            print("NO")