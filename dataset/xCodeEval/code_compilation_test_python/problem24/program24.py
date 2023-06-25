    FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven","eight", "nine"]
    SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
    OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]
    HUNDRED = "hundred"
    
    s = int(input())
    
def checkio(number):
        l = len(str(number))
        k = 10 ** (l-1)
        if l == 0 or number == 0:
            return ""
        elif l == 1:
            return FIRST_TEN[number-1]
        elif l == 2:
            if number >=10 and number < 20:
                return SECOND_TEN[number-10]
            else:
                a = number // k - 2
                s = "-" if number%k > 0 else ""
                return OTHER_TENS[a] + s + checkio(number%k)
        elif l == 3:
            a = number // k # first number
            s = "-" if number%k > 0 else ""
            return FIRST_TEN[a-1] + "-" + HUNDRED + s + checkio(number%k)
    
    
    
    print(checkio(s))