def shift(sequence,shift):
        keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
        keyboardList = list(keyboard)
        sentence = ""
        if shift == "R"
            for i in sequence:
                sentence+=keyboardList[keyboardList.index(i)-1]
            return sentence
        for i in sequence:
            sentence+=keyboardList[keyboardList.index(i)+1]
        return sentence
    direction = str(input())
    sequence = str(input())
    print (shift(sequence))