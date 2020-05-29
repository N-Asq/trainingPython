def entreBornes(borneInf, borneSup):
    if borneInf>borneSup:
        print("Les bornes sont dans le mauvais sens, on inverse.")
        borneInf,borneSup = borneSup,borneInf
    nb = borneInf
    while nb <= borneSup:
        val = (yield nb) # le générateur recoit la valeur du programme d'appel et envoie nb 
        if val is not None: # Si la valeur existe
            nb = val # On change la valeur de nb
        else:
            nb += 1 # sinon on incrémente
        #print("-",nb)


if __name__=="__main__":
    for nb in entreBornes(6,2):
        print(nb)

    gen = entreBornes(10,18)
    for nb in gen:
        if nb > 22:
            gen.close()
            print("Interdit au plus de 18 !")
        elif nb == 12:
            gen.send(15)
        
        print(nb)