import re

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'mbox-short.txt'
            inFile = open(filename, 'r') # cursor
            lines = inFile.readlines() # [dong1, dong2, ..., dong n]
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

lines = getLines()
s = 0.0
cnt = 0
for line in lines:
    if re.split(r'\s+', line)[0] == 'X-DSPAM-Confidence:':
        s += float(re.split(r'\s+', line)[1])
        cnt += 1

print('Average spam confidence: %.17f' % (s/cnt))