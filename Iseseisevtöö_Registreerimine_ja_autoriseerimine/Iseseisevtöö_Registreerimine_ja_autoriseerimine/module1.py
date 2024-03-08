import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "seva.tsarev@gmail.com"
to_email = "marina.oleinik@tthk.ee"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

subject = "Привет от Питона!"  # Задаем тему письма
body = "Tere tulemast!"  # Задаем тело письма

# Создаем объект сообщения MIMEMultipart
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = to_email
message["Subject"] = subject

# Добавляем тело письма в объект сообщения
message.attach(MIMEText(body, "plain"))

# Преобразуем объект сообщения в строку
msg = message.as_string()

# Пытаемся подключиться к серверу и отправить письмо
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, to_email, msg)
except Exception as e:
    # Выводим любые сообщения об ошибках
    print(e)
finally:
    server.quit()