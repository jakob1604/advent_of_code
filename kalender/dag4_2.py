inp = open("./kalender/dag4.txt","r")
#inp = open("./kalender/dag4_test.txt","r")
cards= inp.read()

cards = cards.splitlines()
totalScorecards = 0
cardNum = 0
# hhæh?
cache = [1,1,1,1,1,1,1,1,1,1,1]

for i in range(len(cards)):
    cardNum += 1
    # [[winning numbers], [your numbers]]
    card = cards[i].split(":")[1].split("|")
    print(f"card: {card}")

    win = []
    winningNumbers = 0
    
    print("Card: ", cardNum)
    for j in range(len(card)):
        
        if (j % 2) == 0:
            case = True
        
        else:
            case = False
        
        card2 = card[j].split(" ")
        

        while("" in card2): 
            card2.remove("")        
        
        print(card2)

        if case == True:
            # add winning cards
            win = card2

        elif case == False:

            for k in range(len(card2)):
                if card2[k] in win:
                    winningNumbers += 1
            
            if winningNumbers > 10:
                winningNumbers = 10
            for b in range(0,cache[0]):
                #print("test")
                for o in range(0,winningNumbers):
                #if cache[0] > 1:
                #    cache[o+1] += cache[0]
                #else:
                    cache[o+1] += 1
            print("Antall rette denne runden: ",winningNumbers)
            print("Ny cache", cache)


            totalScorecards += cache[0]
            print("Total så langt: ", totalScorecards)
        
            del cache[0]
            cache.append(1)
            print("Reset cache", cache)
    print("\n")
    
print(totalScorecards)