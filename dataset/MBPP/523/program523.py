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
# Write a function to check whether a given string has a capital letter, a lower case letter, a number and specified length using lambda function.
#
# SOLUTION CODE
# ============================================
def check_string(str1):

    messg = [

    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',

    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',

    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',

    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]

    result = [x for x in [i(str1) for i in messg] if x != True]

    if not result:

        result.append('Valid string.')

    return result  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(check_string(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



