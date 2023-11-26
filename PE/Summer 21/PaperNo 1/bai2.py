# regex
import re

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'DNSList.txt'
            inFile = open(filename, 'r')
            lines = inFile.readlines()
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

if __name__ == '__main__':
    locations = {}
    # dict = {[key1:value1], [key2:value2], [key3:value3], [key4:1]}
    # dict[key1] = value1
    # dict[key2] = value2

    # dict[key4] = 1
    # add new key with value in dict:
    #       dict[new_key] = value_of_new_key
    lines = getLines() # ['dong 1', 'dong2', ... , 'dong n']

    for line in lines:
        fields = re.split('\s+', line) # \s = 1 space; field = ['<:', '']
        if fields[0] == 'Location:':
            if fields[1] not in locations: # sthg not in dict <=> there is no key of dict equal to sthg
                locations[fields[1]] = 1
            else:
                locations[fields[1]] += 1

    print('DNS Server list:')
    print('%10s%10s' % ('Country', 'Count'))
    for key in sorted(locations.keys()): # dict.keys() => [key1, key2, key3]
        print('%10s%10d' % (key, locations[key]))
