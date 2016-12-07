import xml.etree.ElementTree as etree

tree = etree.parse('./week_opdracht_4.xml')
root = tree.getroot()
#print("title van de server 1 is:", root.find('servers/server[@id="1"]/title').text)
#print("title van de server 1 is:", root.find('servers/server[@id="2"]/title').text)

servers = root.findall('.//server')
clients = root.findall('.//client')
for server in servers:
    print("\nServer met id:", server.attrib['id'])
    print("Server naam is:", server.find('title').text)
    print("Server ipaddress is:", server.find('ipaddress').text)
    print("Server harddisks:", server.find('harddisks_1').text)
    print("Server harddisks:", server.find('harddisks_2').text)
    print("Server harddisks:", server.find('harddisks_3').text)
    print("Server OS:", server.find('OS').text)

for client in clients:
    print("\nServer met id:", client.attrib['id'])
    print("Server naam is:", client.find('title').text)
    print("Server ipaddress is:", client.find('ipaddress').text)
    print("Server harddisks:", client.find('harddisks_1').text)
    print("Server OS:", client.find('OS').text)

