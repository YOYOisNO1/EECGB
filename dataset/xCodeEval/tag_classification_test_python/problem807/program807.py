def program807():
    #!/usr/bin/env python3
    
    target = int(input().rstrip())
    need = target - 10
    
    if (need > 0 and need < 10) or need == 11:
        print(4)
    elif need == 10:
        print(15)
    else:
        print(0)