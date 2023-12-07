inp = open("./kalender/dag6.txt","r")
text= inp.read()

text = text.splitlines()
#print(text)
time = [40,70,98,79]
distance = [215,1051,2147,1005]
x2 = 40709879
y2 = 215105121471005

x = 7
y = 9

total = 1

def calc(t,d):
    num = 0
    for i in range(t+1):
        dist = i*(t-i)
        #print(i)
        #print(dist)
        if dist > d:
            num += 1
    return num

for a in range(0,4):
    funk = calc(time[a],distance[a])
 #   print(funk)
    total = total * funk

#print(total)
#print(27*27*31*48)

t = 71530
d = 940200

print(calc(x2,y2))
