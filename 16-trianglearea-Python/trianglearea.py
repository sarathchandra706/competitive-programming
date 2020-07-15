# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

import math
def trianglearea(s1, s2, s3):
  p = (s1 + s2 + s3)/3
  a = math.sqrt(p(p-s1)(p-s2)(p-s3))
  return abs(a)

