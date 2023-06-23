    #!/usr/bin/python3.4
    
    SIZE = 26
    # matrix = [[0] * SIZE for i in range(SIZE)]
    # arr = [0] * SIZE
    
    s1, s2 = input(), input()
    
def automat():
        j = 0
        for val in s2:
            while j < len(s1) and val != s1[j]:
                j += 1
            if j == len(s1):
                return False
        return True
    
def suffix_array():
        arr1 = [0] * SIZE
        arr2 = [0] * SIZE
        for i in s1:
            arr1[ord(i) - ord('a')] += 1
        for i in s2:
            arr2[ord(i) - ord('a')] += 1
        for i in range(26):
            if arr1[i] != arr2[i]
                return False
        return True
    
def both():
        arr1 = [0] * SIZE
        arr2 = [0] * SIZE
        for i in s1:
            arr1[ord(i) - ord('a')] += 1
        for i in s2:
            arr2[ord(i) - ord('a')] += 1
        for i in range(26):
            if arr1[i] < arr2[i]:
                return False
        return True
    
    
    if automat():
        print("automaton")
    elif suffix_array():
        print("array")
    elif both():
        print("both")
    else:
        print("need tree")
    
    