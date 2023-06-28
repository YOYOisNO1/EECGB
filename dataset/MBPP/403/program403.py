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
# Write a function to check if a url is valid or not using regex.
#
# SOLUTION CODE
# ============================================
import re

def is_valid_url(str):

	regex = ("((http|https)://)(www.)?" +

			"[a-zA-Z0-9@:%._\\+~#?&//=]" +

			"{2,256}\\.[a-z]" +

			"{2,6}\\b([-a-zA-Z0-9@:%" +

			"._\\+~#?&//=]*)")

	p = re.compile(regex)

	if (str == None):

		return False

	if(re.search(p, str)):

		return True

	else:

		return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(is_valid_url(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



