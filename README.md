# Multipule-SSH-Connection-Block
A python Script to Block duplicate SSH Connection

block.py
NOTE:

      Here is a .py script for those who wanna Disconnect more than one connection from a user, even with /false or /nologin SHELL.
 
      When set your SSH port change the code (Here is 8888)
      
      This code lock the user and if you want to unlock use this:
      # sudo usermod --unlock "username"
      
      This script make a log file of username, PIDs of sshd service and IP addresses of source at /var/log/user_block.log
      

###################################################################################
user.py

Create user with password you wanna set (note here is 123456)

set 30 days exp. for password
set /bin/false as shell for user
