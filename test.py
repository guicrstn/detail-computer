import shutil

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Utilisé: %d GiB" % (used // (2**30)))
print("Disponible: %d GiB" % (free // (2**30)))