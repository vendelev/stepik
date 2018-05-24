import sys

stack = []
output= []

def actionPop():
    if len(stack) > 0:
        stack.pop()
    
def actionMax():
    print(stack)

def actionPush(value):
    data = value.split(' ')
    stack.append(int(data[1]))

countOperations = int(sys.stdin.readline())

ii = 0
while ii < countOperations:
    command = sys.stdin.readline().strip()

    if command == 'pop':
        actionPop()
    elif command == 'max':
        actionMax()
    else:
        actionPush(command)
    
    ii+=1

for val in output:
    print(val)