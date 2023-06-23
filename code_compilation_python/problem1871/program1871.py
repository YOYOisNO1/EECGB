def program1871():
    A , B = input().spilt();
    a, b = map(int, [A, B]);
    c = a + 1;
    while ''.join (ch for ch in str(c) if ch in '47') != B:
        c += 1;
    print(c);