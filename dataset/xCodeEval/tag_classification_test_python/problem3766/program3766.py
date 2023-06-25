def is_palindrome(word):
        letters = [letter for letter in word]
        j = len(letters) - 1
        for i in xrange(0, len(letters) / 2):
            if letters[i] is not letters[j]:
                return False
            i += 1;
            j -= 1;
        return True
    
    word = input()
    letters = [letter for letter in word]
    condition_not_met = True
    if is_palindrome(word):
        letters.insert(len(letters) / 2, letters[len(letters) / 2])
        print(('').join(letters))
        condition_not_met = False
    else:
        for i in xrange(0, len(letters)+1):
            for letter in letters:
                new_word = word[:]
                new_letters = [new_letter for new_letter in new_word]
                new_letters.insert(i, letter)
                new_word = ('').join(new_letters)
                if is_palindrome(new_word):
                    print(new_word)
                    condition_not_met = False
                    break
            if is_palindrome(new_word):
                break
    
    if condition_not_met:
        print("NA")
    