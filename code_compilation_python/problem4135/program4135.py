    # http://codeforces.com/contest/623/problem/A
    
    import math
    
    nm = input()
    nm = nm.split(' ')
    n = int(nm[0])
    m = int(nm[1])
    
    edges = [[False for i in range(n)] for x in range(n)]   # False: no such edge
    nodes = [[True for i in range(3)] for x in range(n)]    # True: possible
    
    # read edges
    for i in range(m):
      ab = input()
      ab = ab.split(' ')
      a = int(ab[0]) - 1
      b = int(ab[1]) - 1
      edges[a][b] = True
      #print 'add edge:',a,b
    
def hasEdge(a,b):
      if edges[a][b] or edges[b][a]:
        return True
      else:
        return False
    
    # True if has deduction
def deduce(n1,n2):
      # if has edge, same
      if hasEdge(n1,n2) and certain(n1):
        val_1 = get(n1)
        # n1 is 'a', n2 isn't 'c'
        if val_1 == 0:
          nodes[n2][2] = False
          #print 'node',n2,'is a'
          return True
        # n1 is 'c', n2 isn't 'a'
        if val_1 == 2:
          nodes[n2][0] = False
          #print 'node',n2,'is a'
          return True
      # if no edge, different
      elif not hasEdge(n1,n2) and certain(n1):
        val_1 = get(n1)
        if val_1 == 0:
          nodes[n2][0] = False
          #print 'node',n2,'is c'
          return True
        if val_1 == 2:
          nodes[n2][2] = False
          #print 'node',n2,'is a'
          return True
      return False
          
def deductions():
      for i in range(n):
        for j in range(n):
          if i != j:
            deduce(i,j)
          
    # only has one possibility
def certain(k):
      if (nodes[k][0] + nodes[k][1] + nodes[k][2]) == 1:
        return True
      return False
      
def freeNode(k):
      if (nodes[k][0] + nodes[k][1] + nodes[k][2]) == 3:
        return True
      return False
      
def isDeadNode(k):
      if (nodes[k][0] + nodes[k][1] + nodes[k][2]) == 0:
        return True
      return False
    
    # get the node first possible node, not certain
def get(k):
      if nodes[k][0]:
        return 0
      if nodes[k][1]:
        return 1
      if nodes[k][2]:
        return 2
    
def incompleteSolution():
      for k in range(n):
        if not certain(k):
          return k
      return False
    
def genSolution():
      tmp = incompleteSolution()
      # loop if node id returned
      while isinstance(tmp, int):
        deductions()
        tmp = incompleteSolution()
      
def printSolution():
      ss = []
      for i in range(n):
        theChar = get(i)
        if theChar == 0:
          theChar = 'a'
        elif theChar == 1:
          theChar = 'b'
        else:
          theChar = 'c'
        ss.append(theChar)
      print ''.join(ss)
    
    # main
    # no edge, no b
    complete = True
    firstMissingEdge = []
    for i in range(n):
      for j in range(n):
        if (i != j) and not hasEdge(i,j):
          #print 'no edge: ',i,j
          if complete:
            complete = False
            firstMissingEdge.append(i)
            firstMissingEdge.append(j)
          #print 'missing edge',i,j
          # must not b
          nodes[i][1] = False
          nodes[j][1] = False
    
    # if free node => is b
    for i in range(n):
      if freeNode(i):
        nodes[i][0] = False
        nodes[i][2] = False
        #print 'node',i,'is \'b\''
          
    # complete graph
    if complete:
      ss = []
      for i in range(n):
        ss.append('b')
      print Yes
      print ''.join(ss)
    
    else:
      # 1. guess one node to be 'a'
      a = firstMissingEdge[0]
      b = firstMissingEdge[1]
      nodes[a][2] = False   # node[a] be 'a'
      nodes[b][0] = False   # node[b] be 'c'
      #print 'let node',a,'be a, node',b,'be c'
      # loop check, deduction...
      updated = True
      hasDeadNode = False
      while updated:
        updated = False
        for i in range(n):
          for j in range(n):
            if i != j:
              if deduce(i,j):
                updated = True
              if isDeadNode(j):
                hasDeadNode = True
                break
          if hasDeadNode:
            break
        if hasDeadNode:
          break
    
      if hasDeadNode:
        print 'No'
      else:
        print 'Yes'
      
      
    