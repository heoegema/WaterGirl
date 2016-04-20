#####phone
screen mini_phone2:


    imagebutton:
        xpos 45
        ypos 515
        action (Hide("mini_phone2"),Show("mini_phone"),Hide("phone"),Hide("mailbox"),Hide("phone_settings"),Hide("contacts")) 
        idle "gui/cell_phone/mini_phone_close.png"
        hover "gui/cell_phone/mini_phone_close.png"
  
screen mini_phone:
    

    imagebutton:
        xpos 45
        ypos 515
        action (Show("mini_phone2"),Show("phone")) 
        idle "gui/cell_phone/mini_phone[phone_choice].png"
        hover "gui/cell_phone/mini_phone[phone_choice].png"
  
    
screen phone():
    image "gui/cell_phone/wallpaper_[wallpaper].png" xpos 380
    image "gui/cell_phone/battery_wifi.png" xpos 380
    imagemap:
        xpos 380
        alpha False
        image "gui/cell_phone/phone_[phone_choice].png"
        image "gui/cell_phone/battery_wifi.png"
        ground "gui/cell_phone/wallpaper_[wallpaper].png" 
        imagemap:
            #xpos 380
            alpha False
            cache False
            ground "gui/cell_phone/icons.png" 
            hover "gui/cell_phone/icons_hover.png"
            #image "gui/cell_phone/phone_[phone_choice].png"
        
        
        #icons
            hotspot (150,80,70,80) action Show("contacts")
            hotspot (220,80,70,80) action Show("mailbox")
            hotspot (290,80,70,80) #email icon
            hotspot (150,160,70,80) #Pin Heart icon
            hotspot (220,160,70,80) #gaming icon
            hotspot (150,240,70,80) action Show("phone_settings") 
        
        ######
            imagemap:
                ground "gui/cell_phone/buttons.png"
                hover "gui/cell_phone/buttons_hover.png"
            
            #hotspot (135,450,75,50) action Hide("phone_settings")
            #hotspot (220,450,75,50) action (Hide("phone_settings"),Show("phone"))
            image "gui/cell_phone/shine.png"

        
label phone_label:
    call screen phone
    return
        

screen phone_settings():
    imagemap:
        xpos 380
        alpha False
        image "gui/cell_phone/phone_[phone_choice].png"
        image "gui/cell_phone/battery_wifi.png"
        ground "gui/cell_phone/wallpaper_[wallpaper].png" 
        
        vbox pos (160,100):
            textbutton "{size=+5}Phone Cover" style "settings_button" 
            hbox:
                
                textbutton "<" style "settings_button" action If(phone_choice <= 1, true = SetVariable("phone_choice", 1), false = SetVariable("phone_choice", phone_choice - 1))
                textbutton "Style [phone_choice]" style "settings_button"
                textbutton ">" style "settings_button" action If(phone_choice >= phone_choice_max, true = SetVariable("phone_choice", phone_choice_max), false = SetVariable("phone_choice", phone_choice + 1))
            
            text " " 
            textbutton "{size=+5}Wallpaper" style "settings_button"
            hbox:
                
                textbutton "<" style "settings_button" action If(wallpaper <= 1, true = SetVariable("wallpaper", 1), false = SetVariable("wallpaper", wallpaper - 1))
                textbutton "Style [wallpaper]" style "settings_button"
                textbutton ">" style "settings_button" action If(wallpaper >= wallpaper_max, true = SetVariable("wallpaper", wallpaper_max), false = SetVariable("wallpaper", wallpaper + 1))
                
        
        ######
        imagemap:
            ground "gui/cell_phone/buttons.png"
            hover "gui/cell_phone/buttons_hover.png"
            
            hotspot (135,450,75,50) action Hide("phone_settings")
            hotspot (220,450,75,50) action (Hide("phone_settings"),Show("phone"))
        image "gui/cell_phone/shine.png"