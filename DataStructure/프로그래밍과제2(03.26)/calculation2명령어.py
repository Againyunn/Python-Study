from calculation2 import calculator2

cal = calculator2()

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
    
    elif command[0] == 'cs':
        cal.changeSum()
    elif command[0] == 'MS':
        cal.memorySave()
    elif command[0] == 'MR':
        cal.memoryRead()
    elif command[0] == 'MC':
        cal.memoryClear()
    elif command[0] == 'M+':
        cal.memoryAdd()
    elif command[0] == 'M-':
        cal.memorySub()