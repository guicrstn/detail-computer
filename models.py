import os
import socket
import shutil
import subprocess



class Ordinateur():
    '''
    Class : Ordinateur 
    Description : Classe qui comprend le nom du poste et l'utilisateur.
    '''
    def __init__(self) :
        self.name = socket.gethostname()
        self.user = os.getlogin()

class Network():
    '''
    Class : Network 

    Description : Classe qui comprend: Nom de domaine, adresse IP, masque de sous réseaux, passerelle, dns
    '''
    def __init__(self, ordinateur : Ordinateur):
        self.ordinateur = ordinateur
        self.ip_adress = socket.gethostbyname(self.ordinateur.name)

    def print_info(self):
        print( "Le nom de l'ordinateur est : {} \nL'utilisateur est: {}".format(self.ordinateur.name, self.ordinateur.user))
        print( "L'IP: {} ".format(self.ip_adress))

class Disk():
    '''
    Class : Disk 
    
    Description : Classe qui comprend: taille du disque utilisé, taille de la place restante, taille total
    '''
    def __init__(self, ordinateur : Ordinateur):
        pass        
        self.ordinateur = ordinateur
        self.path = "C:"
        self.space = shutil.disk_usage(self.path) 
    def print_info(self):
        print("ESPACE DISQUE \n {}".format(self.space))

class Software():
    
    def __init__(self) -> None:

        '''
        Class : Disk 
        
        Description : Classe qui comprend: taille du disque utilisé, taille de la place restante, taille total
        '''
    
        self.software = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        self.a = str(self.software)
    def print_info(self):
        print("APPLICATION INSTALLEES \n " ) 
        for element in self.a.split("\\r\\r\\n")[6:]: 
            print(element)