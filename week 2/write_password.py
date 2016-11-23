
fileopen = open("password.txt", "r")
filewrite = open("password.txt", "a")
password = input()

for line in fileopen:
    if password in line:
        print("Wachtwoord OK")
    else:
        print("Wachtwoord FOUT")
        filewrite.write('\n')
        filewrite.write(password)

fileopen.close()
filewrite.close()
