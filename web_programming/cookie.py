import http.cookiejar
from re import L
from unicodedata import name
import urllib
import urllib.request

URL = input("Provide a URL: ")

def extract_info():
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    response = opener.open(URL)

    for cookie in cookie_jar:
        print("Cookie: %s --> %s" % (cookie.name, cookie.value))
    
    print("Headers: %s" % response.headers)

if __name__ == "__main__":
    extract_info()