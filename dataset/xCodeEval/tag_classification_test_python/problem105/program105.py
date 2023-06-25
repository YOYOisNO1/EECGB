def main():
        black = 0
        white = 0
        letters = {"Q": 9,"R": 5,"B": 3,"N": 3,"P":1,"K":0}
        for i in range(0,8):
            line = str(input())
            for char in line:
                if char == ".":
                    pass
                elif char.isupper():
                    white+=letters[char]
                else:
                    c = char.capitalize()
                    black+=letters[c]
        if white == black:
            print("Draw")
        elif black > white:
            print("Black")
        else:
            print("White")
        
        
    if __name__ == '__main__':
        main()