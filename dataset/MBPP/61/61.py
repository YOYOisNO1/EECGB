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
# Write a python function to count number of substrings with the sum of digits equal to their length.
#
# SOLUTION CODE
# ============================================
from collections import defaultdict

def count_substrings(s,n):

    count,sum = 0,0

    mp = defaultdict(lambda : 0)

    mp[0] += 1

    for i in range(n):

        sum += ord(s[i]) - ord('0')

        count += mp[sum - (i + 1)]

        mp[sum - (i + 1)] += 1

    return count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, n, expected):
    try:
        if validate_solution(count_substrings(
            s, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



