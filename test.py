import netifaces


addrs = (netifaces.ifaddresses('ens33'))
print(addrs[netifaces.AF_INET][0]['addr'])