# 0 1 1 2 3 5 8 ....

def fibonacci(n):
    result = [0] * (n + 1)
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result

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
print('The Fibonacci sequence of %d:' % (num))
print(*fibonacci(num)[:num], sep = ' ')