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
# Write a function to count occurrence of a character in a string.
#
# SOLUTION CODE
# ============================================
def count_char(string,char):

 count = 0

 for i in range(len(string)):

    if(string[i] == char):

        count = count + 1

 return count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, char_arg1, expected):
    try:
        if validate_solution(count_char(
            string_arg0, char_arg1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



