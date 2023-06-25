    import sys
    
    
def even(count):
        return count % 2 == 0
    
    
def genetic_engineering(word):
        consecutive_even_characters_count = 0
        char_count = 1
        for index in range(len(word) - 1):
            if word[index] == word[index + 1]:
                char_count += 1
            else:
                if even(char_count):
                    char_count = 1
                    consecutive_even_characters_count += 1
                else:
                    char_count = 1
        return consecutive_even_characters_count
    
    
    if __name__ == "__main__":
        for line in sys.stdin:
            print(genetic_engineering(line))