def program3638():
    sec = int(input()[2:])
    word = input()
    for i in range(sec):
        word = word.replace('BG', 'GB')
    print((word))