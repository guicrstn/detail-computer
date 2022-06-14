
from models import Disk, Interfaces, Network, Ordinateur, Software, Prompt
import platform
import sysconfig

''' Result of script '''   

def print_result(type,val):
    print("{} {}".format(type,val))   



# (domain_name, ip_address, mask, gateway, dns) = get_network_computer

#print_result('Nom du PC :\n', name)
#print_result('Nom utilisateur :\n',hostname)
#print_result('ip:\n', get_network_computer(name))

prompt = Prompt()

prompt.set_value("Système d'exploitation............ {}".format(platform.system()))
prompt.set_value("Version du sytème d'exploitation.. {}".format(sysconfig.get_platform()))
prompt.set_value("Taille des bits du système........ {}".format(platform.machine()))

interfaces = Interfaces()

prompt.set_value("Adresse IP ....................... {}".format(interfaces.get_IPV4()))
prompt.set_value("Masque de sous réseaux............ {}".format(interfaces.get_subnetmask()))
prompt.set_value("Passerelle par défault............ {}".format(interfaces.get_defaultgateway()))

monOrdinateur1 = Ordinateur()
monReseau1 = Network(monOrdinateur1)
monReseau1.print_info()
monDisk = Disk(monOrdinateur1)
monDisk.print_info()
monSoftware = Software()
monSoftware.print_info()