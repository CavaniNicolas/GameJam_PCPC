# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define jem = Character('James Rond', color="#c8ffc8")

define nom = "Random"
define sympathie = 50


# Le jeu commence ici
label start:
    scene base:
        zoom 2
        yalign 0
    show spy
    jem "Enfin pour finir, écris ton nom "
    python:
        nom = renpy.input("Quel est votre nom")
    if nom == "jean":
        $ sympathie -= 40000
    jem "Bonjour [nom] et bienvenue dans la sociétée de la terre ronde "
    jem "Je te nomme membre officiel n°2 de la STR"
    menu:
        "Cool *rire géné*":
            $ sympathie = sympathie
        "Mais c'est génial !":
            $ sympathie += 10
        "M'en bas lec frer":
            $ sympathie -= 10
    jem "Bon on a pas le temps"
    jem "Tu vas devoir visiter 4 lieu dans le but de trouver des preuves que la terre est ronde"
    jump descriptionlieu
    return

label descriptionlieu:
    menu:
        jem "Sur quel lieu veut tu des info ?"

        "Le centre spatial de la NAFA":

        "La grande université de Flatvard":

        "Le stade de Platsbee":

        "La forêt":

        "Ca ira" :
            jump choixlieu

    jump descritpionlieu
