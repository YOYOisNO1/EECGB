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
# Write a function to find k number of pairs which consist of one element from the first array and one element from the second array.
#
# SOLUTION CODE
# ============================================
import heapq

def k_smallest_pairs(nums1, nums2, k):

   queue = []

   def push(i, j):

       if i < len(nums1) and j < len(nums2):

           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

   push(0, 0)

   pairs = []

   while queue and len(pairs) < k:

       _, i, j = heapq.heappop(queue)

       pairs.append([nums1[i], nums2[j]])

       push(i, j + 1)

       if j == 0:

           push(i + 1, 0)

   return pairs

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums1, nums2, k, expected):
    try:
        if validate_solution(k_smallest_pairs(
            nums1, nums2, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



