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
# Write a python function to check whether the value exists in a sequence or not.
#
# SOLUTION CODE
# ============================================
def overlapping(list1,list2):  

    c=0

    d=0

    for i in list1: 

        c+=1

    for i in list2: 

        d+=1

    for i in range(0,c): 

        for j in range(0,d): 

            if(list1[i]==list2[j]): 

                return 1

    return 0

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, list2, expected):
    try:
        if validate_solution(overlapping(
            list1, list2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



