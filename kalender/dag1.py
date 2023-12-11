inp = open("./kalender/dag1.txt","r")
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

x = 0
for i, row in enumerate(text): 
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

        
    print(firstNumber, lastNumber)
    s = firstNumber + lastNumber
    print(x)
    
    x += int(s)
    
print(x)

#print(text)
    

