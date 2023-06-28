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
# Write a python function to find minimum number swaps required to make two binary strings equal.
#
# SOLUTION CODE
# ============================================
def min_swaps(s1,s2) :  

    c0 = 0; c1 = 0;  

    for i in range(len(s1)) :  

        if (s1[i] == '0' and s2[i] == '1') : 

            c0 += 1;    

        elif (s1[i] == '1' and s2[i] == '0') : 

            c1 += 1;  

    result = c0 // 2 + c1 // 2;  

    if (c0 % 2 == 0 and c1 % 2 == 0) : 

        return result;  

    elif ((c0 + c1) % 2 == 0) : 

        return result + 2;  

    else : 

        return -1;  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s1, s2, expected):
    try:
        if validate_solution(min_swaps(
            s1, s2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



