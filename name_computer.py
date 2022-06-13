import socket   
import os


def get_name_computer(): 
    ''' function computer name '''
    name=socket.gethostname()   
    hostname=os.getlogin()

    return (name, hostname)