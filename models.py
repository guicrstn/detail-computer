from ipaddress import ip_address
import os
import socket
import shutil



class Ordinateur():
    name = None
    user = None
    def __init__(self) :
        self.name = socket.gethostname()
        self.user = os.getlogin()

class Network():
    ordinateur : Ordinateur
    name = None
    ip_adress = None
    def __init__(self, ordinateur : Ordinateur):
        self.ordinateur = ordinateur
        self.ip_adress = socket.gethostbyname(self.ordinateur.name)

    def print_info(self):
        print( "Le nom de l'ordinateur est : {} \nL'utilisateur est: {}".format(self.ordinateur.name, self.ordinateur.user))
        print( "L'IP: {} ".format(self.ip_adress))

class Disk():
    ordinateur : Ordinateur
    space = None 
    def __init__(self, ordinateur : Ordinateur):
        self.ordinateur = ordinateur
        path = "C:"
        self.space = shutil.disk_usage(path) 
    def print_info(self):
        print("L'utilisation est : {}".format(self.space))



    
    