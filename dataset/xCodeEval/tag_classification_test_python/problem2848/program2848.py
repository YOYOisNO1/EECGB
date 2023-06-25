def program2848():
    let=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    x=input()
    y=input()
    z=''
    q=0
    for i in range(len(x)):
      if let.index(x[i])==let.index(y[i]):
          z+=x[i]
      elif let.index(x[i])>let.index(y[i]):
        z+=y[i]
      else:
        q=1
        break
    if q==0:
      print(z)
    else:
      print('-1')