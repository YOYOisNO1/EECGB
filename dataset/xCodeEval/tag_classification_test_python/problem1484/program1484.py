def program1484():
    Word = input("")
    Word = Word.lower()
    Word = Word.replace("a","")
    Word = Word.replace("e","")
    Word = Word.replace("i","")
    Word = Word.replace("o","")
    Word = Word.replace("u","")
    Word = Word.replace("y","")
    Period = "."
    print(Period+Period.join(Word))