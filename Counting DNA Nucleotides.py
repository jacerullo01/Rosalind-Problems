def countDNANucleaotides(s):
    aCount = 0
    cCount = 0
    gCount = 0
    tCount = 0
    for char in s:
        if char == 'a':
            aCount+= 1
        elif char == 'c':
            cCount += 1
        elif char == 'g':
            gCount += 1
        else:
            tCount += 1
