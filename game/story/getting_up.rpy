label getting_up:

    if day == 1:
        call first_getting_up

    call dressing

    return

label first_getting_up:

    scene room_morning with fade

    "Le réveil affiche 7h32. Trop tôt pour un samedi."

    "Vous ouvrez les yeux en grognant légèrement, la lumière pâle filtrant à travers les volets à moitié fermés."

    "Un parfum de café flotte déjà dans l'air, signe que François est levé depuis un moment."

    "Vous restez allongée quelques secondes, les images de la soirée d'hier encore vives dans votre esprit."

    "Le bruit du bar, les rires de Gwen, et surtout cette étrange sensation d'excitation mêlée de crainte au moment où elle vous a parlé de ses défis."

    $ clothes = "pajamas"
    $ show_isabelle()

    p "Qu'est-ce que j'ai accepté ?"

    "Un léger frisson vous parcourt en repensant à ses mots"
    
    scene bar with fade

    show gwen smiling

    g "Tu verras, après ces quatre semaines, tu sauras si tu veux vraiment changer les choses."

    # TODO play sound toctoc

    scene room_morning

    "Un coup contre la porte de la chambre vous fait sursauter."

    show chloe happy at right
    $ show_isabelle("smiling", [left])
    show chloe at center
    with moveinright

    d "Maman ! C'est l'heure du p'tit dej !"

    "Chloé, six ans, la crinière en bataille et encore en pyjama licorne, vous fixe avec impatience."

    d "Tu sais, j'ai bien travaillé mon piano. Je suis sure que Sami va être content de moi ce matin." 

    show simon happy at center_right

    s "Coucou Maman, regarde ce que je vais faire au baby athlé !"

    "Simon, quatre ans et demi, déboule à son tour et exécute une roulade (ou presque) sur le lit, déjà surexcité."

    $ show_isabelle("smile")

    "Un soupir attendri vous échappe."

    p "J'arrive, j'arrive…"

    "Un samedi comme un autre. Enfin, non, pas tout à fait. Les défis trottent tranquillement dans votre tête tandis que la vie normale continue autour de vous."

    return


label dressing:

    scene room_morning 
    with dissolve

    "Il est temps de vous habiller."

    if day == 1:
        "C'est le premier moment que vous redoutiez."
        "Pourtant, c'est plutôt facile, en soi. Il y en a des vêtements dans votre dressing qui pourrait satisfaire le premier défi." 
        "Ce sont vos vêtements, rien qui ne soit déjà approuvé par vous-même !"
        "Pourquoi est-ce aussi difficile alors."
        "Après tout, vous n'avez qu'à transporter vos enfants à leurs activités, vous verrez peu de monde. Et à la zumba, vous êtes entre filles."
        "Vous essayez de vous rassurer mais le regard des pairs vous importe plus que vous le voulez. Et puis il y a le coach."
        "N'importe quoi. Vous tentez de chasser ces pensées ridicules de votre tête. Il est temps de décider"

    label dressing_choice:
        menu: 
            "Comment vous habillez-vous ?"

            "Porter une jupe courte":
                if try_action(compute_cost(1), 1):
                    "Je porte une jupe !"
                else:
                    jump dressing_choice
        
            "Porter un décolleter":
                "Porter un décolleter"

    call check_level
    

    return