import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print('El nombre de tu ordenador es: ' + hostname)
print('El nombre de tu Ip es: ' + ip) 