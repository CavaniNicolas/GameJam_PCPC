# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Narator', color="#c8ffc8")
define nom="osef"
define platiste=0
define sympathie=50




# Le jeu commence ici
label start:

    "Bienvenue dans la fôret de bitenbois"

    n "je devrais visiter cette fôret"

    jump r1


label r1:
    n "que voulez vous faire?"

    menu:
        "aller à droite":
            jump r14
        "aller à gauche":
            jump r2

        "aller en avant":
            jump r12

        "coup de boule à l'arbre, des pommes tombent"
            jump r1
        "sortir de la forêt"

label r2:
    n "que voulez vous faire?"

    menu:
        "aller à droite":
            jump r1

        "aller en avant":
            jump r3

        "coup de boule à l'arbre, des pommes tombent":
            jump r2

label r3:
    n "que voulez vous faire?"

    menu:
        "aller à droite":
            jump r14
        "aller à gauche":
            jump r2

        "aller en avant":
            jump r12

        "coup de boule à l'arbre, des pommes tombent"
            jump r1
        "sortir de la forêt"
