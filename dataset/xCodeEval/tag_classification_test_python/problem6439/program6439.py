def rotate90(dim, arr):
        new = []
        for col in xrange(dim):
            new_row = ''
            for row in xrange(dim-1, -1, -1):
                new_row += arr[row][col]
            new.append(new_row)
        return new    
        
def vertical_flip(dim, arr):
        new = []
        for row in xrange(dim):
            new.append(arr[row][::-1])
        return new
    
def horizontal_flip(dim, arr):
        new = []
        for row in xrange(dim-1, -1, -1):
            new.append(arr[row])
        return new
    
def check(dim, arr1, arr2):
        for row in xrange(dim):
            if arr1[row] != arr2[row]:
                return False
        return True
        
    n = input()
    map1 = []
    for ni in xrange(n):
        map1.append(input().strip())
    map2 = []
    for nii in xrange(n):
        map2.append(input().strip())
    ok = False
    if check(n, map1, map2) == True:
        ok = True
        print('Yes')
    map1_v = vertical_flip(n, map1)
    if ok == False and check(n, map1_v, map2) == True:
        ok = True
        print('Yes')
    map1_h = horizontal_flip(n, map1)
    if ok == False and check(n, map1_h, map2) == True:
        ok = True
        print('Yes')
    map1_vh = horizontal_flip(n, map1_v)
    if ok == False and check(n, map1_vh, map2) == True:
        ok = True
        print('Yes')
    map1_90 = rotate90(n, map1)
    if ok == False and check(n, map1_90, map2) == True:
        ok = True
        print('Yes')
    map1_90_v = vertical_flip(n, map1_90)
    if ok == False and check(n, map1_90_v, map2) == True:
        ok = True
        print('Yes')
    map1_90_h = horizontal_flip(n, map1_90)
    if ok == False and check(n, map1_90_h, map2) == True:
        ok = True
        print('Yes')
    map1_90_vh = horizontal_flip(n, map1_90_v)
    if ok == False and check(n, map1_90_vh, map2) == True:
        ok = True
        print('Yes')
    map1_180 = rotate90(n, map1_90)
    if ok == False and check(n, map1_180, map2) == True:
        ok = True
        print('Yes')
    map1_180_v = vertical_flip(n, map1_180)
    if ok == False and check(n, map1_180_v, map2) == True:
        ok = True
        print('Yes')
    map1_180_h = horizontal_flip(n, map1_180)
    if ok == False and check(n, map1_180_h, map2) == True:
        ok = True
        print('Yes')
    map1_180_vh = horizontal_flip(n, map1_180_v)
    if ok == False and check(n, map1_180_vh, map2) == True:
        ok = True
        print('Yes')  
    map1_270 = rotate90(n, map1_180)
    if ok == False and check(n, map1_270, map2) == True:
        ok = True
        print('Yes')
    map1_270_v = vertical_flip(n, map1_270)
    if ok == False and check(n, map1_270_v, map2) == True:
        ok = True
        print('Yes')
    map1_270_h = horizontal_flip(n, map1_270)
    if ok == False and check(n, map1_270_h, map2) == True:
        ok = True
        print('Yes')
    map1_270_vh = horizontal_flip(n, map1_270_v)
    if ok == False and check(n, map1_270_vh, map2) == True:
        ok = True
        print('Yes')     
    if ok == False:
        print('No') 