
password = input("hier uw password:")

fname = 'password.txt'
try:
    try:
        if (fname):
            print("Found file '{}'".format(fname))
            with open(fname, 'r') as f:
                for line in f:
                    print (line, end="")
            f.close()
        else:
            print("no file found")

    except:
        print("sorry er is iets verkeerd gegaan.")
except:
    print()
