import requests

all_packages = []
with open('packages.txt') as my_file:
    for line in my_file:
        all_packages.append(line)
        
for i in range(len(all_packages)):
    package = all_packages[i].strip("\n")
    print ("Fetching: ", package)
    filename = "SPEC/" + package + ".spec"
    url = "https://src.fedoraproject.org/rpms/" + package + "/raw/rawhide/f/" + package + ".spec"
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
