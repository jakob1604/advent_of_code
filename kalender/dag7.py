inp = open("./kalender/dag7_test.txt","r")
text= inp.read()
text = text.splitlines()
#print(text)

for i in range(len(text)):
    hand = text[i].split(" ")
    print("Hand: ", hand)

    def check(x):
        lik = 0
        for b in range(len(hand)):
            print("B: ", b)
            print("X: ", x)
            print("Hand(x): ", hand[0][x])
            print("Hand(b): ", hand[0][b])
            if hand[x] == hand[b]:

                lik += 1
        return lik
    #for j in range(len(hand[0])):
        
    print(check(0))
    #print(check(1))
    #print(check(2))