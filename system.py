import socket

def getHostIP():
    try:
        hostname = socket.gethostname() + '.local'
        ipaddress = socket.gethostbyname(hostname)

        return {'hostname': hostname, 'ipaddress': ipaddress}
    except:
        print("Unable to get Hostname and IP")

    