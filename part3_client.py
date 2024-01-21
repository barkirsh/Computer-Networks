import socket
import sys


def udp_client(serverIP, serverPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        domain = input("Enter a domain (or 'exit' to quit): ")

        if domain.lower() == 'exit':
            break

        # Encode the domain string into bytes
        domain_bytes = domain.encode('utf-8')

        s.sendto(domain_bytes, (serverIP, serverPort))
        data, addr = s.recvfrom(1024)
        print("Server response:", data.decode('utf-8'))

    s.close()


if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("Usage: python part3_client.py <server_ip> <server_port>")
        sys.exit(1)

    serverIP = sys.argv[1]
    serverPort = int(sys.argv[2])
    udp_client(serverIP, serverPort)
