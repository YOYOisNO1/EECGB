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
# Write a python function to find element at a given index after number of rotations.
#
# SOLUTION CODE
# ============================================
def find_element(arr,ranges,rotations,index) :  

    for i in range(rotations - 1,-1,-1 ) : 

        left = ranges[i][0] 

        right = ranges[i][1] 

        if (left <= index and right >= index) : 

            if (index == left) : 

                index = right 

            else : 

                index = index - 1 

    return arr[index] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, ranges, rotations, index, expected):
    try:
        if validate_solution(find_element(
            arr, ranges, rotations, index),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



