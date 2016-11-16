__author__ = 'alexander'
import xml
import xmltodict
import json
import requests

auth_details = ('alexanderkorn7@gmail.com', 'QEkmKHOQOjFBzo9edNsDTvqM-l-1y8X468cfy1fUO1ip_s525hPLgw')
response = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=auth_details)

#response.save('stations.json')


def shrijf_xml(reponse):
    bestand = open("stations.json", 'w')
    bestand.write(str(response))
    bestand.close()

#with open('data.txt', 'w') as outfile:
#  json.dump(data, outfile)

#print(response)