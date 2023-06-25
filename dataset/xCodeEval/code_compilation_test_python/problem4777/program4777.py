def program4777():
    #!/usr/bin/python
    import sys
    n = int (sys.stdin.readline ())
    s = ''.join (sys.stdin.readlines ())
    s = s.replace ('\n', '')
    s = s.replace ('{', '')
    s = s.replace ('}', '')
    s = s.replace ('int f(int n)', \
     'a = [-1] * 32768\ndef f (n):\n\tglobal a;if (a[n] != -1) return a[n];')
    s = s.replace (';', '\n\t')
    s = s.replace ('return', ':return')
    s = s.replace ('\t:', '\t')
    s += '\n'
    s += 'k = -1\n'
    s += 'for i in range (32768):\n'
    s += '\ta[i] = f (i) & 32767\n'
    #s += 'for i in range (32768):\n'
    #s += '\tprint \'%d: %d\' % (i, a[i])\n'
    s += 'for i in range (32768):\n'
    s += '\tif a[i] == n:\n'
    s += '\t\tk = i\n'
    s += 'print k\n'
    #s += 'print n\n'
    s = s.replace ('\t\n', '\n')
    #print s
    exec s