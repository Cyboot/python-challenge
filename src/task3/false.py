file = open("text.txt", "r")
lines = file.read().splitlines()

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        char = lines[y][x].upper()
        
        if y > 0:
            charUP = lines[y - 1][x]
        else:
            charUP = " "
        if y < len(lines) - 1:
            charDOWN = lines[y + 1][x]
        else:
            charUP = " "
        if x > 0:
            charLEFT = lines[y][x - 1]
        else:
            charLEFT = " "
        if x < len(lines[y]) - 1:
            charRIGHT = lines[y][x + 1]
        else:
            charRIGHT = " "
        
        string = charUP + charDOWN + charLEFT + charRIGHT
        string.upper()
        
        if string.count(char) == 3:
            print(str(y) + ":" + str(x) + " ->" + char)

file.close()
