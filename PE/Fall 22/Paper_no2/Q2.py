filename = input('Enter file: ').strip()
if not filename:
     filename = 'Text.txt'
try:
     f = open(filename)  
     larr = f.readline()
     arr = [x.strip() for x in larr.split(',')]
     print(f'The original list from file is: {arr}')   
     result = []
     for i in range(len(arr)):
          for j in range(i + 1, len(arr)):
               result.append(int(arr[i] + arr[j]))
     print(f'All numbers combinations: {result}')
     f.close()
except Exception as e:
     print(e)