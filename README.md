# Nmap-Scanner-Python

The target IP address is first requested from the user in this revised version utilizing the input() function. The target ip variable holds this value.

The nmap is then initialized after that.

Using the target ip variable as the hosts argument and the arguments argument to give the nmap options, we use the scan() method to scan the target IP address.

Next, after iterating over the scan findings, we use a loop to print all the pertinent data for each host and port. In this version of the script, we run a SYN scan using the -sS option and version detection using the -sV option.
