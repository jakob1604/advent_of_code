#inp = open("./kalender/dag7_test.txt","r")
inp = open("./kalender/dag7.txt","r")
text= inp.read()
text = text.splitlines()
#print(text)

col = []

for i in range(len(text)):
    hand = text[i].split(" ")
    #print("Hand: ", hand)

    antall_J = 0
    gammel_lik = 0
    fra_j = True
    for j in range(len(hand[0])):
        lik = 0
        
        #print("Subjekt ", hand[0][j])
        subjekt = hand[0][j]
        if subjekt == "J":
            antall_J += 1
            fra_j = False
        for b in range(len(hand[0])):
        #print("Hand(x): ", hand[0][x])
            #print("Komp: ", hand[0][b])
            komp = hand[0][b]
            if komp == subjekt:
                lik += 1
            
        if lik > gammel_lik:
            gammel_lik = lik

        #print("lik: ",lik)
        
    #print("Gammel lik: ",gammel_lik)
    #print("Antall J : ",antall_J)
    S = hand[0]
    a = ""
    for i in S:
        if i not in a:
            a += i
    uni = (len(a))
    if fra_j == False:
        uni = uni-1
    #print("Unike: ", uni)
    if antall_J < 3:
        gammel_lik = gammel_lik + antall_J
    ny = 0
    
    if antall_J == 3 and uni == 1:
        ny = 6
        
    elif antall_J == 2 and uni == 3:
        ny = 3
    
    elif antall_J == 4:
        ny = 6
    elif antall_J == 3 and uni == 2:
        ny = 5
    elif gammel_lik == 5:
        #print("fem like")
        ny = 6
    elif gammel_lik == 4:
        #print("fire like")
        ny = 5
    elif gammel_lik == 3 and uni == 2:
       # print("fullt hus")
        ny = 4
    elif gammel_lik == 3:
       # print("tre like")
        ny = 3
    elif gammel_lik == 2 and uni == 3:
       # print("to par")
        ny = 2
    elif gammel_lik == 2:
       # print("ett par")
        ny = 1
    
    hand.append(ny)
    #print(hand)
    col.append(hand)
    
#print(col)

# take second element for sort
def takeSecond(elem):
    return elem[2]
# sort list with key
col.sort(key=takeSecond)


    
#print(col)

def checkOrder(a,b):
    if a.isnumeric() == True:
        powerA = int(a)
    elif a == "A":
        powerA = 14
    elif a == "K":
        powerA = 13
    elif a == "Q":
        powerA = 12
    elif a == "J":
        powerA = 1
    elif a == "T":
        powerA = 10                                
    if b.isnumeric() == True:
        powerB = int(b)
    elif b == "A":
        powerB = 14
    elif b == "K":
        powerB = 13
    elif b == "Q":
        powerB = 12
    elif b == "J":
        powerB = 1
    elif b == "T":
        powerB = 10
    
    if powerA < powerB:
        order = True
    else:
        order = False
    return order

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

for i in range(0,1000):
    for g in range(len(col)):
        #print(col[g][2])
        if g < len(col)-1:
            if col[g][2] == col[g+1][2]:
                #print("Lik")
                #print(col[g][0][0])
                #print(col[g+1][0][0])
                if col[g][0][0] == col[g+1][0][0]:
                    #print("neste")
                    if col[g][0][1] == col[g+1][0][1]:
                        #print("neste2")
                        if col[g][0][2] == col[g+1][0][2]:
                            #print("neste3")
                            if col[g][0][3] == col[g+1][0][3]:
                                #print("neste4")
                                if col[g][0][4] == col[g+1][0][4]:
                                    print("De er identiske")
                                else:
                                    x = col[g][0][4]
                                    y = col[g+1][0][4]
                                    if checkOrder(x,y) == False:
                                
                                        pos1 = g
                                        pos2 = g+1
                                        swapPositions(col, pos1, pos2)
                                    
                            else:
                                x = col[g][0][3]
                                y = col[g+1][0][3]
                                if checkOrder(x,y) == False:
                                
                                    pos1 = g
                                    pos2 = g+1
                                    swapPositions(col, pos1, pos2)
                        else:
                            x = col[g][0][2]
                            y = col[g+1][0][2]
                            if checkOrder(x,y) == False:
                            
                                pos1 = g
                                pos2 = g+1
                                swapPositions(col, pos1, pos2)
                    else:
                        x = col[g][0][1]
                        y = col[g+1][0][1]
                        if checkOrder(x,y) == False:
                        
                            pos1 = g
                            pos2 = g+1
                            swapPositions(col, pos1, pos2)
                    
                else:
                    x = col[g][0][0]
                    y = col[g+1][0][0]
                    if checkOrder(x,y) == False:
                    
                        pos1 = g
                        pos2 = g+1
                        swapPositions(col, pos1, pos2)
                    
                


for h in range(len(col)):
    rank = h+1
    col[h].append(rank)
#print(col)

total = 0
for f in range(len(col)):
    win = int(col[f][1])*col[f][3]
    total += win
    print(col[f])
    print("win: ",win)

print(total)