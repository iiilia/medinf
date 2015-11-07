#!/usr/bin/python
def sent(filepath):
    from smtplib import SMTP_SSL
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email import Encoders
    import os
    
    #filepath = "/path/to/file"
    basename = os.path.basename(filepath)
    address = 'adr'
    address_to = "ivanicki-i@yandex.ru"
    
    # Compose attachment
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
    
    # Compose message
    msg = MIMEMultipart()
    msg['From'] = address
    msg['To'] = address_to
    msg.attach(part)
    
    # Send mail
    smtp = SMTP_SSL()
    smtp.connect('smtp.yandex.ru')
    smtp.login(address, 'password')
    smtp.sendmail(address, address_to, msg.as_string())
    smtp.quit()


import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('.//share//' + fn, 'wb').write(fileitem.file.read())

   message = 'Your file "' + fn + '" was uploaded successfully. Just wait the letter'
   
else:
   message = 'No file was uploaded'


print("Content-type: text/html")
print() 
print ('<html><body>   <p>%s</p></body></html>' % (message,))
