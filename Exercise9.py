number = 5
for row in range(number):
    for column in range(number-row):
        print(' ', end='')
    for space in range(2 * row+1):
        print('*', end='')
    print('')