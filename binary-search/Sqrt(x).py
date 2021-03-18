class Solution:
       def mySqrt(self, x):
              l, r = 0, x
              ans = 0
              while l <= r:
                     mid = (l+r)>>1
                     if mid*mid <= x:
                            ans = mid
                            l = mid+1
                     else:
                            r = mid-1
              return ans
