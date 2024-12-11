import libvirt
import os
import sys

conn = libvirt.open('qemu:///system')

# Functions
def Mach_list():
    domains = conn.listAllDomains(0)
    print('#### Liste des Machines Virtuelles ####')
    for dom in domains:
        infos = dom.info()
        print('#############')
        id = dom.ID()
        if id == -1:
            print("Le domaine n'est pas en cours d'exécution, donc il n'a pas d'ID.")
        else:
            print(f'The ID = {id}')
        print(f'Nom = {dom.name()}')
        etat = State(infos[0])
        print(f'État = {etat}')
        print(f'Max Mémoire = {infos[1]}')
        print(f'Nombre de CPUs virt = {infos[3]}')
        print(f'Temps CPU (en ns) = {infos[2]}')
    print('******************')

def launch_Mach():
    domains = conn.listAllDomains(0)
    for j, dom in enumerate(domains):
        print(f'{j}) Nom = {dom.name()}')
    try:
        i = int(input("Entrer le numéro de la machine à démarrer:: "))
        VM = domains[i]
        VM.create()
    except libvirt.libvirtError as e:
        print(str(e))
    except IndexError:
        print("La machine spécifiée n'existe pas")

def visualise():
    domains = conn.listAllDomains(0)
    for j, dom in enumerate(domains):
        print(f'{j}) Nom = {dom.name()}')
    try:
        i = int(input("Entrer le numéro de la machine à afficher:: "))
        VM = domains[i]
        os.system(f"virt-viewer {VM.name()} &")
    except libvirt.libvirtError as e:
        print(str(e))
    except IndexError:
        print("La machine spécifiée n'existe pas")

def HP_name():
    print(f"Le nom de l'hyperviseur est {conn.getHostname()}")

def shutdown_M():
    domains = conn.listAllDomains(0)
    for j, dom in enumerate(domains):
        print(f'{j}) Nom = {dom.name()}')
    try:
        i = int(input("Entrer le numéro de la machine à arrêter:: "))
        VM = domains[i]
        state = VM.info()[0]
        if state == libvirt.VIR_DOMAIN_RUNNING:
            VM.destroy()
            print(f"Arrêt de VM : {VM.name()}")
        else:
            print("VM n'est pas en cours d'exécution")
    except libvirt.libvirtError as e:
        print(str(e))
    except IndexError:
        print("La machine spécifiée n'existe pas")

def IP_M():
    domains = conn.listAllDomains(0)
    for j, dom in enumerate(domains):
        print(f'{j}) Nom = {dom.name()}')
    try:
        i = int(input("Entrer le numéro de la machine pour obtenir les informations IP:: "))
        VM = domains[i]
        if VM.info()[0] == libvirt.VIR_DOMAIN_RUNNING:
            ifaces = VM.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
            print("The interface IP addresses:")
            for name, val in ifaces.items():
                if val['addrs']:
                    for ipaddr in val['addrs']:
                        if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                            print(f"{ipaddr['addr']} VIR_IP_ADDR_TYPE_IPV4")
                        elif ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV6:
                            print(f"{ipaddr['addr']} VIR_IP_ADDR_TYPE_IPV6")
        else:
            print("Le domaine n'est pas en cours d'exécution")
    except libvirt.libvirtError as e:
        print(str(e))
        print("Essayer d'avoir l'adresse IP sans qemu agent")
        print(f"L'adresse IP de {VM.name()} est:")
        os.system(f"for mac in `sudo virsh domiflist {VM.name()} | grep -o -E '([0-9a-f]{{2}}:{{5}}[0-9a-f]{{2}})'` ; do arp -e | grep $mac | grep -o -P '^\\d{{1,3}}\\.\\d{{1,3}}\\.\\d{{1,3}}\\.\\d{{1,3}}' ; done")
    except IndexError:
        print("La machine spécifiée n'existe pas")

def State(state):
    if state == libvirt.VIR_DOMAIN_NOSTATE:
        return 'NOSTATE'
    elif state == libvirt.VIR_DOMAIN_RUNNING:
        return 'RUNNING'
    elif state == libvirt.VIR_DOMAIN_BLOCKED:
        return 'BLOCKED'
    elif state == libvirt.VIR_DOMAIN_PAUSED:
        return 'PAUSED'
    elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
        return 'SHUTDOWN'
    elif state == libvirt.VIR_DOMAIN_SHUTOFF:
        return 'SHUTOFF'

# Main interface
while True:
    print('\n\n\n<<<<<<<<<<<<<<<<<<< VM Manager >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    print('0) Nom de la machine hyperviseur')
    print('1) Lister les machines virtuelles')
    print('2) Démarrer une machine')
    print('3) Visualiser une machine avec virt-viewer')
    print('4) Arrêter une machine')
    print("5) L'adresse IP d'une machine virtuelle donnée")
    print('6) Quitter')
    try:
        ch = int(input("Votre choix ::"))
    except ValueError:
        ch = -1

    if ch == 0:
        HP_name()
    elif ch == 1:
        Mach_list()
    elif ch == 2:
        launch_Mach()
    elif ch == 3:
        visualise()
    elif ch == 4:
        shutdown_M()
    elif ch == 5:
        IP_M()
    elif ch == 6:
        conn.close()
        break
    else:
        print('Entrée invalide \n')

