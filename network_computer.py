import socket   

def get_network_computer(hostname):
    ''' function of network'''
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mysocket.connect(("8.8.8.8", 80))
    print(mysocket.getsockname()[2])
    mysocket.close()    
    ip = socket.gethostbyname(mysocket)
    return(ip)
