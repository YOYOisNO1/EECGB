def program3428():
    u , v = map(int, input().split())
    s1 = input()
    s2 = input()
    result = s1[0] + s2[-1] + s1[-1] + s2[0]
    print('YES' if result in ('>v<^','<^>v') else 'NO')