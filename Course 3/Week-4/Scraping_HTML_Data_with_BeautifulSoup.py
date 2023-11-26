# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# or pip install beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Send request and Parse the Response
url = "http://py4e-data.dr-chuck.net/comments_1249555.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# All number are in <span></span>, so just get the value
tags = soup('span')
# The tag.contents[0] is the number, just print(tag.contents[0]) and see
# Get the sum of those numbers
print(sum(int(tag.contents[0]) for tag in tags))
