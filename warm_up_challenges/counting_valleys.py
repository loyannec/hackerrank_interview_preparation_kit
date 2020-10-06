def countingValleys(steps, path):

    valleys = 0
    altitude = 0

    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1
        else:
            altitude -= 1

    return valleys

#print(countingValleys(8, 'UDDDUDUU'))
#print(countingValleys(12, 'DDUUDDUDUUUD'))
print(countingValleys(8, 'UDUDUDUD'))