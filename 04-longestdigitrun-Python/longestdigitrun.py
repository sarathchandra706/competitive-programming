# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
  if n <0:
      n = -n
  l = list(map(int,str(n)))
  dict = {}
  c = 1
  for i in range(len(l)-1):
      if l[i] == l[i+1]:
          c = 0
          if l[i] in dict:
              dict[l[i]] = dict[l[i]]+1
          else:
              dict[l[i]] = 1
              
  if c == 1:
      l.sort()
      return l[0]
  dic = {}
  f = sorted(dict.keys())
  for i in f:
      dic[i] = dict[i]
  dic = sorted(dic.items(),key = lambda item:item[1], reverse = True)
  return dic[0][0]