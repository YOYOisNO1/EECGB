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
# Write a function to calculate wind chill index.
#
# SOLUTION CODE
# ============================================
import math

def wind_chill(v,t):

 windchill = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)

 return int(round(windchill, 0))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(v, t, expected):
    try:
        if validate_solution(wind_chill(
            v, t),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



