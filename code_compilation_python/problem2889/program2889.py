    # This is codeforces 399
    # B. Red and Blue Balls
    
    
def is_all_stack_red(stack):
        for item in stack:
            if item != 'R':
                return False
        return True
    
def find_first_blue(stack):
        for i in xrange(len(stack)):
            if stack[i] == 'B':
                return i
        return None
    
def checkio(stack):
        counter = 0
        while not is_all_stack_red(stack):
            first_blue = find_first_blue(stack)
            for i in xrange(first_blue):
                stack[i] = 'B'
            stack[first_blue] = 'R'
            counter+=1
        return counter
    
    while True:
        num = input()
        stack_str = input()
        stack = list(stack_str)
        return checkio(stack)