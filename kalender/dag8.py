#inp = open("./kalender/dag8_test.txt","r")
inp = open("./kalender/day8.txt","r")
text= inp.read()
text = text.splitlines()
#print(text)
Tdict = {}
instruct = []
for i in range(len(text)):
    part = text[i].split(" ")
    print(part)
    if i == 0:
        instruct = part[0]
    if i > 1:
        Tdict[part[0]] = [part[2][1:-1],part[3][:-1]]
    print(part)

print(instruct)
print(Tdict)

location = "AAA"
step = 0
while location != "ZZZ":
    for j in range(len(instruct)):
        print(instruct[j])
        if instruct[j] == "L":
            location = Tdict[location][0]
        else:
            location = Tdict[location][1]
        print(location)
        step += 1

print(step)