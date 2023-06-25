def program2758():
    gl, gr = map(int, input().split())
    bl, br = map(int, input().split())
    if (br >= gl-1 and br <= (gl+1)*2) or (bl >= gr-1 and bl <= (gr+1)*2):
      print('YES')
    else:
      print('NO')