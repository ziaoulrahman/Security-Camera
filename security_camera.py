from time import sleep
from gpiozero import MotionSensor
from picamera import PiCamera
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
 	print("gotcha")
        sleep(0.1)
        camera = PiCamera()
        camera.start_preview()
        sleep(2)
        camera.capture("/tmp/picture.jpg")
        camera.stop_preview()
        email_user = 'sales@exentech.net'
        email_password = 'Exen1234'
        email_send = 'coskun.ersahin@exentech.net','ahmetozer@exentech.net'

        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Python!'
        msg.attach(MIMEText(body,'plain'))

        filename='picture.jpg'
        attachment  = open('/tmp/picture.jpg','rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.yandex.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()

        
