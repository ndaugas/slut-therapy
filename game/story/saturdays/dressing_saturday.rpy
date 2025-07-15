default nb_skirt = 0

label dressing_saturday:
    scene room_morning 
    with dissolve

    if day == 1:
        "C'est le premier moment que vous redoutiez."
        "Pourtant, c'est plutôt facile, en soi. Il y en a des vêtements dans votre dressing qui pourrait satisfaire le premier défi." 
        "Ce sont vos vêtements, rien qui ne soit déjà approuvé par vous-même !"
        "Pourquoi est-ce aussi difficile alors. Après tout, il ne s'agit que de conduire vos enfants à leurs activités, vous ne croiserez pas grand monde. Et à la zumba, vous êtes entre filles."
        "Vous essayez de vous rassurer mais le regard des pairs vous importe plus que vous le voulez. Et puis il y a le coach."
        "N'importe quoi. Vous tentez de chasser ces pensées ridicules de votre tête. Il est temps de décider"
        "Vous pouvez mettre cette robe-chemise en jean pour mettre vos jambes en valeur."
        "Ou bien pourquoi pas ce haut que vous n'avez jamais mis car vous trouviez que finalement car trop décolleté."
        "Et sinon cette robe à bretelles. Même un gilet, il reste sacrément décolleté."
    else:
        "On est samedi. Il est temps de mettre quelque chose de confortable."




    label dressing_choice:
        menu: 
            "Quelle tenue choisissez-vous ?"

            "Porter la robe-chemise":
                if try_action(compute_cost(1), 1):
                    $clothes = "casual_skirt"
                    $ show_isabelle()
                    "Vous boutonner votre robe-chemise."
                else:
                    jump dressing_choice
        
            "Porter le haut avec décolleté et un jean":
                if try_action(compute_cost(1), 1):
                    $clothes = "casual_lowcut"
                    "Je porte un décolleté !"
                else:
                    jump dressing_choice

            "Tenter la robe à bretelle fine":
                if try_action(compute_cost(2), 2):
                    if is_week_day():
                        $ clothes = "casual_light"

    call check_level