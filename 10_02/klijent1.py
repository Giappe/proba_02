import socket

# c = socket.socket(type=socket.SOCK_DGRAM)

# c.sendto(b"dobar dan", ("127.0.0.1", 9000))

# for i in range(1000):
#     c.sendto(f"dobar dan {i}".encode(), ("127.0.0.1", 9000))



c = socket.socket(type=socket.SOCK_DGRAM)
c.sendto(f"dovla|10,20".encode(), ("127.0.0.1", 9000))
odgovor,adresa = c,recvfrom(128)
print(odgovor,adresa)
