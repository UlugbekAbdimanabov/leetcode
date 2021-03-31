class Solution:
       def minFlips(self, s):
              ans = 0
              now = '1'
              for x in s:
                     if now == x:
                            now = '0' if x == '1' else '1'
                            ans += 1;
              return ans