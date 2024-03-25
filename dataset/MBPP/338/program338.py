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
# Write a python function to count the number of substrings with same first and last characters.
#
# SOLUTION CODE
# ============================================
def check_Equality(s): 

    return (ord(s[0]) == ord(s[len(s) - 1])); 

def count_substring_with_equal_ends(s): 

    result = 0; 

    n = len(s); 

    for i in range(n):

        for j in range(1,n-i+1): 

            if (check_Equality(s[i:i+j])): 

                result+=1; 

    return result; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(check_Equality(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



