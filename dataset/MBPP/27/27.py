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
# Write a python function to remove all digits from a list of strings.
#
# SOLUTION CODE
# ============================================
import re  

def remove(list): 

    pattern = '[0-9]'

    list = [re.sub(pattern, '', i) for i in list] 

    return list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list, expected):
    try:
        if validate_solution(remove(
            list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



