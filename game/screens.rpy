# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu
    add "gui/Main Menu BG.jpg"
    
    #Imagebutton code 
    imagebutton auto "gui/start_%s.png" xpos 100 ypos 500 focus_mask True action Start()
    imagebutton auto "gui/load_%s.png" xpos 300 ypos 500 focus_mask True  action ShowMenu('load')
    imagebutton auto "gui/pref_%s.png" xpos 500 ypos 500 focus_mask True action ShowMenu('preferences')
    imagebutton auto "gui/quit_%s.png" xpos 700 ypos 500 focus_mask True action Quit(confirm=False)
    
    
init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"
        font "CaviarDreams.ttf" 

##############################################################################
# Save, Load
#
screen file_picker:
    #add "gui/menus/saveload/saveload_backdrop.png"
    imagemap:
            ground "gui/menus/saveload/saveload_backdrop.png"
            hover "gui/menus/saveload/sl_hover.png"
            
            
            idle "gui/menus/saveload/sl_ground.png"
            #selected_idle "gui/menus/saveload/sl_hover.png"
            #selected_hover "gui/menus/saveload/sl_hover.png"   
            
        

            
            cache False
            alpha False

            hotspot (150, 90, 160, 160) clicked FilePage("1")
            hotspot (150, 272, 160, 160) clicked FilePage("2")
            hotspot (150, 460, 160, 160) clicked FilePage("3")

            
            #hotspot(920,260,290,72) action MainMenu()
            #hotspot(920,330,290,72) action Quit(confirm=True)
            
            #hotspot(50,590,400,200) action Return() at buttonfade
            
            
            hotspot (335,100,380,125) clicked FileAction(1):
                use load_save_slot(number=1)
                key "save_delete" action FileDelete(1)
            hotspot (335,290,380,125)   clicked FileAction(2):
                use load_save_slot(number=2)
                key "save_delete" action FileDelete(2)
            hotspot (335,480,380,125)   clicked FileAction(3):
                use load_save_slot(number=3)
                key "save_delete" action FileDelete(3)
                
            hotspot (720,100,380,125) clicked FileAction(4):
                use load_save_slot(number=4)
                key "save_delete" action FileDelete(4)
            hotspot (720,290,380,125)   clicked FileAction(5):
                use load_save_slot(number=5)
                key "save_delete" action FileDelete(5)
            hotspot (720,480,380,125)   clicked FileAction(6):
                use load_save_slot(number=6)
                key "save_delete" action FileDelete(6)
            
            #add "ui/menus/saveload/sl_overlay.png"
            
    imagemap: 
            ground "gui/PrefMenu.png" 
            idle "gui/PrefMenu.png" 
            hover "gui/PrefMenuHoverNav.png" 
            alpha False
        
        
    #Setting up hotspots
            hotspot(136,649,114,44) action Return()
            hotspot(290,649,121,44) action ShowMenu("save") 
            hotspot(453,649,124,44) action ShowMenu("load") 
            hotspot(621,649,105, 44) action ShowMenu("preferences")  
            hotspot(767,649,95,44) action MainMenu() 
            hotspot(905,649,105,54) action Help() 
            hotspot(1049,649,106,51) action Quit() 

screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    use file_picker

        
  ##############################################
 #############                   ################
##############  LOAD SAVE SLOTS  #################
 #############                   ################
  ##############################################


         
screen load_save_slot:
    $ file_text = "%s\n %s" % (
                        
                        FileTime(number, empty=_("Empty Slot")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 120 ypos 20
    text file_text xpos 127 ypos 55 size 23 drop_shadow [(1, 2)] #font "palooka-bb.regular.ttf"
    
    
    
    
    
   
init -2 python:
               
    #config.thumbnail_width = 237
    #config.thumbnail_height = 250
    
    config.thumbnail_width = 150
    config.thumbnail_height = 85


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    #Imagemap for preferences menu 
    
    imagemap: 
        ground "gui/PrefMenuGround.png" 
        idle "gui/PrefMenuIdle.png" 
        hover "gui/PrefMenuHover.png"
        selected_idle "gui/PrefMenuSelectedIdle.png"
        selected_hover "gui/PrefMenuHover.png" 
        alpha False 
        
    #setting up hotspots 
        hotspot(148,91,121,29) action Preference("display", "window")
        hotspot(314, 92, 148, 29) action Preference("display", "fullscreen")
        hotspot(69, 223,200, 35) action Preference("skip", "all")
        hotspot(308, 224,242,35) action Preference("skip", "seen")
        hotspot(815, 224, 128, 30) action Preference("transitions", "all") 
        hotspot(981, 226, 180, 31) action Preference("transitions", "none") 
        hotspot(1008, 91, 215, 33) action Preference("after choices", "skip") 
        hotspot(760, 89,210, 33) action Preference("after choices", "stop") 
        bar pos(115,360) value Preference("auto-forward time") style "pref_slider" 
        bar pos(115, 472) value Preference("text speed") style "pref_slider" 
        bar pos(813, 360) value Preference("music volume") style "pref_slider" 
        bar pos(813, 471) value Preference("sound volume") style "pref_slider" 
    
    
    #imagemap for menu 
    
    imagemap: 
        ground "gui/PrefMenu.png" 
        idle "gui/PrefMenu.png" 
        hover "gui/PrefMenuHoverNav.png" 
        alpha False
        
        
    #Setting up hotspots
        hotspot(136,649,114,44) action Return()
        hotspot(290,649,121,44) action ShowMenu("save") 
        hotspot(453,649,124,44) action ShowMenu("load") 
        hotspot(621,649,105, 44) action ShowMenu("preferences")  
        hotspot(767,649,95,44) action MainMenu() 
        hotspot(905,649,105,54) action Help() 
        hotspot(1049,649,106,51) action Quit() 
    
#for the slider

init -2 python: 
    
    #the bar when it's full
    
    style.pref_slider.left_bar = "gui/SliderSelect.png"
    
    #the bar when it's empty 
    
    style.pref_slider.right_bar = "gui/SliderIdle.png" 
    
    #size of bar
    
    style.pref_slider.xmaximum = 387 #size of the bar (x-wise) 
    
    style.pref_slider.ymaximum = 30 #size of bar y wise
    
  


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    #image "gui/menus/backdrop.png"
    imagemap:
        ground "gui/menus/backdrop.png"
        idle "gui/menus/yesno/yesno.png"
        hover "gui/menus/yesno/yesnohover.png"
        
        #textbutton "test" xpos 250 ypos 450
        
        hotspot (250,450,360,200) action yes_action
        hotspot (700,450,360,200) action no_action

    if message == layout.ARE_YOU_SURE:
        add "gui/menus/yesno/yesno_are_you_sure.png"
        
    elif message == layout.DELETE_SAVE:
        add "gui/menus/yesno/yesno_delete_save.png"
        
    elif message == layout.OVERWRITE_SAVE:
        add "gui/menus/yesno/yesno_overwrite_save.png"
        
    #elif message == layout.LOADING:
        #add "gui/menus/yesno/yesno_loading.png"
        
    elif message == layout.QUIT:
        add "gui/menus/yesno/yesno_quit.png"
        
    #elif message == layout.MAIN_MENU:
        #add "gui/menus/yesno/yesno_main_menu.png" 
    else:
        add "gui/menus/yesno/yesno_are_you_sure.png"

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.83
        yalign 0.942

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#fff"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

