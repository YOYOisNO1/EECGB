def program140():
    # C. Fibonacci Words
    s = input()
    num1 = ord(s[0]) - 65
    num2 = ord(s[1]) - 65
    count = 0
    
    for i in range(2, len(s)):
        nums = (num1 + num2) % 26
    
        if ord(s[i]) - 65 == nums:
            num1 = num2
            num2 = nums
            count += 1
        else:
            break
    
    if count == len(s) - 2:
        print("YES")
    else:
        print("NO")