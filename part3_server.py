import socket
import sys


def load_ip_mapping(file_path):
    ip_mapping = {}
    with open(file_path, 'r') as file:
        for line in file:
            domain, ip = line.strip().split(',')
            ip_mapping[domain] = ip
    return ip_mapping


def udp_server(ip_mapping, my_host='0.0.0.0', my_port=12345, parent_ip='localhost',
               parent_port=12346, ips_file_name='default_ips.txt'):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((my_host, my_port))  # Fix here: use my_host and my_port
    print(f"Server listening on {my_host}:{my_port}")

    while True:
        # get a domain from client
        data, client_address = server_socket.recvfrom(1024)
        domain = data.decode('utf-8')

        if domain in ip_mapping:
            response = ip_mapping[domain].encode('utf-8')
        else:
            print("response = IP not found for the given domain. go to father")
            # Forward the request to the parent server
            server_socket.sendto(domain.encode('utf-8'), (parent_ip, parent_port))
            data, ip_parent = server_socket.recvfrom(1024)
            ip_domain = data.decode('utf-8')

            # Update the local mapping with the received IP from the parent server
            ip_mapping[domain] = ip_domain
            response = ip_domain.encode('utf-8')

        server_socket.sendto(response, client_address)


if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("Usage: python server.py <myPort> <parentIP> <parentPort> <ipsFileName>")
        sys.exit(1)

    my_port = int(sys.argv[1])
    parent_ip = sys.argv[2]
    parent_port = int(sys.argv[3])
    ips_file_name = sys.argv[4]

    file_path = ips_file_name
    ip_mapping = load_ip_mapping(file_path)
    udp_server(ip_mapping, my_port=my_port, parent_ip=parent_ip, parent_port=parent_port,
               ips_file_name=ips_file_name)
