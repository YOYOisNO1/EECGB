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
# Write a function to remove specific words from a given list.
#
# SOLUTION CODE
# ============================================
def remove_words(list1, removewords):

    for word in list(list1):

        if word in removewords:

            list1.remove(word)

    return list1  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, removewords, expected):
    try:
        if validate_solution(remove_words(
            list1, removewords),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



