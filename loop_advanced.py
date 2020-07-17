# Sample Python/Pygame Programs
# Excecise
# http://programarcadegames.com/index.php?chapter=back_to_looping


# helper functions to print list


def print_array(array):
    n = ''
    for x in range(len(array)):
        n += str(array[x]) + ' '
    print(n)


def print_array_simple(array):
    for x in range(len(array)):
        print(x, end=' ')
    print()


# Questions/Quiz

# # q.7.
print('---------------q7--------------------')
for row in range(10):
    for column in range(10):
        print(row, end=" ")

    # Print a blank line to move to the next row
    print()


for x in range(10):
    n = str(x) + " "
    print(n * 10)

# q.8
print('---------------q8--------------------')

for row in range(10):
    for column in range(row+1):
        print(column, end=" ")

    # Print a blank line
    # to move to the next row
    print()


for x in range(10):
    n = ''
    for y in range(x + 1):
        n += str(y) + ' '
    print(n)

# q.9
print('---------------q9--------------------')
# q.9.1
print('---------------q9.1 std -------------')

for row in range(10):
    # print spaces in empty rows
    for j in range(row):
        print(" ", end=" ")

    for j in range(10-row):
        print(j, end=" ")

    print()


for x in range(10):
    n = ''
    for y in range(10 - x):
        n += str(y) + ' '
    print(n)

print('---------------q9.1-------------------')

for x in range(10):
    n = ''
    for y in range(10 - x):
        n += str(y) + ' '
    n = ' ' * x + n
    print(n)

# q.9.2
print('---------------q9.2--------------------')
for x in range(10):
    n = ''
    for y in range(10 - x):
        n += str(y) + ' '
    n = ' ' * 2 * x + n
    print(n)

# q.10
print('-----------------------------------')
for x in range(10):
    n = []
    for y in range(10):
        n.append(10 * x + y)
    print_array(n)

# # q.10
print('----------------q 10-------------------')
for x in range(1, 10):
    n = []
    for y in range(1, 10):
        n.append(x * y)
    print_array(n)


for i in range(1, 10):
    for j in range(1, 10):
        # Extra space?
        if i*j < 10:
            print(" ", end="")

        print(i*j, end=" ")

    # Move down to the next row
    print()

# q.11
print('-------------q 11----------------------')

for x in range(10):
    n = []
    t = []
    for y in range(10):
        if y != 0 and y < x or y != 0 and y == x:
            n.append(y)
            t.insert(0, y)
        else:
            n.insert(0, ' ')
            t.append(' ')
    print_array(n + t[1: len(t)])

print('-------------q 11 std------------------')
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i+1):
        print(j, end=" ")
    # Count down
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

# q.12
print('-------------q 12----------------------')

for x in range(10):
    n = []
    t = []
    for y in range(10):
        if y != 0 and y < (9 - x):
            n.append(y)
            t.insert(0, y)
        else:
            n.insert(0, ' ')
            t.append(' ')
    print_array(n + t[1: len(t)])
