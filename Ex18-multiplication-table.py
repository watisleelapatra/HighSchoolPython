#Generate multiplication table
i, j = 1, 2
while i <= 12:
    while j <= 12:
        print ("{: >3} ".format(i*j), end = '')
        j = j + 1
    print()
    j = 2
    i = i + 1