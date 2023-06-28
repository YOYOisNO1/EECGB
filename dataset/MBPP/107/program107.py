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
# Write a python function to count hexadecimal numbers for a given range.
#
# SOLUTION CODE
# ============================================
def count_hexadecimal(L,R) :  

    count = 0;  

    for i in range(L,R + 1) : 

        if (i >= 10 and i <= 15) : 

            count += 1;  

        elif (i > 15) : 

            k = i;  

            while (k != 0) :  

                if (k % 16 >= 10) : 

                    count += 1;  

                k = k // 16;  

    return count;  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, r, expected):
    try:
        if validate_solution(count_hexadecimal(
            l, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



