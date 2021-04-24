class Solution:
       def numSplits(self, s: str) -> int:
              rest = [0]*26
              for x in s:
                     rest[ord(x)-ord('a')] += 1
              firstPart = [0]*26
              ans = 0
              fPos = sPos = 0  # not to check every time positive elements
              for x in rest:
                     sPos += x > 0
              for i in s:
                     temp = ord(i)-ord('a')
                     firstPart[temp] += 1
                     rest[temp] -= 1
                     fPos += firstPart[temp] == 1
                     sPos -= rest[temp] <= 0
                     ans += fPos == sPos
              return ans
