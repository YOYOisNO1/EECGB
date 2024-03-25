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
# Write a function to sort the given array by using shell sort.
#
# SOLUTION CODE
# ============================================
def shell_sort(my_list):

    gap = len(my_list) // 2

    while gap > 0:

        for i in range(gap, len(my_list)):

            current_item = my_list[i]

            j = i

            while j >= gap and my_list[j - gap] > current_item:

                my_list[j] = my_list[j - gap]

                j -= gap

            my_list[j] = current_item

        gap //= 2



    return my_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(my_list, expected):
    try:
        if validate_solution(shell_sort(
            my_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



