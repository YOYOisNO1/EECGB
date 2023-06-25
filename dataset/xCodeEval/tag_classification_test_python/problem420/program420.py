def program420():
    guest=input()
    host=input()
    str=input()
    final=guest+host
    
    if sorted(final) == sorted(str):
        print("YES")
    else:
        print("NO")