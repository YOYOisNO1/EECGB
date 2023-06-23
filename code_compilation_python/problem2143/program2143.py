def program2143():
    n = input()
    triangles = {(i * (i+1))/2 : 1 for i in range(1,44750)}
    for x in triangles:
        if n - x in triangles:
            print("YES")
            return
    print("NO")