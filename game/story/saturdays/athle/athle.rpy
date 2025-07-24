
# Maxime est un jeune homme de 18 ans, confiant, qui a l'habitude de séduire. 
# Il a à son palmarès plusieurs conquêtes et séduire une femme plus âgée et mariée ne lui fait pas peur.
define t = Character("Maxime")

default athle_first_time_revealing_clothes = True

# Relation avec Maxime
# 0 : ils ne se connaissent pas (lv 0)
# 1 : ils se sont rencontrés et connaissent leurs prénoms (lv 0)
# 2 : ils connaissent leurs numéros (lv 0)
# 3 : ils ont passé du temps ensemble (lv 1)
# 4 : ils se sont embrassés (lv 1)
# 5 : ils ont eu un préliminaire (lv 2)
# 6 : ils ont eu une relation (lv 3)
# 7 : elle est accroc (lv 3)
default relation_t = 0

label athle:

    if day == 1:
        "J'arrive à la maison et dans un branle-bas de combat, je laisse Chloé à son père pour l'échanger contre Simon."
        "Il est déjà habillé, il ne reste qu'à remplir sa gourde."
        "J'ai à peine le temps de faire un bisou à François que je dois déjà partir."
        "J'arrive au gymnase. Simon ne tient pas en place, impatient de commencer son cours de baby-athlé."

        "A l'intérieur, les parents embrassent leurs enfants, les rassurent, les encouragent." 
        "Pour beaucoup, laisser leur enfant pendant une heure est un véritable défi, pour d'autres c'est une délivrance."
        "Pour ma part, c'est un peu des deux mais cette fois-ci, je me retrouve livrée avec moi-même, pensant encore à cette Slut Therapy."

    if revealing_clothes > 0 and athle_first_time_revealing_clothes:
        $ athle_first_time_revealing_clothes = False
        
        "Je ne sais pas si c'est mon imagination ou si c'est réel mais j'ai l'impression que tout le monde me regarde."

        if level == 0:
            "Je me sens ridicule mais je suppose qu'il faut en passer par là pour gagner un peu de confiance en soi."
    
    if revealing_clothes > 1:
        $relation_t += 1

        "Je m'apprête à quitter le gymnase après avoir laissé Simon, quand un garçon m'aborde."

        "Je ne l'avais encore jamais vu ici. Il a l'air jeune. Très jeune. Mais il s'avance vers moi avec une aisance presque déconcertante."

        t "Excusez-moi."

        "Il sourit. Tranquille, assuré. Ce genre de sourire qui vient d'un visage encore adolescent, mais déjà habitué à plaire."

        p "Oui ?"

        t "Je voulais juste vous dire… vous êtes absolument renversante dans cette tenue."

        "Je reste un instant sans voix."

        "Il ne détourne pas les yeux. Il ne regarde ni mes jambes, ni ma poitrine. Il me fixe avec sérieux, comme s'il venait simplement d'énoncer un fait objectif."

        "Ses traits sont encore marqués par la jeunesse : peau lisse, lèvres pleines, pommettes hautes. Mais ce regard… il n'appartient pas à un gamin."

        p "Je... Merci. C'est gentil."

        "Je ne sais pas du tout comment réagir. Je ne m'attendais pas à un tel compliment, surtout pas de la part d'un garçon aussi jeune."

        t "Je vois que vous êtes troublée. Je ne veux pas vous être désagréable."

        "Sa voix est posée. Grave pour son âge. Il se tient droit, parfaitement à l'aise, sans chercher à combler le silence."

        "Un instant, je me demande quel âge il peut bien avoir. Dix-huit ? Dix-neuf, peut-être ? Il dégage quelque chose de beaucoup plus sûr. Trop sûr."

        p "Ce n'est pas désagréable. Mais audacieux, c'est sûr."

        "Je me rends compte que je souris, malgré moi. Il a ce petit air de défi qui me plaît."

        t "J'ai tendance à penser qu'un compliment sincère ne devrait jamais attendre."

        "Il me tend la main."

        t "Maxime."

        "Je la serre, sans réfléchir. Sa paume est chaude. Il garde le contact juste un instant de trop. Pas assez pour me mettre mal à l'aise, juste assez pour troubler."

        p "Isabelle."

        "Je me souviens des défis que je dois relever. Peut-être est-ce le bon moment pour en relever un."

        label athle_first_meeting_choice:
            menu:
                "Le fixer en imaginant une scène torride":
                    if try_action(compute_cost(1), 1):
                        $ relation_t += 1
                        "Je le regarde droit dans les yeux, imaginant ses mains sur moi, sa bouche si jeune m'embrasser avec fougue."
                        "Je l'imagine me déshabiller."
                        t "J'aimerais beaucoup vous revoir. Peut-être samedi prochain ? Peut-être avant pour un café ? Si vous accepter de me donner votre numéro."
                        "Je suis abasourdie par sa proposition. Il est direct, sans détour, comme s'il avait l'habitude de ce genre de situation."
                        "Je bredouille."
                        p "Euh... D'accord, pourquoi pas ?"
                        t "Très bien, alors je te dis à bientôt Isabelle."
                    
                    else: 
                        jump athle_first_meeting_choice
                "Ne rien faire":
                    "Je me contente de le regarder, sans rien dire. Je ne sais pas quoi faire de cette situation."

                    t "Enchanté, Isabelle. Peut-être à samedi prochain ?"

                    "Et il s'éloigne sans se retourner. Comme s'il savait exactement quel effet il laissait derrière lui."

        "Je reste figée un moment."

        "Je dois avoir presque deux fois son âge et je me suis retrouvée comme une gamine face à son assurance si mûre."

    else:
        "J'arrive à toute vitesse au baby-athlé et dépose Simon qui se précipite à son cours."

        if relation_t == 0:
            # TODO
            "truc"



    return