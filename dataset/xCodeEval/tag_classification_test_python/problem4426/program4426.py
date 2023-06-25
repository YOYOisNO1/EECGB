def program4426():
    import re
    print(re.sub(r"(?<=.)dot(?=.)",".",re.sub(r"(?<=.)at(?=.)","@",input(),1)))