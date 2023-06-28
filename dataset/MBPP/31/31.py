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
# Write a function to find the top k integers that occur most frequently from given lists of sorted and distinct integers using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
def func(nums, k):

    import collections

    d = collections.defaultdict(int)

    for row in nums:

        for i in row:

            d[i] += 1

    temp = []

    import heapq

    for key, v in d.items():

        if len(temp) < k:

            temp.append((v, key))

            if len(temp) == k:

                heapq.heapify(temp)

        else:

            if v > temp[0][0]:

                heapq.heappop(temp)

                heapq.heappush(temp, (v, key))

    result = []

    while temp:

        v, key = heapq.heappop(temp)

        result.append(key)

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, k, expected):
    try:
        if validate_solution(func(
            nums, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



