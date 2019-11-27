import http
import urllib.request



req = urllib.request.Request(
    url="http://192.168.1.14:8080/status",
    method="GET"
)

with urllib.request.urlopen(req) as resp:
    response_content = resp.read().decode("utf8")

if "off" in response_content:
    print ("Off")

print ("hello")