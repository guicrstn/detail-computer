import os
import socket
import shutil
import subprocess
import platform
import netifaces
import shutil

class Prompt():

    '''
    Class : Prompt 
    Description : Classe qui permet d'afficher des informations.

    '''

    def __init__(self) -> None:
        self.resultats = [] 
        self.set_value("SYSTEME D'EXPLOITATION <<<" )  
       

    def set_value(self, value):
        self.value = value
        self.resultats.append(self.value)
        self.print_info()    

    def print_info(self):
        print('>>> {}'.format(self.value))

    def save_to_txt(self, name = "resultats" ):
        with open('{}.txt'.format(name), 'a') as file: 
            for value in self.resultats:
                file.write('{}\n'.format(value))

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

    - Adresse MAC

    '''

    def __init__(self) -> None:
        self.value = "Interface <<<"  
        self.addrs = netifaces.ifaddresses('ens33')
    def get_IPV4(self):
        return self.addrs[netifaces.AF_INET][0]['addr']
    def get_subnetmask(self):
        return self.addrs[netifaces.AF_INET][0]['netmask']
    def get_defaultgateway(self):
        return self.addrs[netifaces.AF_INET][0]['broadcast']
    def get_macadress(self):
        return self.addrs[netifaces.AF_LINK][0]['addr']
        


class Computer():


    '''
    Class : Computer

    Description : Classe qui contient les informations du disque dur.

    - Taille total  
                                                                        
    - Taille utilisé 

    - Taille restante

    '''
    def __init__(self) -> None:

        self.value = "Information disque <<<"
        self.total, self.used, self.free = shutil.disk_usage("/")
    
    def get_totaldisk(self):
        return self.total // (2**30)
    
    def get_useddisk(self):
        return self.used // (2**30)
    
    def get_freedisk(self):
        return self.free // (2**30)
          

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


