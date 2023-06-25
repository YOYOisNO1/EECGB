    import sys
    
def seek(x, terms, sums, index):
      if x == 0 or sums[index] == x:
        print('YES')
        sys.exit()
      if sums[index] < abs(x):
        return
      if x > 0:
        seek(x-terms[index], terms, sums, index-1)
      else:
        seek(x+terms[index], terms, sums, index-1)
      seek(x, terms, sums, index-1)
    
    base, x = map(int, input().split())
    terms = [1]
    sums = [1]
    while terms[-1] < x:
      terms.append(base * terms[-1])
      sums.append(sums[-1] + terms[-1])
    seek(x, terms, sums, len(terms)-1)
    print('NO')
    