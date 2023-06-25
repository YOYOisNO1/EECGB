def program226():
    stones = [0 for i in range(14)]
    
    stones = map(int, input().split())
    
    finalsitrep = [[0 for j in range(14)] for i in range(14)]
    
    for start in range(14):
           stillleft = stones[start]
           leftover = 14 - start - 1
           if(leftover>=stillleft):
                  for k in range(start+1, start+stillleft+1):
                         finalsitrep[start][k]=stones[k] + 1
                  finalsitrep[start][start] = 0
                  for k in range(start):
                         finalsitrep[start][k] = stones[k]
           else:
                  stillleft = stillleft - leftover
                  for k in range(start+1, 14):
                         finalsitrep[start][k]=stones[k] + 1
                  finalsitrep[start][start] = 0
                  for k in range(start):
                         finalsitrep[start][k] = stones[k]
                  numincr = stillleft/14
                  for k in range(14):
                         finalsitrep[start][k]+=numincr
                  finalleft = stillleft%14
                  for k in range(finalleft):
                         finalsitrep[start][k]+=1
    
    finalans = 0
    for sitrep in finalsitrep:
           anstemp = 0
           for entry in sitrep:
                  if entry%2==0 and entry!=0:
                         anstemp+=entry
           if(anstemp > finalans):
                  finalans = anstemp
    print(finalans)