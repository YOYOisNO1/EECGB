def program2151():
    x=input()
    x.strip("0")
    for i in range(len(x)):
         if (x[i]!=x[-i-1]):
              return "NO"
         return"YES"