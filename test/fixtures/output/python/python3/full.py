import http.client
import gzip

conn = http.client.HTTPConnection("mockbin.com")

payload = "foo=bar"

headers = {
    "cookie": "foo=bar; bar=baz",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
}

conn.request("POST", "/har?foo=bar&foo=baz&baz=abc&key=value", payload, headers)

res = conn.getresponse()
data = res.read()

if res.headers['content-encoding'] == 'gzip':
    print(gzip.decompress(data).decode("utf-8"))
else:
    print(data.decode("utf-8"))
