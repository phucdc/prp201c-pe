import random

def intinput():
     while True:
          try:
               # 2 dices -> min = 2, max = 12
               result = int(input('Enter an integer number of total: '))
               if result < 2 or result > 12:
                    print('You must enter an integer from 2 to 12!')
                    continue
               return result
          except:
               print('You must enter an integer number!')
               
total = intinput()
cnt = 0
while True:
     dice1 = random.randint(1, 6)
     dice2 = random.randint(1, 6)
     cnt += 1
     print(f'Result of throw: {cnt} {dice1} + {dice2}')
     if dice1 + dice2 == total:
          break
print(f'You got your total in {cnt} throws')