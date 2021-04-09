class Solution:
       def arrangeWords(self, t: str) -> str:
              a = list(t.lower().split())
              a.sort(key = len)
              ans = ""
              temp = list(a[0])
              temp[0] = temp[0].upper()
              for x in temp:
                     ans += x
              for i in range(1, len(a)):
                     ans += ' '+a[i]
              return ans