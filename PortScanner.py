# Use socket to scan for open ports on host machine with multiple threads
import socket
import threading

# Scan for open ports on host machine, with multiple threads and impliment a timeout
def scan(port, timeout, output, service):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        output[port] = 'OPEN'
        # try to find service name and add to output
        try:
            service[port] = socket.getservbyport(port, 'tcp')
        except:
            try:
                service[port] = socket.getservbyport(port, 'udp')
            except:
                service[port] = 'unknown'

    except:
        output[port] = ''

# main
def main():

    # Define host
    global host
    host_name = input("Enter host to scan: ")
    host = socket.gethostbyname(host_name)
    # Print host
    print(host_name + ": " + host)
    # Start threading
    threads = []
    output = {}
    service = {}

    # Define timout in seconds
    timeout = int(input("Enter timeout in seconds: "))

    # Spawn threads
    for port in range(65536):
        t = threading.Thread(target=scan, args=(port, timeout, output, service))
        threads.append(t)

    # Start threads
    for i in range(65536):
        threads[i].start()

    # Join threads
    for i in range(65536):
        threads[i].join()

    # Print output
    for i in range(65535):
        if output[i] == 'OPEN':
            print(str(i) + ': ' + output[i])
            try:
                print('Service: ' + service[i])
            except:
                print('Service: ' + 'Unknown')

# Run main
if __name__ == '__main__':
    main()
