    from sys import stdin
    
def solve(y,queue):
      vec=''
      for t in range(y):
        k=(len(queue)-1)
        while(k>0):
          if queue[k]=='G'and queue[k-1]=='B':
            queue[k-1]='G'
            queue[k]='B'
            k-=1
          k-=1
      for i in range (len(queue)):
        vec=vec+str(queue[i])
      return (vec)
    
def main():
      x,y=stdin.readline().strip().split()
      queue=stdin.readline().strip()
      print(solve(int(y),list(queue)))
    main()