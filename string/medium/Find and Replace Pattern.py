class Solution:
       def findAndReplacePattern(self, words, pattern):
              from itertools import zip_longest
              ans = []
              for x in words:
                     mp, pm = dict(), dict()
                     takeIt = True
                     for (i, j) in zip_longest(x, pattern):
                            if i not in mp:
                                   mp[i] = j
                            if j not in pm:
                                   pm[j] = i
                            if mp[i] != j or pm[j] != i:
                                   takeIt = False
                                   break
                     if takeIt:
                            ans.append(x)
              return ans