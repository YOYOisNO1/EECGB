def program1211():
    from sys import stdin, stdout
    
    a, b = map(int, stdin.readline().split())
    cnt = 0
    cnt_a = a
    cnt_b = 0
    
    while cnt_a >= 1:
        cnt += cnt_a
        cnt_b += cnt_a
        cnt_a = cnt_b // b
        cnt_b = cnt_b % b
    
    stdout.write(f"{cnt}\n")