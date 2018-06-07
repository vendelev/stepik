import sys, math

kucha = []
output= []


def getLeftIndex(ii):
    return 2 * ii + 1


def getRigthIndex(ii):
    return 2 * ii + 2


def down(index):
    global kucha, output

    maxindex = index
    size = len(kucha)

    l = getLeftIndex(index)
    if l < size and kucha[l] < kucha[maxindex]:
        maxindex = l

    r = getRigthIndex(index)
    if r < size and kucha[r] < kucha[maxindex]:
        maxindex = r

    if index != maxindex:
        output.append([index, maxindex])
        tmp = kucha[maxindex]
        kucha[maxindex] = kucha[index]
        kucha[index] = tmp

        down(maxindex)

def run(data):
    global kucha, output

    kucha = list(map(int, data.split(' ')))
    size  = len(kucha)
    index = math.trunc(size / 2)

    while index >= 0:
        down(index)
        index -= 1

    print(len(output))

    for index, value in enumerate(output):
        print(value[0], value[1])

sys.stdin.readline().strip()
run(sys.stdin.readline().strip())

# run('5 4 3 2 1')
# run('7 6 5 4 3 2')

run('19 14 12 3 20 2 5 8 4 11 13 9 16 15 1 7 6 17 10 18')
# 20
# 19 14 12 3 20 2 5 8 4 11 13 9 16 15 1 7 6 17 10 18
#
# Answer:
# 12
# 7 16
# 6 14
# 4 9
# 2 6
# 1 3
# 0 2
# 9 19
# 6 14
# 3 8
# 2 5
# 8 18
# 5 11

# run('9 14 2 12 6 19 1 7 5 13 8 4 3 11 17 16 18 15 10 20')
# 20
# 9 14 2 12 6 19 1 7 5 13 8 4 3 11 17 16 18 15 10 20
#
# Answer:
# 8
# 5 12
# 3 8
# 2 6
# 1 3
# 0 2
# 8 18
# 3 7
# 2 6

# run('5 20 8 7 13 17 10 19 16 18 2 9 4 1 14 15 6 12 11 3')
# 20
# 5 20 8 7 13 17 10 19 16 18 2 9 4 1 14 15 6 12 11 3
#
# Answer:
# 13
# 9 19
# 8 18
# 7 16
# 6 13
# 5 12
# 4 10
# 3 7
# 2 6
# 1 4
# 0 2
# 4 9
# 2 5
# 9 19

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 20
# 18 10 13 1 7 9 5 2 15 8 3 4 11 16 20 19 17 14 6 12
#
# Answer:
# 11
# 8 18
# 5 11
# 4 10
# 2 5
# 1 3
# 0 1
# 5 11
# 3 7
# 1 3
# 3 8
# 8 17
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 20
# 4 12 7 14 19 5 11 20 9 10 16 15 2 1 6 3 8 17 18 13
#
# Answer:
# 13
# 7 15
# 6 13
# 5 12
# 4 9
# 3 7
# 2 6
# 1 3
# 0 2
# 9 19
# 7 16
# 6 14
# 3 7
# 2 5