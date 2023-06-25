def program818():
    n=int(input())
    c=['R','O','Y','G','B','I','V']
    ans=c[:]
    n-=7
    while(n>0):
      s=set(c[:])
      s.remove(ans[-1])
      s.remove(ans[-2])
      s.remove(ans[-3])
      s.remove('R')
      s.remove('O')
      s.remove('Y')
      ans.append(s.pop())
      n-=1
    print(''.join(ans))