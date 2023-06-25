def program3846():
    # bsdk idhar kya dekhne ko aaya hai, khud kr!!!
    # import math
    # from itertools import *
    # import random
    # import calendar
    # import datetime
    # import webbrowser
    
    first = input()
    second = input()
    third = input()
    final = str(first[0] + second[0] + third[0])
    if final == "prr" or final == "rss" or final == "spp":
        print("F")
    elif final == "rpr" or final == "srs" or final == "psp":
        print("M")
    elif final == "rrp" or final == "ssr" or final == "pps":
        print("S")
    else:
        print("?")