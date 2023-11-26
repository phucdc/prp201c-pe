import math

def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def checkInput():
    while True:
        try:
            num = int(input('Enter a integer positive number: '))
            if num < 0:
                print('Number must be positive.')
                pass # continue;
            else:
                return num
        except ValueError:
            print('Number must be a positive number.')

if __name__ == '__main__':
    num = checkInput()
    if num < 2:
        print('There is no prime number from 0 to %d' % (num)) 
        # printf("%d", num); <=> print('%d' % (num))
    else:
        print('The prime numbers from 0 to %d:' % (num))
        for i in range(2, num + 1):
            if isPrime(i):
                print(i, end = ' ')