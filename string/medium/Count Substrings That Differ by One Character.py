class Solution:
       def countSubstrings(self, s, t):
              from queue import Queue
              ans = 0
              for i in range(len(s)):
                     for j in range(len(t)):
                            ti, tj = i, j
                            b = 0
                            while ti < len(s) and tj < len(t) and b < 2:
                                   b += s[ti] != t[tj]
                                   ans += b == 1
                                   ti += 1
                                   tj += 1
              return ans