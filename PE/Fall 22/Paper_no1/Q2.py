filename = input('Enter file: ').strip()
if not filename: 
     filename = 'Text.txt'
try:
     f = open('Text.txt')
     larr = f.readline()
     arr = [x.strip() for x in larr.split(',')]
     print(f'The original list is: {arr}')
     arr1 = [x for x in arr if int(x) > 0]
     print(f'List after removing negative numbers: {arr1}')
     f.close()
except Exception as e:
     print(e)