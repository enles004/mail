import os
from dotenv import load_dotenv

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("USERNAME_MAIL")
pass_email = os.getenv("PASS")

print(sender_email)