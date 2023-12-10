inp = open("./kalender/dag10_test.txt","r")
#inp = open("./kalender/dag10.txt","r")
text= inp.read()
text = text.splitlines()
print(text)
#print(text[0][1])
for rowIndex, row in enumerate(text):
    for row, node in enumerate(row):
        #print(node)
        if node == "S":
            sCol = row
            sRow = rowIndex
            print(sCol,sRow)

print("south",text[sRow+1][sCol])
print("north",text[sRow-1][sCol])
print("east",text[sRow][sCol+1])
print("west",text[sRow][sCol-1])

def getNabour(x,y):
    nab = []
    if x > 0:
        nab.append(text[x-1][y])
    if x < len(text[x]):
        nab.append(text[x+1][y])
    if y > 0:
        nab.append(text[x][y-1])
    if y < len(text[x]):
        nab.append(text[x][y+1])
    return nab
print(getNabour(sCol,sRow))