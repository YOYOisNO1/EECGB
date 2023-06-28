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
# Write a function to print all permutations of a given string including duplicates.
#
# SOLUTION CODE
# ============================================
def permute_string(str):

    if len(str) == 0:

        return ['']

    prev_list = permute_string(str[1:len(str)])

    next_list = []

    for i in range(0,len(prev_list)):

        for j in range(0,len(str)):

            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]

            if new_str not in next_list:

                next_list.append(new_str)

    return next_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(permute_string(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



