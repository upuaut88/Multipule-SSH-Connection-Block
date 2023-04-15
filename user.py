import subprocess
import datetime

# Prompt the user for the username
username = input("Enter username: ")

# Set the password
password = "123456"

# Calculate the expiration date (30 days from now)
expiration_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

# Use subprocess to run the 'adduser' command with the '--shell' option to set the shell to /bin/false
subprocess.run(["adduser", "--disabled-password", "--shell", "/bin/false", username])

# Use subprocess to run the 'chpasswd' command to set the password
subprocess.run(["echo", f"{username}:{password}"], stdout=subprocess.PIPE)
subprocess.run(["chpasswd"], input=f"{username}:{password}", universal_newlines=True)

# Use subprocess to run the 'chage' command to set the expiration date
subprocess.run(["chage", "-E", expiration_date, username])

