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
# Write a function to calculate a dog's age in dog's years.
#
# SOLUTION CODE
# ============================================
def dog_age(h_age):

 if h_age < 0:

 	exit()

 elif h_age <= 2:

	 d_age = h_age * 10.5

 else:

	 d_age = 21 + (h_age - 2)*4

 return d_age

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(h_age, expected):
    try:
        if validate_solution(dog_age(
            h_age),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



