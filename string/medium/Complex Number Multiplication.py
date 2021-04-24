class Solution:
       def complexNumberMultiply(self, a: str, b: str) -> str:
              # a = 'a1+a2i'
              # b = 'b1+b2i'

              a1, a2 = a.split('+')
              a1 = int(a1)
              a2 = int(a2.split('i')[0])
              b1, b2 = b.split('+')
              b1 = int(b1)
              b2 = int(b2.split('i')[0])

              return f'{a1*b1-a2*b2}+{a1*b2+a2*b1}i'
