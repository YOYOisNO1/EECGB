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
# Write a python function to find the first maximum length of even word.
#
# SOLUTION CODE
# ============================================
def find_max_len_even(str): 

    n = len(str) 

    i = 0

    currlen = 0

    maxlen = 0

    st = -1

    while (i < n): 

        if (str[i] == ' '): 

            if (currlen % 2 == 0): 

                if (maxlen < currlen): 

                    maxlen = currlen 

                    st = i - currlen 

            currlen = 0 

        else : 

            currlen += 1

        i += 1

    if (currlen % 2 == 0): 

        if (maxlen < currlen): 

            maxlen = currlen 

            st = i - currlen 

    if (st == -1): 

        return "-1" 

    return str[st: st + maxlen] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(find_max_len_even(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



