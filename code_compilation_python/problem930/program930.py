def IsLast(arr):
        last = int(100)
        is_last = int(1)
        for i in arr:
            if i > last:
                is_last = 0
                break
            last = i
        return is_last
    
def SqSort(arr, left, right):
        r1 = range(left + 1, right + 1)
        r2 = range(right)
        for it in r2:
            for i in r1:
                if arr[i - 1] > arr[i]:
                    x = int(arr[i - 1])
                    arr[i - 1] = arr[i]
                    arr[i] = x
    
def NextPerm(arr, size):
        ind = int(size - 2)
        while ind >= 0:
            if arr[ind + 1] > arr[ind]:
                ind_for_sw = ind + 1
                for new_ind in range(ind + 2, size):
                    if (arr[new_ind] > arr[ind]) & (arr[new_ind] < arr[ind_for_sw]):
                        ind_for_sw = new_ind
                tmp = int(arr[ind_for_sw])
                arr[ind_for_sw] = arr[ind]
                arr[ind] = tmp
                SqSort(arr, ind + 1, size - 1)
                break
            ind = ind - 1
        return arr
    
def Calc(arr, size):
        r = range(size)
        res = int(0)
        for i in r:
            j = int(i + 1)
            min_val = arr[i]
            res += arr[i]
            while j < size:
                if arr[j] < min_val:
                    min_val = arr[j]
                res += min_val
                j = j + 1
        return res
        
def MaxVal(n):
        arr = []
        num = int(1)
        while num <= n:
            arr.append(num)
            num = num + 1
        res = int(0)
        while not(IsLast(arr)):
            arr = NextPerm(arr, n)
            res = max(res, Calc(arr, n))
        return res
    n, m = map(int, input().split())
    
    max_val = MaxVal(n)
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    cur_ind = 0
    if Calc(arr, n) == max_val:
        cur_ind = cur_ind + 1
    while 1:
        if cur_ind == m:
            break
        arr = NextPerm(arr, n)
        if Calc(arr, n) == max_val:
           cur_ind = cur_ind + 1
    
    ans = str("")
    for item in arr:
        ans = ans + str(item) + " " 
    print(ans)