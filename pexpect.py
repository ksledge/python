import paramiko, time

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('10.254.0.89', username= 'ksledge', password = 'cisco', look_for_keys= False, allow_agent= False)
new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output) 

new_connection.send("show version")
time.sleep(3)
output = new_connection.recv(5000)
print(output)
new_connection.close()