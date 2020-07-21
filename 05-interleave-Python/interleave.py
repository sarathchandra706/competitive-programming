# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
    string = ""
    if len(s1) > len(s2):
        for i in range(len(s2)):
            string += s1[i] + s2[i]
        for j in range(len(s2),len(s1)):
            string += s1[j]
        return string
     
    elif len(s2) > len(s1):
        for p in range(len(s1)):
            string += s1[p] + s2[p]
        for q in range(len(s1),len(s2)):
            string += s2[q]     
        return string      
    else :   
        if (len(s1)== len(s2)):          
          for t in range(len(s1)):
            string += s1[t]+s2[t]
        return string