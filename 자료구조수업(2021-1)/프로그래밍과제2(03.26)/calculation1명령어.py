from calculation1 import calculator1

cal = calculator1()

while True:
    command=list(input().split())

    if command[0] == 'add':
        cal.add(int(command[1]))
    elif command[0] == 'sub':
        cal.sub(int(command[1]))
    elif command[0] == 'mpy':
        cal.mpy(int(command[1]))
    elif command[0] == 'div':
        cal.div(int(command[1]))
    elif command[0] == 'sub':
        cal.mod(int(command[1]))
    
    elif command[0] == 'currentValue':
        print(cal.getValue())
    elif command[0] == 'setValue':
        cal.setValue(int(command[1]))
    elif command[0] == 'clear':
        cal.self()
    elif command[0] == 'quit':
        break
