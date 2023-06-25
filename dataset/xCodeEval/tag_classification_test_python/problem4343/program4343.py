def program4343():
    a=int(input())
    d=input()
    finalists=[]
    for veri in d.split(' '):
      finalists.append(int(veri))
    print(max(max(finalists)-25,0))