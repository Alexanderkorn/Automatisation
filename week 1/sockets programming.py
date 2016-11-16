import socket
import sys
import subprocess

#subprocess.Popen('calc')
p = subprocess.Popen('calc')
print("daar ben ik")
p.wait()
print("nu ben ik weg")
print("nu ben ik weg")

