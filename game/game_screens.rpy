screen character_selection:
    add "images/screens/blackscreen.png"

    hbox:
        align (0.5, 0.5)

        # Character 1 button
        imagebutton:
            idle "images/selection/k mirror.png"
            hover "images/selection/kmirror hover.png"
            action Jump("keiroute")
            at left

        # Character 2 button
        imagebutton:
            idle "images/selection/j mirror.png"  
            hover "images/selection/jmirror hover.png"  
            action Jump("judiroute")

        # Character 3 button
        imagebutton:
            idle "images/selection/a mirror.png"
            hover "images/selection/amirror hover.png"
            action Jump("aliroute")
            at right

label judiroute:
    call jb_start from judi_backstory
    return

label keiroute:
    call kb_start from kei_backstory
    return

label aliroute:
    # call ab_start from ali_backstory
    hide window
    show screen wiproute with fade
    pause

    show screen demothx with fade
    pause

    show screen credits with fade
    pause

    hide screen wiproute
    hide screen demothx
    hide screen credits with fade

    return

label judite:
    call jt_start from judi_triggerevent
    return

label keite:
    call kt_start from kei_triggerevent
    return

label alite:
    call at_start from ali_triggerevent
    return

screen cat_thief:
    add "cgs/catgotthatbag.png"

screen friend_comfort:
    add "cgs/comfortjudi.png"

screen judi_parkhand:
    add "cgs/judiparkhand.png"

screen judi_parkfull:
    add "cgs/judiparkfull.png"

screen tbc:
    add "screens/tbc.png"

screen wiproute:
    add "screens/wip-route.png"

screen demothx:
    add "screens/demo-thx.png"

screen credits:
    add "screens/credits.png"

label demoend:
    hide window
    show screen tbc with fade
    pause

    show screen demothx with fade
    pause

    show screen credits with fade
    pause

    hide screen tbc 
    hide screen demothx 
    hide screen credits with fade
    
    return

# choices    

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    default bar_width = 300  # Maximum width of the bar
    default elapsed_time = 0  # Tracks elapsed time for animation

    frame:
        xalign 0.5
        yalign 0.9
        xmaximum bar_width
        ymaximum 20
        background None

        # Background bar (static grey line)
        add Solid("#444444"):  # Grey color
            xsize bar_width  # Full width
            ysize 20  # Height of the bar

        # Foreground bar (dynamic red timer)
        add Solid("#FF0000"):  # Red color
            xsize int(bar_width * (time / timer_range))  # Scales based on time left
            ysize 20  # Height of the bar

    # Timer logic
    timer 0.016 repeat True action If(
        time > 0,
        true=[
            SetVariable("time", time - 0.016),
            SetVariable("elapsed_time", elapsed_time + 0.016),
        ],
        false=[
            Hide("countdown"),
            Jump(timer_jump)
        ]
    )

        
label judieyes1:
    
    label jmenu1:
        $ time = 5                           
        $ timer_range = 5                       
        $ timer_jump = 'jmenu1_slow'                 
        show screen countdown                         

        menu:
            "Open your eyes":
                hide screen countdown       
                jump demoend
            "Keep eyes closed":
                hide screen countdown  
                jump judite

    label jmenu1_slow:
        "..."
        jump demoend

label keieyes1:
    
    label kmenu1:
        $ time = 5                                     
        $ timer_range = 5                             
        $ timer_jump = 'kmenu1_slow'        
        show screen countdown   

        menu:
            "Open your eyes":
                hide screen countdown      
                jump demoend
            "Keep eyes closed":
                hide screen countdown      
                jump keite

    label kmenu1_slow:
        "..."
        jump demoend

label alieyes1:
    
    label amenu1:
        $ time = 5                                     
        $ timer_range = 5                             
        $ timer_jump = 'amenu1_slow'        
        show screen countdown   

        menu:
            "Open your eyes":
                hide screen countdown      
                jump demoend
            "Keep eyes closed":
                hide screen countdown      
                jump alite

    label amenu1_slow:
        "..."
        jump demoend