import http.client
import gzip

conn = http.client.HTTPConnection("mockbin.com")

conn.request("GET", "/har?foo%5Bbar%5D=baz%2Czap&fiz=buz&key=value")

res = conn.getresponse()
data = res.read()

if res.headers['content-encoding'] == 'gzip':
    print(gzip.decompress(data).decode("utf-8"))
else:
    print(data.decode("utf-8"))
