#inp = open("dag4.txt","r")
inp = open("dag4_test.txt","r")
text= inp.read()

text = text.splitlines()
total = 0
num = 0
cache = [1,1,1,1,1,1,1,1,1,1]

for i in range(len(text)):
    num += 1
    card = text[i].split(":")[1]
    card = card.split("|")

    win = []
    right = 0
    
    print("Card: ", num)
    for j in range(len(card)):
        
        if (j % 2) == 0:
            case = True
        
        else:
            case = False
        
        card2 = card[j].split(" ")
        
        

        while("" in card2): 
            card2.remove("")        
        
        #print(card2)

        if case == True:
            win = card2

        elif case == False:

            for k in range(len(card2)):
                if card2[k] in win:
                    right += 1
            
            if right > 9:
                right = 9
            for b in range(0,cache[0]):
                #print("test")
                for o in range(0,right):
                #if cache[0] > 1:
                #    cache[o+1] += cache[0]
                #else:
                    cache[o+1] += 1
            print("Antall rette denne runden: ",right)
            print("Ny cache", cache)
        
            total += cache[0]
            print("Total så langt: ", total)
        
            del cache[0]
            cache.append(1)
            print("Reset cache", cache)
    print("\n")
    
print(total)