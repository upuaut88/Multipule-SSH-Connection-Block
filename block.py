import os
import subprocess
import datetime

# Step 1: Run the first command and get the list of user IDs and process IDs
ps_output = subprocess.check_output("ps -aux | awk '$1 != \"root\" && $11 ~ /sshd:/ ' | awk '{print $1,$2}' | sort", shell=True)
ps_output = ps_output.decode().strip().split("\n")
user_pids = [line.split() for line in ps_output]

# Step 2: Run the second command and get the list of connections on port 8888 for the SSH users
pid_list = subprocess.check_output("ps -aux | awk '$1 != \"root\" && $11 ~ /sshd:/ ' | awk '{print $2}' | sort | uniq -d", shell=True)
pid_list = pid_list.decode().strip().split("\n")
ss_output = subprocess.check_output("ss -tnp | awk -v pid=\"{}\" '$0 ~ pid && $0 ~ /:8888/'".format(" ".join(pid_list)), shell=True)
ss_output = ss_output.decode().strip().split("\n")

# Step 3: Lock the users and log the results
log_file = "/var/log/user_block.log"
time_banner = "#" * 22 + " {} ".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "#" * 22 + "\n"

for user in set([p[0] for p in user_pids]):
    pids = [p[1] for p in user_pids if p[0] == user]
    os.system("usermod --lock {}".format(user))
    with open(log_file, "a") as f:
        f.write(time_banner)
        f.write("User: {}\n".format(user))
        f.write("PIDs: {}\n".format(", ".join(pids)))
        f.write("IP Address (ss command output):\n")
        for line in ss_output:
            if any(pid in line for pid in pids):
                f.write(line + "\n")
        f.write("\n")

