def main():
      n, k = input().split()
      k = int(k)
      if len(n) <= k or n == '0':
        print(len(n)) - 1
        return
      
      n = n[::-1]
      #print(n,) k
      numeros_sacados = 0
      ceros = 0
      for dig in n:
        if ceros == k:
          print(numeros_sacados)
          return
        if dig == '0':
          ceros += 1
        else:
          numeros_sacados += 1
      print(len(n)) - 1
      return
        
      
    main()