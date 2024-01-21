import socket

def udp_client(serverIP, serverPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        domain = input("")
        s.sendto(domain, (serverIP, serverPort))
        data, addr = s.recvfrom(1024)
        print(str(data))
    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    serverIP = sys.argv[1]
    serverPort = int(sys.argv[2])
    udp_client(serverIP, serverPort)