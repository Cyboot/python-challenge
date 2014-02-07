# http://www.pythonchallenge.com/pc/def/equality.html
# Solution: linkedlist


file = open("text.txt", "r")
lines = file.read().splitlines()

def left(x,y):
    line = lines[y]
    if line[max(x-4,0)].isupper():
        return False
    else:
        return line[max(x-3,0):x].isupper()

def right(x,y):
    line = lines[y]
    if line[min(x+4,len(line)-1)].isupper():
        return False
    else:
        return line[x+1:min(x+4,len(line))].isupper()

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        char = lines[y][x]
        if char.isupper():
            continue
        if left(x,y) and right(x,y):
            print(char)
        
file.close()
