def program1295():
    s = input().split('/')
    ans = [str('/') + i for i in s if i != '']
    print(''.join(ans) if ans else '/')