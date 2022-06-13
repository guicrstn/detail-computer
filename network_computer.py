import socket   




def get_network_computer(hostname):
    ''' function of network'''
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(hostname)

    return(ip)
