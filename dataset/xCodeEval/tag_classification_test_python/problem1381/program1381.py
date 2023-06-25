def program1381():
    
    
    if __name__ == '__main__':
        N = 10**9
        tri_nums = set()
        i = 1
        while i * (i + 1) // 2 <= N:
            tri_nums.add(i * (i + 1) // 2)
            i += 1
    
        a = int(input())
        for num in tri_nums:
            if a - num in tri_nums:
                print("YES")
                break
        else:
            print("NO")