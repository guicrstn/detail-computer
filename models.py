import os
import socket
import shutil
import subprocess
import platform
import netifaces

class Prompt():

    '''
    Class : Prompt 
    Description : Classe qui permet d'afficher des informations.

    '''

    def __init__(self) -> None:
        self.value = "SYSTEME D'EXPLOITATION <<<"   
        self.print_info()

    def set_value(self, value):
        self.value = value
        self.print_info()    

    def print_info(self):
        print('>>> {}'.format(self.value))


class Interfaces():
    
    '''
    Class : Interfaces 

    Description : Classe qui contient les informations de l'interface: 
    - Système d'exploitation

    - Version du système d'exploitation
                                                                        
    - Tailles des bits du système 

    - Adresse IP

    - Masque de sous réseaux

    - Passerelle par défault

    '''

    def __init__(self) -> None:
        self.value = " Interface <<<"  
        self.addrs = netifaces.ifaddresses('ens33')
    def get_IPV4(self):
        return self.addrs[netifaces.AF_INET][0]['addr']
    def get_subnetmask(self):
        return self.addrs[netifaces.AF_INET][0]['netmask']
    def get_defaultgateway(self):
        return self.addrs[netifaces.AF_INET][0]['broadcast']










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


