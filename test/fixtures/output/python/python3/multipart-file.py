import http.client
import gzip

conn = http.client.HTTPConnection("mockbin.com")

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"foo\"; filename=\"hello.txt\"\r\nContent-Type: text/plain\r\n\r\n\r\n-----011000010111000001101001--\r\n"

headers = { "content-type": "multipart/form-data; boundary=---011000010111000001101001" }

conn.request("POST", "/har", payload, headers)

res = conn.getresponse()
data = res.read()

if res.headers['content-encoding'] == 'gzip':
    print(gzip.decompress(data).decode("utf-8"))
else:
    print(data.decode("utf-8"))
