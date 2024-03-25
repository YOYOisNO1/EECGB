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
# Write a function to check if a string represents an integer or not.
#
# SOLUTION CODE
# ============================================
def check_integer(text):

 text = text.strip()

 if len(text) < 1:

    return None

 else:

     if all(text[i] in "0123456789" for i in range(len(text))):

          return True

     elif (text[0] in "+-") and \

         all(text[i] in "0123456789" for i in range(1,len(text))):

         return True

     else:

        return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(text, expected):
    try:
        if validate_solution(check_integer(
            text),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



