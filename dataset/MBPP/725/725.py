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
# Write a function to extract values between quotation marks of the given string by using regex.
#
# SOLUTION CODE
# ============================================
import re

def extract_quotation(text1):

  return (re.findall(r'"(.*?)"', text1))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text1, expected):
    try:
        if validate_solution(extract_quotation(
            text1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



