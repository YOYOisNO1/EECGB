def program951():
    import string
    s = input().lower()
    ans = ''
    for i in s:
        if i not in 'aeiou':
            ans +=('.'+i)
    print ans