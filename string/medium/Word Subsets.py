class Solution:
       def wordSubsets(self, A, B):
              cnt = [0]*26
              for x in B:
                     temp = self.countLetters(x)
                     for i in range(26):
                            cnt[i] = max(cnt[i], temp[i])
              ans = []
              for x in A:
                     temp = self.countLetters(x)
                     takeIt = True
                     for i in range(26):
                            takeIt &= temp[i] >= cnt[i]
                     if takeIt:
                            ans.append(x)
              return ans
       
       def countLetters(self, x):
              temp = [0]*26
              for i in x:
                     temp[ord(i)-ord('a')] += 1
              return temp
