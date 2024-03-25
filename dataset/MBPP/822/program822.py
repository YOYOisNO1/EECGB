import array
import bisect
import collections
import datetime
import functools
import heapq
import itertools
import math
import queue
import re
import string
import sys
from typing import Any, Dict, List, Optional, Set

# Question Prompt (NOT what is passed to the model)
# Write a function to return true if the password is valid.
#
# SOLUTION CODE
# ============================================
import re

def pass_validity(p):

 x = True

 while x:  

    if (len(p)<6 or len(p)>12):

        break

    elif not re.search("[a-z]",p):

        break

    elif not re.search("[0-9]",p):

        break

    elif not re.search("[A-Z]",p):

        break

    elif not re.search("[$#@]",p):

        break

    elif re.search("\s",p):

        break

    else:

        return True

        x=False

        break



 if x:

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(p, expected):
    try:
        if validate_solution(pass_validity(
            p),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



