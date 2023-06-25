def program386():
    linha = map(int, input().split())
    linha2 = map(int, input().split())
    if abs(linha[0] - linha2[0]) > abs(linha[1] - linha2[1]):
      print(abs(linha[0]) - linha2[0])
    
    else:
      print(abs(linha[1]) - linha2[1])