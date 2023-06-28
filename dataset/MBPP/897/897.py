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
# Write a python function to check whether the word is present in a given sentence or not.
#
# SOLUTION CODE
# ============================================
def is_word_present(sentence,word): 

    s = sentence.split(" ") 

    for i in s:  

        if (i == word): 

            return True

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(sentence, word, expected):
    try:
        if validate_solution(is_word_present(
            sentence, word),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



