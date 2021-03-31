class Solution:
       def minSteps(self, s, t):
              from collections import Counter
              cs, ct = Counter(s), Counter(t)
              ans = 0
              s = str(set(s))
              for x in s:
                     ans += max(0, cs[x]-ct[x]);
              return ans