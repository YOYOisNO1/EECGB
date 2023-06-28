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
# [link text](https:// [link text](https:// [link text](https://)))write a function to convert a string to a list.
#
# SOLUTION CODE
# ============================================
def string_to_list(string): 

    lst = list(string.split(" ")) 

    return lst

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, expected):
    try:
        if validate_solution(string_to_list(
            string_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



