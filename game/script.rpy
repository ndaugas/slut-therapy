# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

call characters

call initGame

call customScreens

# The game starts here.

label start:

    call intro
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    while day <= DAY_NUMBER:
        #block of code to run

        call awakening

        show screen hud

        p "Hello, let's hide"

        hide screen hud

        $ day += 1

    return
