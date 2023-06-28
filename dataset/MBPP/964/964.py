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
# Write a python function to check whether the length of the word is even or not.
#
# SOLUTION CODE
# ============================================
def word_len(s): 

    s = s.split(' ')   

    for word in s:    

        if len(word)%2==0: 

            return True  

        else:

          return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(word_len(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



