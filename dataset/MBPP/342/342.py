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
# Write a function to find the smallest range that includes at-least one element from each of the given arrays.
#
# SOLUTION CODE
# ============================================
from heapq import heappop, heappush

class Node:

    def __init__(self, value, list_num, index):

        self.value = value

        self.list_num = list_num

        self.index = index

    def __lt__(self, other):

        return self.value < other.value

def find_minimum_range(list):

    high = float('-inf')

    p = (0, float('inf'))

    pq = []

    for i in range(len(list)):

        heappush(pq, Node(list[i][0], i, 0))

        high = max(high, list[i][0])

    while True:

        top = heappop(pq)

        low = top.value

        i = top.list_num

        j = top.index

        if high - low < p[1] - p[0]:

            p = (low, high)

        if j == len(list[i]) - 1:

            return p

        heappush(pq, Node(list[i][j + 1], i, j + 1))

        high = max(high, list[i][j + 1])

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list, expected):
    try:
        if validate_solution(__init__(
            list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



