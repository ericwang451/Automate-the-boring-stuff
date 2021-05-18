import random
def generate():
    list = []
    for i in range(100):
        number = random.randint(0,1)
        if (number == 0):
            list.append('H')
        else:
            list.append('T')
    return list

def checkStreak(list, streak):
    counter = 0
    instancesOfStreak = 0
    while (counter<(len(list)-1)):
        i = 0
        while (i<streak and counter<(len(list)-1)):
            if (list[counter] == list[counter+1]):
                i+=1
                counter+=1
            else:
                counter+=1
                i=0
        if (i==streak):
            instancesOfStreak+=1
    return instancesOfStreak

def main():
    total = 0
    TOTAL_TESTS = 10000
    for i in range(TOTAL_TESTS):
        list = generate()
        if (checkStreak(list, 6)>1):
            total +=1
    percentage = total / TOTAL_TESTS
    print(total)
    print(TOTAL_TESTS)
    print(percentage)
    return percentage

print("Chance of streak of 6 in 100 coin flips, 10,000 times over is: %s%%" %str(main()))