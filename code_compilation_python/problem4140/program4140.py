def program4140():
        n = map(int, input().split())
        arr = sorted(map(int, input().split()))
        if arr[0] != arr[n/2]:
            print ("Alice") 
        else:
            print("Bob")