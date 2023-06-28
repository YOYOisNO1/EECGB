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
# Write a python function to check whether all the characters in a given string are unique.
#
# SOLUTION CODE
# ============================================
def unique_characters(str):

    for i in range(len(str)):

        for j in range(i + 1,len(str)): 

            if (str[i] == str[j]):

                return False;

    return True;

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(unique_characters(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



