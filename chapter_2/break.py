import sys

while True:
    print('Please type your name: \n')
    name = input()
    if name == 'Eric':
        break

    if name == 'exit':
        print('You are about to exit this program')
        sys.exit()
print('thank you!')