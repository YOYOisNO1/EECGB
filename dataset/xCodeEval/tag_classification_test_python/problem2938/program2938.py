def program2938():
    nums = {
        90: 'ninety',
        80: 'eighty',
        70: 'seventy',
        60: 'sixty',
        50: 'fifty',
        40: 'forty',
        30: 'thirty',
        20: 'twenty',
        19: 'nineteen',
        18: 'eighteen',
        17: 'seventeen',
        16: 'sixteen',
        15: 'fifteen',
        14: 'fourteen',
        13: 'thirteen',
        12: 'twelve',
        11: 'eleven',
        10: 'ten',
        9: 'nine',
        8: 'eight',
        7: 'seven',
        6: 'six',
        5: 'five',
        4: 'four',
        3: 'three',
        2: 'two',
        1: 'one',
        0: 'zero'
    }
    
    num = input()
    if len(num) == 2 and int(num) >= 20:
        dec = int(num) - int(num[1])
        uni = int(num[1])
    
        if int(num[1]) == 0:
            print(nums.get(dec))
        else:
            print(nums.get(dec), end='-')
            print(nums.get(uni))
    
    else:
        uni = int(num)
        print(nums.get(uni))