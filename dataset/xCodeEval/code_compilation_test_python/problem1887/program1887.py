def program1887():
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')
    a,b = inp.read(3).split(' ')
    out.write(str(int(a) ^ int(b)))
    out.close()
    inp.close()