import sys

stackMax = []
stackVal = []
output   = []
index    = 0

def actionPop():
    global index, stackMax, stackVal
    if index > 0:
        index -= 1
        result = stackVal[index]
        del stackMax[index]
        del stackVal[index]
    else:
        return False
    
def actionMax():
    global index, stackMax, stackVal
    if index > 0:
        val = stackMax[index - 1]
        output.append(val)
        return val
    else:
        return False

def actionPush(value):
    global index, stackMax, stackVal
    data = value.split(' ')
    if data[0] != 'push':
        return False

    value = int(data[1])

    if index > 0:
        val = max(stackMax[index -1], value)
    else:
        val = value

    index += 1
    stackMax.append(val)
    stackVal.append(value)

    return True

def printOutput():
    for val in output:
        print(val)

def execCommand(command):
    if command == 'pop':
        actionPop()
    elif command == 'max':
        actionMax()
    else:
        actionPush(command)

# ii = 0
# countOperations = int(sys.stdin.readline().strip())

# while ii < countOperations:
#     execCommand(sys.stdin.readline().strip())
#     ii+=1

operations = [
    'push 5',
    'pop',
    'push 3',
    'max'
]

for commnad in operations:
    execCommand(commnad)

printOutput()