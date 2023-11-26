import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to host (server) port 80 is for HTTP, 443 for HTTPS in default
mysock.connect(('data.pr4e.org', 80))
#send GET request
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    #just check if there are some data, not empty
    if len(data) < 1:
        break
    #print the response
    print(data.decode())
mysock.close()