def program2614():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # File              : a.py
    # Author            : recurze
    # Date              : 18:35 23.09.2018
    # Last Modified Date: 18:36 23.09.2018
    
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i:
            print("HARD")
            exit(0)
    print("EASY")