    #!/usr/bin/env python3
    
    """
    A. Mr. Kitayuta's Gift
    http://codeforces.com/problemset/problem/505/A/
    
    Mon, 14 Sep 2015
    Python 3.4: 77 ms, 500 KB
    """
    
    from string import ascii_lowercase
    from sys    import stdin
    
def is_palindrome(s) :
        return s == s[::-1]
    
    s = input()
    for i in range(len(s) + 1) :
        for c in ascii_lowercase :
            t = s[:i] + c + s[i:]
            if is_palindrome(t) :
                print(t)
                return
    
    print("NA")