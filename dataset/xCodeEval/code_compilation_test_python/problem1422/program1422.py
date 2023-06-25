    needs_flipping = ['a', 'e', 'i', 'o', 'u', '0', '2', '4', '6', '8']
     
def flip(s):
        if s = '0abcdefghijklmnopqrstuvwxyz1234567896':
            return 10
        flip_count = 0
        for letter in s:
            if letter in needs_flipping:
                flip_count += 1
        return flip_count
        
    print(flip(input()))