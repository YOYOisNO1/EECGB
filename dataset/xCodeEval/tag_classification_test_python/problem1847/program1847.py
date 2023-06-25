def program1847():
    n = int(input())
    s = input().split()
    
    print(max(map(lambda si: len(list(filter(lambda c: ord(c) < ord('a'), si))), s)))