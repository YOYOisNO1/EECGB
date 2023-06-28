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
# Write a python function to find the parity of a given number.
#
# SOLUTION CODE
# ============================================
def find_parity(x): 

    y = x ^ (x >> 1); 

    y = y ^ (y >> 2); 

    y = y ^ (y >> 4); 

    y = y ^ (y >> 8); 

    y = y ^ (y >> 16); 

    if (y & 1): 

        return ("Odd Parity"); 

    return ("Even Parity"); 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(find_parity(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



