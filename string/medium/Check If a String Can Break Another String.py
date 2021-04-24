class Solution:
       def checkIfCanBreak(self, s1: str, s2: str) -> bool:
              s1 = sorted(list(s1))
              s2 = sorted(list(s2))
              if s1 > s2:
                     s1, s2 = s2, s1
              ans = True
              for i in range(len(s1)):
                     ans &= s1[i] <= s2[i]
              return ans
