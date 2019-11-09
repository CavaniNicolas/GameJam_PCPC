# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

define manu = Character('Manu Macpla', color="#c8ffc8")



define perso = Character('Joueur', color="#c8ffc8")



# Le jeu commence ici

label start:
    $ nom = ""
    $ sympathie = 50
    $ platiste = 0
    $ jaque = 0
    manu "Sacré match, hein? Jaque est en feu aujourd'hui."

    menu:
        "C'est vrai.":
            $ sympathie += 5
        "Carrément! Il est bien meilleur qu'à la saison précédente":
            $ sympathie += 10
        "Bof. Le frisbee ne m'intéresse pas tellement.":
            $ sympathie -= 5
            if platiste >= 10:
                $ platiste -= 10
        "Vous rigolez? Il joue comme un pied":
            $ sympathie -= 10
            $ jaque += 1

    if sympathie < 50 :
        manu "Vous gaspillez mon temps. Je suis ici pour me détendre."

        manu "Je suis un homme très occupé, j'ai de gros PROJETS en cours."

        if jaque == 1
            jump jakill
    if sympathie > 50
        manu "Quel est votre sport préféré?"
        menu:
            "Le frisbee."
                $ sympathie -= 5
            "Le football."
                $ secret = 1
            "Le pole dance."
                $ sympathie += 10
            "L'escrime."
                $ sympathie += 5
    if secret == 0
        manu "Intéréssant."
        jump manu
    if secret == 1
        manu "Rejoignez moi dans ma loge après le match."
        jump loge
    return

label jakill:
    
    return

label loge:

    return
