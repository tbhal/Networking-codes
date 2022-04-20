import urllib.error
from urllib.request import urlopen

try:
    urlopen('http://www.ietf.org/rfc/rfc.txt') # here enter the site that we want to check
except urllib.error.HTTPError as e:
    print('Exception', e)
    print('Status', e.code)
    print('reason', e.reason)
    print('url', e.url)
