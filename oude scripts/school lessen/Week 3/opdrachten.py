__author__ = 'alexander'

import os
import sys

b="Ledenlijst.txt"

if os.path.exists(b):
    print("bestaat", b,"Hoeraa.")
    f=open(b)
else:
    print("bestand",b,"bestaat niet.")
    sys.exit(1)