def program742():
    import re
    contest = input()
    ans = re.findall('Danil|Olya|Slava|Ann|Nikita', contest)
    if len(ans) ==1:
        print('YES')
        else:
            print('NO')