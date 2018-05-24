import sys

stackMax = []
stackVal = []
output   = []
index    = 0

def actionPop():
    global index
    if index > 0:
        index -= 1
        stackMax.pop()
        return stackVal.pop()
    else:
        return False
    
def actionMax():
    if index > 0:
        return stackMax[index - 1]
    else:
        return False

def actionPush(value):
    global index
    data = value.split(' ')
    if data[0] != 'push':
        return False

    value= int(data[1])
    cnt  = len(stackMax)

    if cnt > 0:
        val = max(stackMax[cnt -1], value)
    else:
        val = value

    index += 1
    stackMax.append(val)
    stackVal.append(value)

def printOutput():
    for val in output:
        print(val)

def execCommand(command):
    if command == 'pop':
        actionPop()
    elif command == 'max':
        val = actionMax()
        if val:
            output.append(val)
    else:
        actionPush(command)

ii = 0
countOperations = int(sys.stdin.readline().strip())

while ii < countOperations:
    execCommand(sys.stdin.readline().strip())
    ii+=1

printOutput()