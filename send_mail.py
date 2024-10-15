import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

async def send_email(recipient_email):
  sender_email = "bot_brakodel@mail.ru"
  sender_password = "TpvgXUKshANCFBfVXGy3"
  subject = "Акт отбраковки товара"
  filename = "brak_act.xlsx"
  body = "Это письмо создано автоматически. Если вы не запрашивали его создание, или оно попало к вам случайно, просто удалите его"
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = recipient_email
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))
  attachment = MIMEBase('application', 'octet-stream')
  with open(filename, 'rb') as file:
    attachment.set_payload(file.read())
  encoders.encode_base64(attachment)
  attachment.add_header('Content-Disposition', 'attachment; filename={}'.format(filename))
  msg.attach(attachment)
  server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
  server.login(sender_email, sender_password)
  server.sendmail(sender_email, recipient_email, msg.as_string())
  server.quit()
