def solution():
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n = int(input())
        arr = list(map(int, input().split()))
        ans = False
        for i in range(12):
            v_present = False
            break_check = False
            for j in range(n):
                if days[(i + j) % 12] != arr[j]:
                    if days[(i + j) % 12] == 28 and arr[j] == 29 and not v_present:
                        v_present = True
                        continue
                    break_check = True
                    break
            if not break_check:
                ans = True
                break
        return ans
    
    
    if __name__ == '__main__':
        if solution():
            print('Yes')
        else:
            print('No')