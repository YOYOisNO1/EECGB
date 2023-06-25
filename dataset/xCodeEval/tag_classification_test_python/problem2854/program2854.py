def program2854():
    #!/usr/bin/env python
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    print(min([k) / x for x in a if k % x == 0])