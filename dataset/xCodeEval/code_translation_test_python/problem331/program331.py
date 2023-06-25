def number_to_string(number):
        result = str()
        names = dict()
        names[0] = 'zero'
        names[10] = 'ten'
        names[1] = 'one'
        names[11] = 'eleven'
        names[2] = 'two'
        names[12] = 'twelve'
        names[20] = 'twenty'
        names[3] = 'three'
        names[13] = 'thirteen'
        names[30] = 'thirty'
        names[4] = 'four'
        names[14] = 'fourteen'
        names[40] = 'forty'
        names[5] = 'five'
        names[15] = 'fifteen'
        names[50] = 'fifty'
        names[6] = 'six'
        names[16] = 'sixteen'
        names[60] = 'sixty'
        names[7] = 'seven'
        names[17] = 'seventeen'
        names[70] = 'seventy'
        names[8] = 'eight'
        names[18] = 'eighteen'
        names[80] = 'eighty'
        names[9] = 'nine'
        names[19] = 'nineteen'
        names[90] = 'ninety'
        if number in names:
            result = names[number]
        else:
            tens = number // 10;
            ones = number - tens * 10
            result = names[tens * 10] + '-' + names[ones]
        return result
    
    
    print(number_to_string(int(input())))