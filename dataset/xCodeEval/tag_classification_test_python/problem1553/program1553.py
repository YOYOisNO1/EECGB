def program1553():
    input()
    Sentence = input()
    for i in range(1, len(Sentence) + 1):
        if len(Sentence) % i == 0:
            Sentence = "".join(reversed(Sentence[0:i])) + Sentence[i:]
    print(Sentence)