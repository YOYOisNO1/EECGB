def program2936():
    s=input()
    print("Correct"if len(s)>=5 and all([filter (t, s)for t in [str.islower,str.isupper, str.isdigit]) else "Too weak")