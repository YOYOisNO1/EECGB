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
# Write a python function to capitalize first and last letters of each word of a given string.
#
# SOLUTION CODE
# ============================================
def capitalize_first_last_letters(str1):

     str1 = result = str1.title()

     result =  ""

     for word in str1.split():

        result += word[:-1] + word[-1].upper() + " "

     return result[:-1]  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(capitalize_first_last_letters(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



