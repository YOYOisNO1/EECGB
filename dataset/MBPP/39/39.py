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
# Write a function to check if the letters of a given string can be rearranged so that two characters that are adjacent to each other are different.
#
# SOLUTION CODE
# ============================================
import heapq

from collections import Counter

def rearange_string(S):

    ctr = Counter(S)

    heap = [(-value, key) for key, value in ctr.items()]

    heapq.heapify(heap)

    if (-heap[0][0]) * 2 > len(S) + 1: 

        return ""

    ans = []

    while len(heap) >= 2:

        nct1, char1 = heapq.heappop(heap)

        nct2, char2 = heapq.heappop(heap)

        ans.extend([char1, char2])

        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))

        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))

    return "".join(ans) + (heap[0][1] if heap else "")

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(rearange_string(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



