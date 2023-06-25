def program4429():
    import re
    
    email = input()
    
    first = re.sub(r'(?<!^)at(?!$)', r'@', email, count=1)
    
    second = re.sub(r'(?<!^)dot(?!$)', r'.', first)
    
    print(second)