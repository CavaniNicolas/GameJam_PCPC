# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define Perso_pense = Character(nom, who_color="#a2a9af", what_italic=True)
define RondWizzly_mys = Character('???', who_color="#c8ffc8")
define IsaacOldkilo_mys = Character('???', who_color="#a60414")
define RondWizzly = Character("Rond Wizzly", who_color="#c8ffc8")
define IsaacOldkilo = Character("Isaac Oldkilo", who_color="#a60414")

# narrateur : ne rien mettre devant

class perso :
    $ nom = "John Doe"
    $ platiste = 0
    $ sympathie = 50

# Le jeu commence ici
label start:
    "[nom"



#   show image : options
#   scene
#   menu :


    nom "Vous venez de créer un nouveau jeu Ren'Py."

    nom "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    return
