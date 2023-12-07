inp = open("dag4.txt","r")
text= inp.read()

text = text.splitlines()
total = 0
for i in range(len(text)):
    card = text[i].split(":")[1]
    card = card.split("|")

    win = []
    right = 0
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
            win = card2

        elif case == False:

            for k in range(len(card2)):
                if card2[k] in win:
                    right += 1
    print(right)

    if right > 1:       
        score = 2**(right - 1)
    elif right == 1:
        score = 1
    elif right == 0:
        score = 0


    print(score)
    total += score

print(total)