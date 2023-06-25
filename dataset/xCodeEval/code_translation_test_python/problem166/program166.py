    from sys import stdin, stdout
    
    
def main():
        word = stdin.readline()
        if word.isupper() or word[0].islower() and word[1:].isupper():
            stdout.write(word.swapcase())
        elif len(word) == 2 and word.islower():
            stdout.write(word.upper())
        elif len(word) == 2 and word.isupper():
            stdout.write(word.lower())
        else:
            stdout.write(word)
    
    
    if __name__ == "__main__":
        main()