#!/usr/bin/env python3
print("Content-type: text/html")
print()
print('<html>')
print('<body>')
print('<form enctype="multipart/form-data" action="save_file.py" method="post">')
print('<p>File: <input type="file" name="filename" /></p>')
print('<p><input type="submit" value="Download" /></p>')
print('</form>')
print('</body>')
print('</html>')
