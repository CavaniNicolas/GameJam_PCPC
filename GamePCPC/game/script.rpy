define n = Character('Narator', color="#c8ffc8")
define nom="osef"
define platiste=0
define sympathie=50
define oldk= Character('OldKilo', color="#c8ffc8")




# Le jeu commence ici
label start:

    "Bienvenue dans la fôret de bitenbois"

    n "je devrais visiter cette fôret"

    jump r1


label r1:
    n "que voulez vous faire?"

    menu:
        "aller à l'OUEST":
            jump r14
        "aller à l'EST":
            jump r2

        "aller au SUD":
            jump r12

        "coup de boule à l'arbre, des pommes tombent"
            jump r1
        "sortir de la forêt"

label r2:
    n "que voulez vous faire?"

    menu:
        "aller à l'EST":
            jump r1

        "aller au SUD":
            jump r3

        "coup de boule à l'arbre, des pommes tombent":
            jump r2

label r3:
    n "que voulez vous faire?"

    menu:
        "aller à l'EST":
            jump r12
        "aller au NORD":
            jump r2

        "aller au SUD":
            jump r4

        "coup de boule à l'arbre, des pommes tombent":
            jump r3
        "sortir de la forêt":
            "Vous Partez"
label r4:
    n "que voulez vous faire?"

    menu:
        "aller à l'EST":
            jump r11
        "aller AU NORD":
            jump r3
        "aller au SUD":
            jump r5

        "coup de boule à l'arbre, des pommes tombent":
            jump r4
        "sortir de la forêt":
            "Vous Partez"
label r11:
    n "que voulez vous faire?"

    menu:
        "aller à l'EST":
            jump r4
        "aller à l'OUEST":
            jump r10
        "aller au NORD":
            jump r12

        "aller au SUD":
            jump r6

        "coup de boule à l'arbre, des pommes tombent":
            jump r11
label r10:
        n "que voulez vous faire?"

        menu:
            "aller à l'EST":
                jump r11
            "aller à l'OUEST":
                jump r9
            "aller au NORD":
                jump r13

            "aller au SUD":
                jump r7

            "coup de boule à l'arbre, des pommes tombent":
                jump r10
label r9:
        n "que voulez vous faire?"

        menu:
            "aller à l'EST":
                jump r10
            "aller à l'OUEST":
                jump r19
            "aller au NORD":
                jump r16

            "aller au SUD":
                jump r8

            "coup de boule à l'arbre, des pommes tombent":
                jump r9
label r19:
        n "que voulez vous faire?"

        menu:
            "aller à l'EST":
                jump r9
            "aller au NORD":
                jump r16

            "aller au SUD":
                jump pomme

            "coup de boule à l'arbre":
                "des pommes tombent"
                jump r19
            "sortir de la forêt":
                vous partez

label pomme:
    "coup de boule à l'arbre, quelqu'un tombe":
