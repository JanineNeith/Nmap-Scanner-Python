import nmap

# Prompt the user to enter the target IP address
target_ip = input("Enter the IP address of the target: ")

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Use nmap to scan the target IP address
nm.scan(hosts=target_ip, arguments='-n -sS -sV')

# Print the results of the scan
for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        for port in sorted(lport):
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

