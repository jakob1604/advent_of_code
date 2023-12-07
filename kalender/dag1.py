inp = open("dag1.txt","r")
text= inp.read()

numbers = {["one","1"],["two","2"],[],[],[]}
#text = text.replace("one","1")
#text = text.replace("two","2")
#text = text.replace("three","3")
#text = text.replace("four","4")
#text = text.replace("five","5")
#text = text.replace("six","6")
#text = text.replace("seven","7")
#text = text.replace("eight","8")
#text = text.replace("nine","9")

text = text.splitlines()

x = 0
for i in range(len(text)): 
    y = ""
    for j in range(len(text[i])):
        if text[i][j].isnumeric() == True:
            #print(text[i][j])
            y += text[i][j]
    f = y[0]
    s = y[-1]
    ny=f+s
    x += int(ny)
    
print(x)

#print(text)
    

