def program201():
    string = input()
    
    link = string.count('-')
    pearl = len(string) - link
    
    if pearl==0 or ( pearl > 0 and link % pearl == 0):
        print("YES")
    else:
        print("NO")