def program2990():
    A, B, C, N = map(int, input().split())
     
    if C > A or C > B:
      print(-1)
      exit()
    else:
      A-=C
      B-=C
      
    pass_students = A+B+C
    if pass_students < N:
      print(N-pass_stidents)
      exit()
      return N - pass_students
    else:
      print(-1)