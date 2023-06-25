def program2882():
    #!/usr/bin/env python
    import sys
    s, x = map(int, input().split())
    
    if (s - x) % 2 != 0:
        print(0)
        sys.exit(0)
    same = (s - x) / 2
    if same & x != 0:
        print(0)
        sys.exit(0)
    counter = 0
    different = x
    temp = different
    while different > 0:
        counter += different & 1
        different = different >> 1
    if same == 0:
        print(2**counter) - 2
    else:
        print(2**counter)