# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
       def swapPairs(self, cur):
              if not cur:
                     return cur
              next = cur.next
              if next:
                     cur.val, next.val = next.val, cur.val
                     self.swapPairs(next.next)
              return cur
