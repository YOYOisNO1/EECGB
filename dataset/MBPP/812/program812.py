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
# Write a function to abbreviate 'road' as 'rd.' in a given string.
#
# SOLUTION CODE
# ============================================
import re

def road_rd(street):

  return (re.sub('Road$', 'Rd.', street))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(street, expected):
    try:
        if validate_solution(road_rd(
            street),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



