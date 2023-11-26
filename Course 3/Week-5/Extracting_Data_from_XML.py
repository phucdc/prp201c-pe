import requests
import xml.etree.ElementTree as ET

'''
Structure of the XML tree, in this Excercise:
    <comments>
        <comment>
            <name>Cillin</name>
            <count>93</count>
        </comment>
        ....
    </comments>
So, to get the number, we need to get to comments/comment first (line 23), the length here is the number of comment tags
Now we just need to find out the count tag, get the numbers, and sum them! 
'''

url = 'http://py4e-data.dr-chuck.net/comments_1249557.xml'
data = requests.get(url)
# Get the tree structure
print(data.text)
tree = ET.fromstring(data.text)
# Go to the comment tag
results = tree.findall('comments/comment')
# Print out the results
print(len(results))
print(sum(float(result.find('count').text) for result in results))