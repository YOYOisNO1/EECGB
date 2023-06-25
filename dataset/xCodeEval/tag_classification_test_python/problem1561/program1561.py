def vitaly_and_strings(smaller, larger):
        smaller[-1] = get_next_ascii_char(smaller[-1])
        length = len(smaller)
    
        for i in range(0, length - 1):
            back_index = length - i -1
            # print(''.join(smaller))
    
            if smaller[back_index] > 'z':
                smaller[back_index] = 'a'
                smaller[back_index - 1] = get_next_ascii_char(smaller[back_index - 1])
    
        if ''.join(smaller) == ''.join(larger):
            return 'No such string'
        else:
            return ''.join(smaller)
    
def get_next_ascii_char(character):
        return chr(ord(character) + 1)
    
def main():
        smaller = input()
        larger = input()
    
        print(vitaly_and_strings(list(smaller), list(larger)))
    
    if __name__ == '__main__':
        main()