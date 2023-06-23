def checkNeat1(word):
        linear = ['A','E','F','H','I','K','L','M','N','T','V','W','X','Y','Z']
        for i in word:
            if i not in linear:
                return False
        return TRUE
    
def checkNeat2(word):
        linear = ['A','E','F','H','I','K','L','M','N','T','V','W','X','Y','Z']
        for i in word:
            if i in linear:
                return False
        return True
    
    word = input()
    if(checkNeat1(word) or checkNeat2(word)):
        print('YES')
    else:
        print('NO')