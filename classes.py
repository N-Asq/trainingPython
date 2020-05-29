# Comprendre les classes

class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    personnesCrees = 0 # Attribut de classe


    def combien(cls): # Méthode de classe
        print("{0} personnes ont été créées.".format(cls.personnesCrees))
    combien = classmethod(combien)

    def sayHello(): # Méthode statique (indépendante de données)
        print("Hello World !")
    sayHello = staticmethod(sayHello)

    #################################################################
    ## Méthodes spéciales
    def __init__(self,nom = "Claus",prenom = "Santa", age = 42, lieuResidence = "Laponie"): # Notre méthode constructeur
        print("Création d'une Personne.")
        self.nom = nom         
        self.prenom = prenom 
        self.age = age
        self._lieuResidence = lieuResidence
        Personne.personnesCrees += 1

    def __repr__(self): # Méthode spéciale pour la représentation (affichage dans l'intérpréteur)
        return("Objet de classe Personne:\n\tNom: {0}\n\tPrénom: {1}\n\tAge: {2}\n\tLieu de résidence: {3}".format(self.nom,self.prenom,self.age,self.lieuResidence))

    def __str__(self): # Méthode spéciale pour l'affichage avec print(). Egalement, méthode utilisée lors du castage en str. Si non définie, utilisation de __repr__()
        return("{0} {1}, âgé de {2} ans.".format(self.prenom,self.nom,self.age))
    
    def __getattr__(self,attr): # Méthode appélée si l'attribut invoqué n'existe pas
      print("L'attribut {0} n'existe pas.".format(attr))

    def __setattr__(self,attr,val_attr): # Méthode appélée si on fixe la valeur d'un attribut attr
        object.__setattr__(self, attr, val_attr)
        print("{0} vaut {1}.".format(attr,val_attr))
        
    def __delattr__(self,attr): # Méthode appélée si on fixe la valeur d'un attribut attr
        object.__delattr__(self, attr)
        print("L'attribut {0} a été supprimé.".format(attr))


    #################################################################
    # Définir une propriété (exemple avec le lieu de résidence)
    def _getLieuResidence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieuResidence'"""
        print("On accède à l'attribut lieuResidence !")
        return self._lieuResidence

    def _setLieuResidence(self, nouvelleResidence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
        self.prenom, nouvelleResidence))
        self._lieuResidence = nouvelleResidence

    def _rmLieuResidence(self):
        """Méthode appelée quand on souhaite supprimer le lieu de résidence"""
        print("{} ne peut pas être SDF !".format(self.prenom))
        
    # On va dire à Python que notre attribut lieuResidence pointe vers une
    # propriété
    lieuResidence = property(_getLieuResidence, _setLieuResidence,_rmLieuResidence,"Message d'aide écrit par moi")
    
if __name__ == "__main__":
    print("\nTEST DE LA CLASSE Personne")
    print("--------------------")
    print("Test d'un attribut de classe.")
    Personne.combien()
    tonton = Personne("De Montargis","Quentin",54,"Montargis")
    tonton.combien()
    print("--------------------")


    print("Je m'appelle {0} {1}, j'ai {2} ans et j'habite à {3}."
        .format(tonton.prenom,tonton.nom.upper(),tonton.age,tonton.lieuResidence))
    tonton.lieuResidence = "Puteaux"
    print("Tentative de suppression du lieu de résidence.")
    del(tonton.lieuResidence)
    print("Tentative de suppression de lâge.")
    del(tonton.age)
    # help(Personne.lieuResidence)
    print("--------------------")
    print(tonton.sexe)
    tonton.sexe = "M" # Apparemment on peut ajouter un attribut à la classe sans que cela ne pose problème
    print(tonton.sexe)
    print("--------------------")
    print("Affichage des attributs spécifiques à l'objet :")
    print("\t",tonton.__dict__,"\n")
    print("Affichage de tous les attributs et méthodes  de la classe et de l'objet:")
    print("\t",dir(tonton))
    print("--------------------")

    repr(tonton)
    help(Personne.lieuResidence)
