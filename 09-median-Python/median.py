# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
    l = len(a)
    if l == 0:
        return None
    elif l >=1:
        q = sum(a)/l
    return q
