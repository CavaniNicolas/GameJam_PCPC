# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define jem = Character('James Rond', color="#c8ffc8")
define juge = Character('Juge RondHomme',color="#cd45a3")
define nom = "Random"
define sympathie = 50

define flash = Fade(.25, 0, .75, color="#fff")


# Le jeu commence ici
label start:
    scene base
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
            "NAFA"
        "La grande université de Flatvard":
            "Flatvard"
        "Le stade de Platsbee":
            "bbeeeeeeeeeee"
        "La forêt":
            "foret"

        "Ca ira" :
            jem "Très bien passons a ton choix"
            jump choixlieu

    jump descriptionlieu

label choixlieu:
    menu:
        jem "Où veux tu aller ?"

        "Le centre spatial de la NAFA":
            jump NAFA
        "La grande université de Flatvard":
            jump flatvard
        "Le stade de Platsbee":
            jump platsbee
        "La forêt":
            jump foret

        "Je veux présenter mes preuves !" :
            jump tribunal

label tribunal:
    jem "Excellent choix ...."
    jem "{cps=5}Excellent ... Choix{/cps}  "
    scene tribunal
    with flash
    juge ""
