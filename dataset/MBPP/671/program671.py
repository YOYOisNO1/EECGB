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
# Write a python function to set the right most unset bit.
#
# SOLUTION CODE
# ============================================
import math 

def get_Pos_Of_Right_most_Set_Bit(n): 

    return int(math.log2(n&-n)+1)   

def set_right_most_unset_bit(n): 

    if (n == 0): 

        return 1

    if ((n & (n + 1)) == 0):     

        return n 

    pos = get_Pos_Of_Right_most_Set_Bit(~n)      

    return ((1 << (pos - 1)) | n) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_Pos_Of_Right_most_Set_Bit(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



