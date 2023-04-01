import os
import sys
import subprocess
import json
def error(message,code=1):
    print(message)
    quit(code)
    
DIRECTORY=os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))

ARCH=str(int(subprocess.check_output('od -An -t x1 -j 4 -N 1 "$(readlink -f /sbin/init)"',shell=True))*32)
if ARCH != "64" and ARCH != "32":
    error("Failed to detect OS CPU architecture! Something is very wrong.")

def loadapp(name):
    icon=DIRECTORY + "/apps/" + name + "/icon-64.png"
    color = "#0000ff"
    with open(DIRECTORY + "/apps/" + name + "/website", 'r') as website_f:
        website = website_f.readline()[:-1]
    description = DIRECTORY + "/apps/" + name + "/description"
    if os.path.exists(DIRECTORY + "/data/status/" + name):
        with open(DIRECTORY + "/data/status/" + name, 'r') as f_status:
            status=f_status.readline()[:-1]
    else:
        status='uninstalled'
    with open(DIRECTORY + "/pimenu/tmp.json", "w") as tmp:
        tmp.write(json.dumps([{"label": "App Details"},{"name": name, "icon":icon, "website": website, "description": description, "status": status, "color_sheme": color}]))
    quit()
def getdefs(name, arg):
    if name.endswith("/"):
        if os.path.exists(DIRECTORY + "/icons/categories/" + name[:-1] + "-64.png"):
            icon=DIRECTORY + "/icons/categories/" + name[:-1] + "-64.png"
        else:
            icon=DIRECTORY + "/icons/categories/default-64.png"
        color = "#0000ff"
        label = name[:-1]
        status = ""
        value = arg+name
    else:
        icon=DIRECTORY + "/apps/" + name + "/icon-64.png"
        color = "#F22F2F"
        label = name
        value = name
        if os.path.exists(DIRECTORY + "/data/status/" + name):
            with open(DIRECTORY + "/data/status/" + name, 'r') as f_status:
                status=f_status.readline()[:-1]
        else:
            status='uninstalled'
    return({'label': label, 'name': value, 'status': status, 'icon': icon, 'color': color})


if len(sys.argv) <= 1:
    arg="./"
elif sys.argv[1] == "":
    arg="./"
elif sys.argv[1] == "back":
    with open(DIRECTORY + "/pimenu/c_dir", 'r') as data:
        dit=data.readline()
        if dit != './':
            arg=os.path.dirname(os.path.dirname(dit)) + "/"
        else:
            arg='./'
else:
    arg=sys.argv[1]
CURRENT_DIR=arg

categories=subprocess.check_output("cat " + DIRECTORY + "/etc/categories | sort | uniq | grep -v '|hidden'", shell=True).decode('unicode escape').split('\n')[0:-2]
tree=list()

for appc in categories:
    appc=appc.split('|')
    appc[1]="./" + appc[1] + "/"
    if os.path.exists(DIRECTORY + "/apps/" + appc[0] + "/install") or os.path.exists(DIRECTORY + "/apps/" + appc[0] + "/install-" + ARCH) or os.path.exists(DIRECTORY + "/apps/" + appc[0] + "/package"):
        if not "./All Apps/"+appc[0] in tree:
            tree.append("./All Apps/"+appc[0])
        tree.append(appc[1] + appc[0])
        
tree.sort()
list_apps = [arg + item.split(arg)[1].split("/")[0] for item in tree if item.startswith(arg)]
if arg == "./Installed/":
    for (x,y,files) in os.walk(DIRECTORY + '/data/status/'):
        list_stats = files
        break
    list_apps = list()
    for file in list_stats:
        with open(DIRECTORY + '/data/status/' + file, 'r') as f:
            stat=f.readline()
        if stat=="installed\n":
            list_apps.append("./Installed/" + file)
        
list_apps = list(set(list_apps))
list_apps.sort()
if arg=="./":
    items_dirs=[getdefs("All Apps/", "./"), getdefs("Installed/", "./")]
else:
    items_dirs=list()
items_apps=list()

for item in list_apps:
    name=item.split('/')[-1]
    if os.path.exists(DIRECTORY + "/apps/" + name):
        items_apps.append(getdefs(name, arg))
    else:
        items_dirs.append(getdefs(name + "/", arg))
        
items=items_dirs + items_apps
print(json.dumps(items))
with open(DIRECTORY + "/pimenu/tmp.json", "w") as tmp:
    tmp.write(json.dumps(items) + "\n")
with open(DIRECTORY + "/pimenu/c_dir", "w") as tmp:
    tmp.write(CURRENT_DIR)