import socket

# Scan local network IPs from 192.168.1.1 to 192.168.1.10
print("Scanning network...")

for i in range(1, 11):
    ip = f"192.168.1.{i}"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Timeout for faster scanning
    result = sock.connect_ex((ip, 80))  # Check port 80 (HTTP)
    if result == 0:
        print(f"{ip} is active")
    sock.close()

print("Scan complete!")
