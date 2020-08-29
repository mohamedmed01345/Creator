from random import randint, choice
numNum = int(input("How many nums BRO >> "))
Services = ["012","011","010"]
z = 0
while z < numNum :
    I = 0
    Service = choice(Services)
    numE = ""
    while I < 8:
        numF = str(randint(0,9))
        numE += numF
        I += 1
    FullNum = Service+numE
    print(FullNum)
    z += 1
    with open("nums.txt","a") as nums:
        nums.write(FullNum+"\n")
