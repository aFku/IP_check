import socket

def getIP():
    try:
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        return ip
    except:
        return 'Cannot get IP'


if __name__ == '__main__':
    print('Library test')
    print('IP adress: ', getIP())
