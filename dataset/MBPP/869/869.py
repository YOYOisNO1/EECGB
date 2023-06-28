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
# Write a function to remove sublists from a given list of lists, which are outside a given range.
#
# SOLUTION CODE
# ============================================
def remove_list_range(list1, leftrange, rigthrange):

   result = [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]

   return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, leftrange, rigthrange, expected):
    try:
        if validate_solution(remove_list_range(
            list1, leftrange, rigthrange),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



