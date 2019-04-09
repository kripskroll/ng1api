import xml.etree.ElementTree as ET

def ipExist(existips, newips):
    """Check if IP is already defined.

    Arguments :
        existips -- String with list of existing IPs.
        newips -- String with new IPs"""
    #create a set of items from a list for both ips
    
    return any(elem in existips.split(",") for elem in newips.split(","))
            

def addIP(xmlapp, ip):
    """Add IP(s) to Application Definition

    Arguments :
        xmlapp -- xml Application definition
        ip -- IP or list of IPs, in a comma separated string "1.1.1.1/32, 2.2.2.2/32" with netmask"""

    root = ET.fromstring(xmlapp)
    # find HostAddresses
    hosts = root.findall('.//HostAddresses')
    if hosts ==[] :
        print("No IP defined for Application.\nCreating ,<HostAdresses>")
        for appconf in root.findall('ApplicationConfiguration'):
            ET.SubElement(appconf, 'HostAddresses')
    hosts = root.findall('.//HostAddresses')
    for host in hosts:
        if host.text is None:
            # <HostAdresses> has just been created and has no IPs
            new_ip = ip
        elif not ipExist(host.text,ip):
            # new IPs are not duplicates of existing ones
            print ipExist(host.text,ip)
            new_ip = host.text + "," + ip
        else:
            # Some IPs are already existing. Return only old ones
            print("IPs already exists")
            new_ip = host.text
        print new_ip
        host.text = new_ip
    return ET.tostring(root)
