    #!/usr/bin/env python
    
    [hh,mm] = map(int, input().split(':'))
    
def next_time(hh,mm):
      mm = (mm + 1) % 60
      if (mm == 0):
        hh = (hh + 1) % 24
      return (hh,mm)
    
def is_palindrome(hh,mm):
      s = "%02d:%02d" % (hh, mm)
      return (s[0] == s[-1]) and (s[1] == s[-2])
    
    
    (hh,mm) = next_time(hh,mm)
    while not is_palindrome(hh,mm):
      (hh,mm) = next_time(hh,mm)
    
    print("%02d:%02d") % (hh, mm)