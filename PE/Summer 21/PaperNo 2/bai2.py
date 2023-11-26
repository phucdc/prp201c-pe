import re

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'Trace.txt'
            inFile = open(filename, 'r') # cursor
            lines = inFile.readlines() # [dong1, dong2, ..., dong n]
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

if __name__ == '__main__':
    troubleshot = {}
    # dictionary
    # dict = {key1:value1, key2:value2, ... keyn:valuen}
    '''
    name = microsoft
    name not in dict -> dict[name] = 1
    ...
    name = microsoft
    name in dict -> dict[name] += 1
    '''
    lines = getLines()
    for line in lines:
        fields = re.split(r'\s+', line)
        if fields[0] == 'Name:':
            provider = fields[1].split('-')[0]
            if provider not in troubleshot:
                troubleshot[provider] = 1
            else:
                troubleshot[provider] += 1
    print('Troubleshot wired LAN related issues:')
    for provider in sorted(troubleshot.keys()):
        print('%s: %d' % (provider, troubleshot[provider]))