def program1223():
    ﻿d1=input()
    d2=input()
    
    if d1=='monday':
      if d2=='monday' or d2=='wednesday' or d2=='thursday':
        print('YES')
      else:
        print('NO')
    if d1=='tuesday':
      if d2=='tuesday' or d2=='thursday' or d2=='friday':
        print('YES')
      else:
        print('NO')
    if d1=='wednesday':
      if d2=='wednesday' or d2=='friday' or d2=='saturday':
        print('YES')
      else:
        print('NO')
    if d1=='thursday':
      if d2=='thursday' or d2=='saturday' or d2=='sunday':
        print('YES')
      else:
        print('NO')
    if d1=='friday':
      if d2=='friday' or d2=='sunday' or d2=='monday':
        print('YES')
      else:
        print('NO')
    if d1=='saturday':
      if d2=='saturday' or d2=='monday' or d2=='tuesday':
        print('YES')
      else:
        print('NO')
    if d1=='sunday':
      if d2=='sunday' or d2=='tuesday' or d2=='wednesday':
        print('YES')
      else:
        print('NO')