# Parsing an URL
import urllib.parse # not just urllib

url = 'https://ex.com:80/path/to?a=b#x'
parsed = urllib.parse.urlparse(url)

print('Scheme:', parsed.scheme)

print('Host:', parsed.hostname)
print('Port:', parsed.port)

print('Path:', parsed.path)
print('Query:', parsed.query)
print('Fragment:', parsed.fragment)
