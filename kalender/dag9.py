inp = open("./kalender/dag9_test.txt","r")
#inp = open("./kalender/dag9.txt","r")
text= inp.read()
text = text.splitlines()
print(text)

for line in text:
    history = line.split(" ")
    print(history)
    
    nye = []
    status = True
    # enumerate jakob. enumerate. amoguss også
    while history.count("0")==len(history):
        for i, value1 in enumerate(history):
            
            print(value1)
            
            if i < len(history)-1:
                value2 = history[i+1]
                dif = int(value2)-int(value1)
                print(dif)
                nye.append(dif)
                if dif > 0:
                    status = False
            print("Nye: ",nye)
            history = nye
        if status == False:
            print("Fortsette")
    print(history)
        
    #print(nye)

"""
        nye2 = []
        status = True
        for i in range(len(nye)):
        
            print(nye[i])
        
            if i < len(nye)-1:
                dif = int(nye[i+1])-int(nye[i])
                print(dif)
                nye2.append(dif)
                if dif > 0:
                    status = False
            print("Nye2: ",nye2)
            if nye2[-1] == 0:
                nye2.append(nye2[-1])
            print("TEST: ",nye2)

    if status == False:
        print("Fortsette")
"""