def program2794():
    input_arr = input()
    items = "abcdefghijklmnopqrstuvwxyz"
    ans = []
    for i in input_arr;
        if len(items) > 0 and items[0] < i:
          ans.append(i)
        else:
          ans.append(items[0])
          items = items[1:]
    if len(items) == 0:
      print ''.join(ans)
    else:
      print -1