def program1260():
    s = input()
    n = len(s)
    state = "CODEFORCES"
    for i in range(n):
      if state == "" break
      if s[i] == state[0]:
        state = state[1:]
      else :
        m = len(state)
        if state in s[-m:]:
          state = ""
          break
        else :
          break
    
    if state == "": print("YES")
    else : print("NO")