define day_font = "gui/fonts/RETROACTIVE.ttf"

screen hud():
    # Day (right)
    text "Day : [day_name] ([day]/28)" xpos 0.98 ypos 0.02 xanchor 1.0 yanchor 0.0 size 36 color "#FFFFFF" font day_font outlines [(2, "#000000")]

    # Visible stats
    hbox:
        xpos 0.02
        ypos 0.02
        spacing 5

        vbox:
            spacing 5
            text "Courage"
            text "Slut level"
            text ""
        
        vbox:
            spacing 5
            bar value VariableValue("confidence", CONFIDENCE_MAX) xmaximum 200 ymaximum 20 left_bar "#008100" right_bar "#333333"
            text "[level]"
            bar value VariableValue("xp", XP_PER_LEVEL[level]) xmaximum 200 ysize 4 left_bar "#ff0000" right_bar "#333333"
    
    textbutton "Tâches" action Show("task_screen") xpos 0.98 ypos 0.98 xanchor 1.0 yanchor 1.0

screen task_screen():
    tag menu # Prevent several openings of the same screen

    add Solid("#00000088")
    vbox:
        xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
        spacing 10
        text "Tâches" size 36 color "#FFFFFF"
        for task in TASKS_PER_SLUT_LEVEL[level]:
            text task
        textbutton "Fermer" action Hide("task_screen") xalign 0.5
