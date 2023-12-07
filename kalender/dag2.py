inp = open("dag2.txt","r")
text= inp.read()

text = text.splitlines()

x = 0

red = 12
green = 13
blue = 14
gameN = 0

for i in range(len(text)):
    gameN += 1
    game = text[i].split(":")[1]
    game = game.split(";")

    mRed = 0
    mGreen = 0
    mBlue = 0
    
    valid = True
    print(game)
    for j in range(len(game)):
        color = game[j].split(",")
       
        for k in range(len(color)): 
            color2 = color[k].split(" ")
            n = int(color2[1])
            c = color2[2]
            
            if c == "red":
                if n > mRed:
                    mRed = n
            elif c == "green":
                if n > mGreen:
                    mGreen = n
            elif c == "blue":
                if n > mBlue:
                    mBlue = n

    print(mBlue)
        #print(color2)


    gamepower = mRed*mBlue*mGreen

        #print(gamepower)

    x += gamepower


print(x)