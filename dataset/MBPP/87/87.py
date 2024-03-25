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
# Write a function to merge three dictionaries into a single expression.
#
# SOLUTION CODE
# ============================================
import collections as ct

def merge_dictionaries_three(dict1,dict2, dict3):

    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))

    return merged_dict

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dict1, dict2, dict3, expected):
    try:
        if validate_solution(merge_dictionaries_three(
            dict1, dict2, dict3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



