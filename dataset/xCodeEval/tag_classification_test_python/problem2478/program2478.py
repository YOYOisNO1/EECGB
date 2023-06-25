def main():
         n = input()
         s = input()
         i = 0
         Out = []
         In = []
         while i < n:
              if s[i] == '(':
                   i += 1
                   begin = i
                   while s[i] != ')':
                        i += 1
                   In.append(s[begin:i])
              i += 1
         #print(In)
         for i in xrange(len(In)):
              s = s.replace('(' + In[i]+')', '_')
         Out = s.split('_')
         ans_max = 0
         for i in xrange(len(Out)):
              ans_max = max(ans_max, len(Out[i]))
         inner = ''
         for i in xrange(len(In)):
              inner += In[i] + '_'
         count = 0
         A = inner.strip('_').split('_')
         for i in xrange(len(A)):
              if A[i] != '':
                   count += 1
         print(ans_max,) count
    if __name__ == '__main__':
         main()