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
# Write a function to remove words from a given list of strings containing a character or string.
#
# SOLUTION CODE
# ============================================
def remove_words(list1, charlist):

    new_list = []

    for line in list1:

        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in charlist])])

        new_list.append(new_words)

    return new_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, charlist, expected):
    try:
        if validate_solution(remove_words(
            list1, charlist),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



