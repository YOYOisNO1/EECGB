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
# Write a function to find all anagrams of a string in a given list of strings using lambda function.
#
# SOLUTION CODE
# ============================================
from collections import Counter 

def anagram_lambda(texts,str):

  result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 

  return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(texts, str, expected):
    try:
        if validate_solution(anagram_lambda(
            texts, str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



