def load_ip_mapping(file_path):
    ip_mapping = {}
    with open(file_path, 'r') as file:
        for line in file:
            domain, ip = line.strip().split(',')
            ip_mapping[domain] = ip
    return ip_mapping


## def udp_server(ip_mapping, my_host='localhost', my_port=12345, parent_ip='localhost', parent_port=12346, ips_file_name='default_ips.txt'):
def udp_server(ip_mapping, host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        domain = data.decode('utf-8')

        if domain in ip_mapping:
            response = ip_mapping[domain].encode('utf-8')
        else:
            response = b"IP not found for the given domain."

        server_socket.sendto(response, client_address)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python server.py <myPort> <parentIP> <parentPort> <ipsFileName>")
        sys.exit(1)

    my_port = int(sys.argv[1])
    parent_ip = sys.argv[2]
    parent_port = int(sys.argv[3])
    ips_file_name = sys.argv[4]

    file_path = ips_file_name
    ip_mapping = load_ip_mapping(file_path)
    udp_server(ip_mapping, my_port=my_port, parent_ip=parent_ip, parent_port=parent_port, ips_file_name=ips_file_name)