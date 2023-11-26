import requests
import re

#request to the link, get data file content
urlData = "http://py4e-data.dr-chuck.net/regex_sum_1249553.txt"
req = requests.get(urlData)

#just simple, re.findall to find all integer numbers with \d+ then sum them all 
print(sum(int(n) for n in re.findall("\d+", req.text)))