import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# creating and starting the smtp server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

# get the password from the details file
with open('details.txt', 'r') as f:
    password = f.read()
server.login('meetkshah01@gmail.com', password)

# creating the message by specifying the fields
msg = MIMEMultipart()
msg['From'] = 'meetkshah01@gmail.com'
msg['To'] = 'classicguru01@gmail.com'
msg['Subject'] = 'My Test 00'
with open('message.txt', 'r') as f:
    message = f.read()
msg.attach(MIMEText(message, 'plain'))

# image adding aas payload and encoding it
image = 'image.jpg'
attachment = open(image, 'rb')
p = MIMEBase('application', 'octet_stram')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename = {image}')
msg.attach(p)

text = msg.as_string()
server.sendmail('meetkshah01@gmail.com', 'classicguru01@gmail.com', text)



