def checkInput():
    while True:
        try:
            num = int(input('Enter number: '))
            if num < 0:
                print('Number must be positive.')
                pass
            else:
                return num
        except ValueError:
            print('Number must be a positive number.')

num = checkInput()
if num < 8:
    print('There is no perfect cube number from 0 to %d:' % (num))
else:
    i = 2
    print('The perfect cubes from 0 to %d:' % (num))
    while (i**3 <= num):
        print(i**3, end = ' ')
        i += 1
