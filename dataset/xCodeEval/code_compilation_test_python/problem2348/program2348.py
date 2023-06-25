def program2348():
    a = input()
    result = input()
    b = ''
    toPrint = True
    for i in range(len(result)):
      if result[i] <= a[i]:
        b += result[i]
      else:
        print('-1')
        toPrint = False
    	break
    if toPrint:
      print(b)