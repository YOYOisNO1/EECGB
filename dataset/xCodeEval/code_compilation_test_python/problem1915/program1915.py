    P = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
def main():
       n = input()
       s = input()
       D = {}
       
       for i in xrange(n):
          if s[i] == '.': continue
          D[i] = s[i]
       
       #print D
       if n == 7:
          for i in xrange(8):
             if len(P[i]) != n: continue
             for l in D:
                r = False 
                if D[l] != P[i][l]: 
                   r = True
                   break
             if r: continue
             break
       
       if n == 6: ans = P[3]
       elif n == 8: ans = P[8]
       else: ans = P[i]
       print ans
       
       
    if __name__ == '__main__':
       main()