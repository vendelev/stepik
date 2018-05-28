import sys

stack1 = []
index1 = -1

stack2 = []
index2 = -1


def pop():
    global index1, index2

    if index2 == -1:
        while index1 >= 0:
            index1 -= 1
            index2 += 1
            value = stack1.pop()
            add_item(stack2, index2, value['item'])

    if index2 > -1:
        index2 -= 1
        return stack2.pop()
    else:
        return False


def push(value):
    global index1

    index1 += 1
    add_item(stack1, index1, int(value))


def add_item(stack, index, value):
    if index > 0:
        maxi = max(stack[index-1]['max'], value)
    else:
        maxi = value

    stack.append({'item': value, 'max': maxi})


def print_max():
    global index1, index2

    if index1 >= 0 and index2 >= 0:
        print(max(stack1[index1]['max'], stack2[index2]['max']))
    else:
        if index1 >= 0:
            print(stack1[index1]['max'])
        else:
            print(stack2[index2]['max'])


def run(data, window):
    cnt = 0
    window = int(window)
    for index, value in enumerate(data):
        cnt += 1
        push(value)

        if cnt == window:
            print_max()

        if cnt > window:
            pop()
            print_max()


sys.stdin.readline().strip()
run(sys.stdin.readline().strip().split(' '), sys.stdin.readline().strip())


# run('2 7 3 1 5 2 6 2'.split(' '), 4)
# run('2 1 5'.split(' '), 1)
# run('2 3 9'.split(' '), 3)
