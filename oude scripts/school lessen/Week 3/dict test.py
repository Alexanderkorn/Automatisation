__author__ = 'alexander'

rp={
    'Processor': 'Cortex-A7',
    'Type': 'Pi2 Model B',
    'Price': '35$',
    'USB 2.0': 4,
    'In Store': True
}

for i in rp:
    print(i,rp[i])

for k,v in rp.items():
    print(k,"***",v)

rp['Memory']="700 MB"
print(rp)