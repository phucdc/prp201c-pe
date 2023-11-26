#Merccire prime
def primes(n, lim):
    if n <= 1:
        return
    result = []
    check = [True] * (n + 1)
    for i in range(2, n + 1):
        if check[i] == True:
            result.append(i)
            if len(result) == lim:
                break
            for j in range(2 * i, n + 1, i):
                check[j] = False
    return result

def lucas_lehmer(p):
    m = (1 << p) - 1
    s = 4
    for i in range(p - 2):
        s = (s * s - 2) % m
    return s == 0 and m or 0

def checkInput():
    while True:
        num = input('Enter number: ')
        try:
            n = int(num)
            if n < 0:
                print('Number must be positive.')
                pass
            else:
                return num
        except ValueError:
            print('Number must be a positive number.')

num = checkInput()
n = int(num)
if n < 6:
    print('There are no perfect numbers lower than 6.')
else:
    print('The perfect numbers from 0 to %d:' % (n))
    print(6, end = ' ')
    for p in primes(n, len(num)):
        m = lucas_lehmer(p)
        if m:
            r = m << (p - 1)
            if r <= n:
                print(r, end = ' ')