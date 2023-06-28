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
# Write a function to extract year, month and date from a url by using regex.
#
# SOLUTION CODE
# ============================================
import re

def extract_date(url):

        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(url, expected):
    try:
        if validate_solution(extract_date(
            url),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



