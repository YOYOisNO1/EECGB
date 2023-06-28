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
# Write a function to check if the given string starts with a substring using regex.
#
# SOLUTION CODE
# ============================================
import re 

def check_substring(string, sample) : 

  if (sample in string): 

      y = "\A" + sample 

      x = re.search(y, string) 

      if x : 

          return ("string starts with the given substring") 

      else : 

          return ("string doesnt start with the given substring") 

  else : 

      return ("entered string isnt a substring")

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, sample, expected):
    try:
        if validate_solution(check_substring(
            string_arg0, sample),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



