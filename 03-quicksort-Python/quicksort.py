"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
  s = []
  b = []
  e = []
  if len(array) > 1:
      p = array[0]
      for i in array:
          if i < p :
              s.append(i)
          elif i > p:
              b.append(i)
          else:
              e.append(i)
      return sorted(s)+e+sorted(b)
  else:
      return array