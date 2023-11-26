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

def isPerfect(num):
    s = 0
    for i in range(1, num): #range(x,y) <=> [x;y)
        if num % i == 0:
            s += i
    return s == num

# Main
if __name__ == '__main__':
    num = checkInput()
    if num < 6:
        print('There is no perfect number from 0 to %d' % (num))
    else:
        print('The perfect numbers from 0 to %d:' % (num))
        for i in range(6, num + 1): # [6, num + 1) <=> [6, num]
            if isPerfect(i):
                print(i, end = ' ') # end = "\n", sep = "\n"