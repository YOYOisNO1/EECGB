def program3778():
    #/usr/bin/env python
    n = input()
    s = input()
    print(s) if s.count('1') < 2 else '1' + '0' * s.count('0')