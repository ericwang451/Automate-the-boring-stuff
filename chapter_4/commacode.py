spam = ['apples', 'bananas', 'tofu', 'cats']
cheese = []
hotDog = ['people']
doge = [['hi people', 'holai'], ['baby']]

def commacode(list):
    if len(list) == 0:
        print("list is empty")
    elif len(list) == 1:
        print(list[0])
    else:
        line = ""
        for i in range(len(list)-1):
            line += str(list[i]) + ", "
        print(line),
        print(str(list[i+1]) + ".")
    
def main():
    commacode(spam)
    commacode(cheese)
    commacode(hotDog)
    commacode(doge)

main()
