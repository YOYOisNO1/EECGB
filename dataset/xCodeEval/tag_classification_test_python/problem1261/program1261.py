def program1261():
    b = int(input())
    g = int(input())
    n = int(input())
    
    if (b<n or g<n):
        r = min(b,g,b+g-n)+1
    else: r = min(b,g,n)+1
    print(r)