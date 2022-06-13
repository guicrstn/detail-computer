import os
import socket
import shutil
import subprocess



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
        print("ESPACE DISQUE \n {}".format(self.space))

class Software():
    name = None
    software = None
    a = None
    def __init__(self) -> None:
        print("APPLICATION INSTALLEES \n " )   

        self.software = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        self.a = str(self.software)
    def print_info(self):
        for element in self.a.split("\\r\\r\\n")[6:]: 
            print(element)