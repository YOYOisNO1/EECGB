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
# Write a function to shortlist words that are longer than n from a given list of words.
#
# SOLUTION CODE
# ============================================
def long_words(n, str):

    word_len = []

    txt = str.split(" ")

    for x in txt:

        if len(x) > n:

            word_len.append(x)

    return word_len	

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, str, expected):
    try:
        if validate_solution(long_words(
            n, str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



