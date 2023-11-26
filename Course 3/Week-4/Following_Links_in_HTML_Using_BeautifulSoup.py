import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# In my case, i was asked for repeat the process 7 times, with name at position 18 (they count from 1, so it actually 17 in list)
cnt = 7
pos = 17
url = "http://py4e-data.dr-chuck.net/known_by_Lynn.html"
while cnt > 0:
    # Send request
    html = urllib.request.urlopen(url, context=ctx).read()
    # Parse the response
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Set url = href value of the 17th anchor tag
    url = tags[pos].get('href', None)
    cnt-=1
# Just print out the result
print(url) 