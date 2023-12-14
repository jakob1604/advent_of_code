inp = open("./kalender/dag1.txt","r")
#inp = open("./kalender/test1.txt","r")
text= inp.read()

writtenNumbers = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
numbers = "123456789"
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
print(len(text))
rowz = 0

x = 0
for i, row in enumerate(text): 
    rowz += 1
    firstIndex = 1000
    lastIndex = -1
    firstNumber = None
    lastNumber = None


    for writtenNumber, number in writtenNumbers.items():
        numberIndex = row.find(writtenNumber)

        if numberIndex == -1:
            continue
        if numberIndex < firstIndex:
            firstIndex = numberIndex
            firstNumber = number
        if numberIndex > lastIndex:
            lastIndex = numberIndex
            lastNumber = number


    for n in numbers:
        numberIndex = row.find(n)

        if numberIndex == -1:
            continue
        if numberIndex < firstIndex:
            firstIndex = numberIndex
            firstNumber = n
        if numberIndex > lastIndex:
            lastIndex = numberIndex
            lastNumber = n

    for writtenNumber, number in writtenNumbers.items():
        numberIndex = row.rfind(writtenNumber)

        if numberIndex == -1:
            continue
        if numberIndex < firstIndex:
            firstIndex = numberIndex
            firstNumber = number
        if numberIndex > lastIndex:
            lastIndex = numberIndex
            lastNumber = number


    for n in numbers:
        numberIndex = row.rfind(n)

        if numberIndex == -1:
            continue
        if numberIndex < firstIndex:
            firstIndex = numberIndex
            firstNumber = n
        if numberIndex > lastIndex:
            lastIndex = numberIndex
            lastNumber = n


    #print(row)
    #print(firstNumber, lastNumber)
    s = firstNumber + lastNumber
    #print("add: ",s)
    #print("total: ",x)
    
    x += int(s)
print(rowz)
print(x)

#print(text)
    

