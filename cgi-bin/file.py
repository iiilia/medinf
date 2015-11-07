import requests
#!/usr/bin/env python3

print("Content-type: text/html")
print ("<body>downloading with requests<\body>")
r = requests.get("C://server//cgi-bin//hello.py")
