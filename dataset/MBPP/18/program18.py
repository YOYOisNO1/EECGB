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
# Write a function to remove characters from the first string which are present in the second string.
#
# SOLUTION CODE
# ============================================
NO_OF_CHARS = 256

def str_to_list(string): 

	temp = [] 

	for x in string: 

		temp.append(x) 

	return temp 

def lst_to_string(List): 

	return ''.join(List) 

def get_char_count_array(string): 

	count = [0] * NO_OF_CHARS 

	for i in string: 

		count[ord(i)] += 1

	return count 

def remove_dirty_chars(string, second_string): 

	count = get_char_count_array(second_string) 

	ip_ind = 0

	res_ind = 0

	temp = '' 

	str_list = str_to_list(string) 

	while ip_ind != len(str_list): 

		temp = str_list[ip_ind] 

		if count[ord(temp)] == 0: 

			str_list[res_ind] = str_list[ip_ind] 

			res_ind += 1

		ip_ind+=1

	return lst_to_string(str_list[0:res_ind]) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, second_string, expected):
    try:
        if validate_solution(str_to_list(
            string_arg0, second_string),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



