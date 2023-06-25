def program1232():
    if __name__ == "__main__":
        n = int(input())
        numbers = list(map(int, input().split()))
        numbers.sort(reverse = True)
        num1 = numbers[0]
        div_num1 = set()
        for val in numbers:
            if num1 % val == 0:
                div_num1.add(val)
        
        for val in div_num1:
            numbers.remove(val)
        
        if len(numbers) == 0:
            num2 = num1
        else:
            numbers.sort(reverse = True)
            num2 = numbers[0]
        
        print(num1, num2)