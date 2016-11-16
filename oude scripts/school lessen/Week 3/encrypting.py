__author__ = 'alexander'
plain_text = "Hoi dit is een test. hallo niet random"

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)