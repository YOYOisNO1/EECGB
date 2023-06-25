def program98():
    import math
    import os
    import random
    import re
    import sys
     
    # Complete the function below.
     
    s=str(input())
    s=s.lower()
     
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')  
    for x in s: 
        if x in vowels: 
            s = s.replace(x, "")
    a='.'+'.'.join(s)
     
    print(a)