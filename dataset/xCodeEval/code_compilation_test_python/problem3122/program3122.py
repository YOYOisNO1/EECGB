def program3122():
    length = input("input:")
    string = input("input string:")
    string = string.split('0')
    result = "
    for i in string:
        result += str(len(i))
    print(int(result))