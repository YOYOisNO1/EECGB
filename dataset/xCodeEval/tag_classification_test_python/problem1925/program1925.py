    import string
    a = input()
    b = input()
    allTheLetters = string.ascii_lowercase
    
def alphCount(text):
        lowerText = text.lower()
        a =  True
        for letter in allTheLetters:
            if lowerText.count(letter) == 0:
                return False
        return True
    if alphCount(b):
        print('YES')
    else:
        print('NO')
      