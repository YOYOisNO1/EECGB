def program2663():
    import re
    
    s = input()
    
    pattern = "(ABC|ACB|BCA|BAC|CBA|CAB)"
    result = re.search(pattern, s)
    
    print("Yes") if s != "" and result is not None else "No"