import math

def intinput(mess):
     while True:
          try:
               result = int(input(mess))
               if result < 0:
                    print('You must enter a positive integer.')
                    continue
               return result
          except:
               print('Please enter an integer number.')

x = intinput('Enter the first number: ')
y = intinput('Enter the second number: ')

# Trường lồn dùng python <3.4 nên không có math.lcm và math.gcd :)))
# print(f'The least common multiple of {x} and {y}: {math.lcm(x, y)}')
# print(f'The greatest common divisor of {x} and {y}: {math.gcd(x, y)}')
