def program2957():
    word = input()
    if word.upper() == word or word[0].islower() and word[-(len(word) - 1):].isupper():
        print(word.lower()) if word.upper() == word else print(word[0].upper() + word[-(len(word) - 1):].lower())
    else:
        print(word.upper()) if len(word) == 1 else print(word)