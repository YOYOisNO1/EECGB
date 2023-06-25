def program2666():
    st=str(input())
    a=['ABC','ACB','BAC','BCA','CBA','CAB']
    ans=0
    for i in range(0,6):
      if a[i] in st:
        ans=1
    if ans==1:
      print("yes")
    else:
      print("no")