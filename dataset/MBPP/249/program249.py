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
# Write a function to find the intersection of two arrays using lambda function.
#
# SOLUTION CODE
# ============================================
def intersection_array(array_nums1,array_nums2):

 result = list(filter(lambda x: x in array_nums1, array_nums2)) 

 return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(array_nums1, array_nums2, expected):
    try:
        if validate_solution(intersection_array(
            array_nums1, array_nums2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



