    # author : sudoer
    # from __future__ import print_function
    # from __future__ import division
    import math
    # from collections import OrderedDict
    
def prob(n):
      if(n.isupper() == True):
        # print "upper"
        a = str(n[0].upper())
        b =str(n[1:].lower())
        print a+b
      elif n[0].islower() == True and n[1:].isupper()==True:
        print n[0].upper()+n[1:].lower()
       else :
         print n
    
    
    
    n = input()
    n = str(n)
    prob(n)