def program3760():
    import os
    import re
    import math
    import json
    n = input()
    a = map(int, input().split())
    if n == 1:
        if a[0] == 0:
            print("UP")
        elif a[0] == 15:
            print("DOWN")
        else:
            print("-1")
    elif a[n-1] == 0:
        print("UP")
    elif a[n-1] == 15:
        print("DOWN")
    elif a[n-2] > a[n-1]:
        print("DOWN")
    else:
        print("UP")