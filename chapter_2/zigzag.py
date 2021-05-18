import sys,time

try:
    while True:
        for i in range(6):
            line = ' ' * i + '*'*8 
            print(line)
            time.sleep(0.1)
        for i in range(6,0,-1):
            line = ' ' * i + '*'*8
            print(line)
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()

