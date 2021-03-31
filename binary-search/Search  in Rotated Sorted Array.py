class Solution:
       def search(self, a, t):
              nol = len(a)
              for i in range(1, len(a)):
                     if a[i] < a[i-1]:
                            nol = i
                            break
              l, r = 0, nol-1
              while l <= r:
                     mid = (l+r)>>1
                     if a[mid] == t:
                            return mid
                     if a[mid] < t:
                            l = mid+1
                     else:
                            r = mid-1
              l, r = nol, len(a)-1
              while l <= r:
                     mid = (l+r)>>1
                     if a[mid] == t:
                            return mid
                     if a[mid] < t:
                            l = mid+1
                     else:
                            r = mid-1
              return -1