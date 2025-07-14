init python:
    day = 0
    DAY_MAX = 28
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    DAY_OFFSET = 5

    CONFIDENCE_MAX = 5
    confidence = CONFIDENCE_MAX
    

    xp = 0
    level = 0
    XP_PER_LEVEL = [7, 21, 63]

    def gainXp(value):
        global xp, level, XP_PER_LEVEL

        xp = xp + value
        toNewLevel = XP_PER_LEVEL[level]
        if xp >= toNewLevel:
            level += 1
            xp -= toNewLevel

