init python:
    day = 0
    DAY_MAX = 28
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    DAY_OFFSET = 4

    def add_day():
        global day, day_in_week, day_name
        day += 1
        day_in_week = (day + DAY_OFFSET)%7
        day_name = DAYS[day_in_week]

    def is_week_day():
        return day_in_week < 5

    CONFIDENCE_MAX = 5
    confidence = CONFIDENCE_MAX

    def try_action(cost, gain):
        global confidence
        if confidence < cost:
            renpy.say(None, "Vous ne vous sentez pas le courage...")
            return False
        confidence -= cost
        gain_xp(gain)
        return True
    
    def gain_confidence(gain):
        global confidence
        confidence += gain
        if confidence > CONFIDENCE_MAX:
            confidence = CONFIDENCE_MAX

    def compute_cost(original_cost):
        if original_cost <= level:
            return 0
        return original_cost - level

    xp = 0
    level = 0
    MAX_LEVEL = 4
    XP_PER_LEVEL = [7, 21, 63]
    new_level = False

    def gain_xp(value):
        global xp, level, new_level

        xp = xp + value
        toNewLevel = XP_PER_LEVEL[level]
        if xp >= toNewLevel:
            level += 1
            xp -= toNewLevel
            new_level = True

    clothes = "old"
    
    def show_isabelle(expression = "neutral", at_list=[]):
        renpy.show("isabelle_" + clothes + "_" + expression, tag="isabelle", at_list=at_list)

    NB_TASK_PER_LEVEL = 5
    TASKS_PER_SLUT_LEVEL = [
        [
            "1. Porter une jupe ou un décolleté", 
            "2. Faire une blague ou une allusion cochonne",
            "3. Fixer quelqu'un",
            "4. Prendre une soirée pour soi",
            "5. Envoyer un texto à double sens"
        ],
        [
            "1. Ne pas porter de culotte/soutien-gorge",
            "2. Toucher quelqu'un",
            "3. Parler fantasme",
            "4. Aller dans un sexshop",
            "5. Danser de façon lascive"
        ],
        [
            "1. Passer la journée avec un sex-toy",
            "2. Contact intime avec une autre personne",
            "3. Faire une proposition indécente",
            "4. Envoyer une photo indescente",
            "5. Simuler un orgasme"
        ],
        [
            "1. Etre nue dans un endroit publique",
            "2. Faire l'amour dans un endroit insolite",
            "3. Se masturber près de quelqu'un",
            "4. Faire un strip-tease",
            "5. Passer sa journée sans sous-vêtements"
        ]
    ]

    executedTasksInfo = [ [0]*NB_TASK_PER_LEVEL for i in range(MAX_LEVEL)]