import ssl, smtplib                                                         #寄出email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
sender = "lee708@gmail.com"                                                 #寄件者
msg["From"] = sender                                                    
msg["To"] = "lee708@me.com"                                                 #收件者
msg["Subject"] = Header("Test send email","utf-8").encode()                 #主旨

body = "this is email from python-3"                                        #內文
msg_content = MIMEText(body)
msg.attach(msg_content)
c = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:            #gmail通訊設定(host,port,)
    server.login(sender,"fhvy uoei mprk cnnh")                              #後為Gmail應用程式密碼
    server.sendmail(sender,"lee708@me.com",msg.as_string())                 #前為寄件者，後為收件者
print("End")