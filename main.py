
from models import Computer, Disk, Interfaces, Network, Ordinateur, Software, Prompt
import platform
import sysconfig

prompt = Prompt()

prompt.set_value("Système d'exploitation............ {}".format(platform.system()))
prompt.set_value("Version du sytème d'exploitation.. {}".format(sysconfig.get_platform()))
prompt.set_value("Taille des bits du système........ {}".format(platform.machine()))

interfaces = Interfaces()

prompt.set_value("Adresse IP ....................... {}".format(interfaces.get_IPV4()))
prompt.set_value("Masque de sous réseaux............ {}".format(interfaces.get_subnetmask()))
prompt.set_value("Passerelle par défault............ {}".format(interfaces.get_defaultgateway()))
prompt.set_value("Adresse MAC....................... {}".format(interfaces.get_macadress()))

computer = Computer()

prompt.set_value("Taille total...................... {} GiB".format(computer.get_totaldisk()))
prompt.set_value("Taille utilisé...................... {} GiB".format(computer.get_useddisk()))
prompt.set_value("Taille disponible...................... {} GiB".format(computer.get_freedisk()))


