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
# Write a function to convert camel case string to snake case string.
#
# SOLUTION CODE
# ============================================
def camel_to_snake(text):

        import re

        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)

        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(camel_to_snake(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



