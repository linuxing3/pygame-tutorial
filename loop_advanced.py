# Sample Python/Pygame Programs
# Excecise
# http://programarcadegames.com/index.php?chapter=back_to_looping


# helper functions to print list

# Function to convert
def list_to_string_loop(s):
    n = ''
    for ele in s:
        n += ele
    return n

# Python program to convert a list
# to string using join() function

# Function to convert


def lis_to_string_join(s):
    n = " "
    return (n.join(s))


def list_to_string_comprehension(list):
    n = ' '.join([str(elem) for elem in list])
    return(n)


def lis_to_string_map(list):
    n = ' '.join(map(str, list))
    return(n)


# self-taught
def print_array_complicated(list):
    n = ''
    for x in list:
        n += str(x) + ' '
    return(n)


def print_array_simple(list):
    for x in range(len(list)):
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
    row = lis_to_string_map(n)
    print(row)

# # q.10
print('----------------q 10-------------------')
for x in range(1, 10):
    n = []
    for y in range(1, 10):
        n.append(x * y)
    row = lis_to_string_map(n)
    print(row)


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
    row = lis_to_string_map(n + t[1: len(t)])
    print(row)

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

for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print(" ", end=" ")
    # Count up
    for j in range(1, 9-i):
        print(j, end=" ")
    # Count down
    for j in range(7-i, 0, -1):
        print(j, end=" ")
    print()

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
    row = lis_to_string_map(n + t[1: len(t)])
    print(row)
