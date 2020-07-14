# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
    if (street < 8):
        return 0
    elif (street >= 8):
        d = street % 8
        e = street // 8
        if (d == 0):
            return e * 8
        if (d >= 1 and d <= 4):
            return e * 8
        else:
            return (e * 8) + 8
