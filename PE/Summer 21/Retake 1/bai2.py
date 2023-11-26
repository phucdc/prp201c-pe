import re

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'Student.txt'
            inFile = open(filename, 'r') # cursor
            lines = inFile.readlines() # [dong1, dong2, ..., dong n]
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

lines = getLines()
courses = {}
for line in lines:
    course = re.split(r'\s+', line)[0]
    if course == 'Course':
        continue
    if course not in courses:
        courses[course] = 1
    else:
        courses[course] += 1

print('Course summary:')
print('%10s %10s' % ('Course', 'Count'))
for course in sorted(courses.keys()):
    print('%10s %10d' % (course, courses[course]))