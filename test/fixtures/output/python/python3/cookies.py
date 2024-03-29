import http.client
import gzip

conn = http.client.HTTPConnection("mockbin.com")

headers = { "cookie": "foo=bar; bar=baz" }

conn.request("POST", "/har", headers=headers)

res = conn.getresponse()
data = res.read()

if res.headers['content-encoding'] == 'gzip':
    print(gzip.decompress(data).decode("utf-8"))
else:
    print(data.decode("utf-8"))
