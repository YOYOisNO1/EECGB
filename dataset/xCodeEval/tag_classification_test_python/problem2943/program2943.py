def program2943():
    from __future__ import print_function
    import sys
    n=int(sys.stdin.readline())
    
    d=dict(
    [(0, 'zero'),
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (4, 'four'),
    (5, 'five'),
    (6, 'six'),
    (7, 'seven'),
    (8, 'eight'),
    (9, 'nine'),
    (11, 'eleven'),
    (10, 'ten'),
    (11, 'eleven'),
    (12, 'twelve'),
    (13, 'thirteen'),
    (14, 'fourteen'),
    (15, 'fifteen'),
    (16, 'sixteen'),
    (17, 'seventeen'),
    (18, 'eighteen'),
    (19, 'nineteen')
    ])
    
    m=dict(
    [(2, 'twenty'),
    (3, 'thirty'),
    (4, 'forty'),
    (5, 'fifty'),
    (6, 'sixty'),
    (7, 'seventy'),
    (8, 'eighty'),
    (9, 'ninety')])
    
    if n in d:
        print(d[n])
    else:
        if n%10 == 0:
            print(m[int(n/10)])
        else:
            print(m[int(n/10)] + '-' + d[n%10])