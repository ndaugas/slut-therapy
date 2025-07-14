define day_font = "gui/fonts/RETROACTIVE.ttf"

screen hud():
    # Day (right)
    text "Day : [DAYS[(day + DAY_OFFSET) % 7]] ([day]/28)" xpos 0.98 ypos 0.02 xanchor 1.0 yanchor 0.0 size 36 color "#FFFFFF" font day_font outlines [(2, "#000000")]

    # Visible stats
    hbox:
        xpos 0.02
        ypos 0.02
        spacing 5

        vbox:
            spacing 5
            text "Confidence"
            text "Slut level"
            text ""
        
        vbox:
            spacing 5
            bar value VariableValue("confidence", CONFIDENCE_MAX) xmaximum 200 ymaximum 20 left_bar "#008100" right_bar "#333333"
            text "[level]"
            bar value VariableValue("xp", XP_PER_LEVEL[level]) xmaximum 200 ysize 4 left_bar "#ff0000" right_bar "#333333"
        