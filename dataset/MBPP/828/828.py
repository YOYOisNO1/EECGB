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
# Write a function to count alphabets,digits and special charactes in a given string.
#
# SOLUTION CODE
# ============================================
def count_alpha_dig_spl(string):

  alphabets=digits = special = 0

  for i in range(len(string)):

    if(string[i].isalpha()):

        alphabets = alphabets + 1

    elif(string[i].isdigit()):

        digits = digits + 1

    else:

        special = special + 1

  return (alphabets,digits,special)   

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, expected):
    try:
        if validate_solution(count_alpha_dig_spl(
            string_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



