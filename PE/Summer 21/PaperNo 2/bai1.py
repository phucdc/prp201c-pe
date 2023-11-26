def prime(n):
    if n <= 1:
        return
    result = []
    check = [True] * (n + 1)
    for i in range(2, n + 1):
        if check[i] == True:
            result.append(i)
            for j in range(2 * i, n + 1, i):
                check[j] = False
    return result

def checkInput():
    while True:
        try:
            num = int(input('Enter a integer positive number: '))
            if num < 0:
                print('Number must be positive.')
                pass
            else:
                return num
        except ValueError:
            print('Number must be a positive number.')

if __name__ == '__main__':
    num = checkInput()
    if num < 2:
        print('There is no prime number from 0 to %d' % (num))
    else:
        print('The prime numbers from 0 to %d:' % (num))
        print(*prime(num), sep = " ")