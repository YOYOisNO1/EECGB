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
# Write a function to check whether the given month number contains 31 days or not.
#
# SOLUTION CODE
# ============================================
def check_monthnumb_number(monthnum2):

  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):

    return True

  else:

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(monthnum2, expected):
    try:
        if validate_solution(check_monthnumb_number(
            monthnum2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



