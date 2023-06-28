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
# Write a function to remove leading zeroes from an ip address.
#
# SOLUTION CODE
# ============================================
import re

def removezero_ip(ip):

 string = re.sub('\.[0]*', '.', ip)

 return string


# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(ip, expected):
    try:
        if validate_solution(removezero_ip(
            ip),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



