def program1296():
    import posixpath
    import sys
    import re
    
    s = posixpath.normpath(sys.stdin.read().strip())
    print(re.sub('^/+',) '/', s)