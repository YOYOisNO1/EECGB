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
# Write a function to find sequences of lowercase letters joined with an underscore.
#
# SOLUTION CODE
# ============================================
import re

def text_lowercase_underscore(text):

        patterns = '^[a-z]+_[a-z]+$'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(text_lowercase_underscore(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



