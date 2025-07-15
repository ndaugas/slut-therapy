label getting_up_saturday:

    if day == 1:
        call first_getting_up
    else:
        call getting_up_usual_saturday

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

    "Un léger frisson vous parcourt en repensant à ses paroles."
    
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

    "Simon, quatre ans et demi, déboule à son tour et exécute une roulade (ou quelque chose qui y ressemble) sur le lit, déjà surexcité."

    $ show_isabelle("smile")

    "Un soupir attendri vous échappe."

    p "J'arrive, j'arrive…"

    "Un samedi comme un autre. Enfin, non, pas tout à fait. Les défis trottent tranquillement dans votre tête tandis que la vie normale continue autour de vous."

    return