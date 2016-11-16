
waarde = 225

# PLEK A

for munt in 200, 100, 50, 20, 10, 5, 2, 1 :
    aantal = 0

    # PLEK B

    while waarde >= munt :
        print("kom ik hier?")# PLEK C

        aantal = aantal + 1
        waarde = waarde - munt

    if aantal > 0 :
        print ( '' + str(aantal) + 'x' + str(munt) )
    else :
        print("kom ik hier?")# PLEK D
        break