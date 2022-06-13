import socket   
import os
from models import Disk, Network, Ordinateur

from name_computer import get_name_computer
from network_computer import get_network_computer

''' Result of script '''   

def print_result(type,val):
    print("{} {}".format(type,val))   

(name, hostname) = get_name_computer()

# (domain_name, ip_address, mask, gateway, dns) = get_network_computer

#print_result('Nom du PC :\n', name)
#print_result('Nom utilisateur :\n',hostname)
#print_result('ip:\n', get_network_computer(name))


monOrdinateur1 = Ordinateur()
monReseau1 = Network(monOrdinateur1)
monReseau1.print_info()
monDisk = Disk(monOrdinateur1)
monDisk.print_info()