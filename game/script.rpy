# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

call characters

call initGame

call customScreens

# The game starts here.

label start:

    call intro
    
    show screen hud

    while day < DAY_MAX - 1:
        $ add_day()

        call getting_up

        
        if is_week_day():
            call weekday
        else:
            if day_in_week == 5:
                call saturday
            else:
                call sunday
            "It's the week-end"

        "Time to sleep"

        $ gain_confidence(3)

    call last_day

    return
