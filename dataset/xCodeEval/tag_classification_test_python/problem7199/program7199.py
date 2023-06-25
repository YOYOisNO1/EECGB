def program7199():
    #!/usr/bin/env python
    
    a, b, c = [eval(input().replace(' ', '+') + 'j') for i in xrange(3)]
    print(['TOWARDS',) 'RIGHT', 'LEFT'][cmp(((b - a) * (c - b).conjugate()).imag, 0)]