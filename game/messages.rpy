##Basic Message System 1.2 provided under CC0 1.0 Universal by saguaro, includes contributions by xavimat
# http://creativecommons.org/publicdomain/zero/1.0/deed.en
# See Lemma Soft Forum for most recent version: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=19295

init python:
    #######button styles for whole game
    style.phone_button.background=Frame("gui/cell_phone/blankbox_[phone_theme].png", 50,50)
    style.phone_button.yminimum=52
    style.phone_button.xminimum=52
    style.phone_button_text.color="F3F781"
    style.phone_button_text.hover_color="fff"
    style.phone_button_text.font="Stanberry.ttf"
    style.phone_button_text.size=18
    style.phone_button_text.drop_shadow=None
    style.phone_button_text.outlines=[(1, "000", 0,0)]
    #
    style.phoneread_button.background=Frame("gui/cell_phone/blankbox_[phone_theme].png", 50,50)
    style.phoneread_button.yminimum=52
    style.phoneread_button.xminimum=52
    style.phoneread_button_text.color="fff"
    style.phoneread_button_text.hover_color="ffffbb"
    style.phoneread_button_text.font="Stanberry.ttf"
    style.phoneread_button_text.size=18
    style.phoneread_button_text.drop_shadow=None
    style.phoneread_button_text.outlines=[(1, "000", 0,0)]
    #
    style.smallphone_button.background=Frame("gui/cell_phone/blankbox_[phone_theme].png", 20,20)
    style.smallphone_button.yminimum=30
    style.smallphone_button.xminimum=30
    style.smallphone_button_text.color="000"
    style.smallphone_button_text.hover_color="663399"
    style.smallphone_button_text.font="Stanberry.ttf"
    style.smallphone_button_text.size=10
    style.smallphone_button_text.drop_shadow=None
    style.smallphone_button_text.outlines=[(1, "000", 0,0)]
    #
    style.smallphone2_button.background=Frame("gui/cell_phone/blankbox_[phone_theme].png", 20,20)
    style.smallphone2_button.yminimum=30
    style.smallphone2_button.xminimum=30
    style.smallphone2_button_text.color="F3F781"
    style.smallphone2_button_text.hover_color="663399"
    style.smallphone2_button_text.font="Stanberry.ttf"
    style.smallphone2_button_text.size=10
    style.smallphone2_button_text.drop_shadow=None
    style.smallphone2_button_text.outlines=[(1, "000", 0,0)]
    
    style.mailboxcommand_button.background=None
    style.mailboxcommand_button_text.color="F3F781"
    style.mailboxcommand_button_text.hover_color="fff"
    style.mailboxcommand_button_text.font="Stanberry.ttf"
    style.mailboxcommand_button_text.size=15
    style.mailboxcommand_button_text.drop_shadow=None
    style.mailboxcommand_button_text.outlines=[(1, "000", 0,0)]
    
    style.mailboxcommand2_button.background=None
    style.mailboxcommand2_button_text.color="000"
    style.mailboxcommand2_button_text.font="Stanberry.ttf"
    style.mailboxcommand2_button_text.size=15
    style.mailboxcommand2_button_text.drop_shadow=None
    #style.mailboxcommand2_button_text.outlines=[(1, "000", 0,0)]
    
    style.noshadow_button.background=None
    style.noshadow_text.font="Stanberry.ttf"
    style.noshadow_text.size=15
    style.noshadow_text.drop_shadow=None
    style.noshadow_text.outlines=[(1, "000", 0,0)]
    
    style.settings_button.background=None
    style.settings_button_text.font="Stanberry.ttf"
    style.settings_button_text.color="fff"
    style.settings_button_text.hover_color="ffffbb"
    style.settings_button_text.size=25
    style.settings_button_text.outlines=[(1, "000", 0,0)]
    
  
    ######color schemes
    
    
    
    import renpy.store as store
    
    reply_screen = False
    draft_screen = False

    class Mail(store.object):
        def __init__(self, subject, sender, body, reply_label=False, delay=False, view=True, read=False):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.reply_label = reply_label
            self.delay = delay
            self.view = view
            self.read = read
            if delay:
                self.queued()
            else:            
                self.deliver()  
                
        def delete(self):
            self.view = False
            renpy.restart_interaction()
            
        def deliver(self):
            if self in mail_queue:
                mail_queue.remove(self)
            mail.insert(0, self)
            
        def mark_read(self):
            self.read = True 
            renpy.restart_interaction()         
            
        def queued(self):
            mail_queue.append(self)           
            
        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)                
            reply_screen = False            
            
        def restore(self):
            self.view = True  
            renpy.restart_interaction()            

    class Contact(store.object):
        def __init__(self, name, draft_label):
            self.name = name
            self.draft_label = draft_label  
            self.add_contact()
            
        def add_contact(self):
            contacts.append(self)

        def draft(self):
            global draft_screen
            draft_screen = True
            renpy.call_in_new_context(self.draft_label, contact=self)            
            draft_screen = False
            
        def delete(self):
            contacts.remove(self)

    def add_message(subject, sender, body, reply_label=False, delay=False):
        message = Mail(subject, sender, body, reply_label, delay)
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.read:
                    return True
                else:
                    return False
                    
    def deliver_all(): 
        mail.extend(mail_queue)
        mail_queue = list()          
        
    def deliver_next():
        if mail_queue:
            mail_queue[0].deliver()

    def mark_all_read():
        unread_messages = [x for x in mail if not x.read]
        for x in unread_messages:
            x.mark_read()                

    def message_count():
        visible_messages = [x for x in mail if x.view]
        return len(visible_messages)
        
    def new_message_count():
        unread_messages = [ x for x in mail if not x.read]
        return len(unread_messages)
            
    def restore_all():
        deleted_messages = [x for x in mail if not x.view]
        for x in deleted_messages:
            x.restore()
        renpy.restart_interaction()

screen mailbox_overlay:
    hbox:
        xalign 1.0 yalign 0.0
        if new_message_count() > 0:
            textbutton "Mailbox (%d New)" % (new_message_count()) action Show("mailbox")
        else:
            textbutton "Mailbox" action Show("mailbox")

screen mailbox():
    image "gui/cell_phone/wallpaper_[wallpaper].png" xpos 380
    image "gui/cell_phone/messages.png" xpos 380
    imagemap ground "gui/cell_phone/phone_[phone_choice].png" xpos 380
        
    #tag menu
    #modal True
    default current_message = None
    $ available_drafts = [i for i in contacts if i.draft_label]    
    #frame:
    style_group "mailbox"
    vbox ypos 100:
        text "{size=+8}Inbox" xpos 610 ypos -48 style "noshadow_text"
        if new_message_count() > 0:
            text ("Messages: %d (%d unread)") % (message_count(), new_message_count())  xpos 530 ypos -50 style "noshadow_text"
        else:
            text ("Messages: %d") % message_count() xpos 530 ypos -50 style "noshadow_text"
        side "c r":
            area (527,-36,220,123)
            viewport id "message_list":
                draggable True mousewheel True
                vbox:
                    for i in mail:
                        if i.view:
                            if not i.read:
                                textbutton ("{size=+5}{b}[i.sender]{/b}{/size}" + "\n " + i.subject) action [SetScreenVariable("current_message",i), i.mark_read] xfill True style "phone_button"
                                #textbutton ("*NEW* " + i.sender + " - " + i.subject) action [SetScreenVariable("current_message",i), i.mark_read] xfill True style "phone_button"
                            else:
                                textbutton ("{size=+5}[i.sender]{/size}" + "\n " + i.subject) action SetScreenVariable("current_message",i) xfill True style "phoneread_button"
        hbox:
            null height 10
        side "c r":
            area (530,-25,220,155)
            viewport id "view_message":
                draggable True mousewheel True
                vbox:
                    
                    if current_message:
                      
                        text ("From: " + current_message.sender) style "noshadow_text"
                        text ("Subject: " + current_message.subject) style "noshadow_text"
                        text " "
                        text "{size=+5}[current_message.body]" style "noshadow_text"
                        #text current_message.body 
            #vbar value YScrollValue("view_message")
        use mailbox_commands
    ######
    imagemap:
        xpos 380
        
        ground "gui/cell_phone/buttons.png"
        hover "gui/cell_phone/buttons_hover.png"
            
        hotspot (135,450,75,50) action Hide("mailbox")
        hotspot (220,450,75,50) action (Hide("mailbox"),Show("phone"))
    image "gui/cell_phone/shine.png" xpos 380

screen mailbox_commands:
    vbox ypos -35:
        hbox:
            #if available_drafts:
                #textbutton "Draft New" action Show("contacts") style "smallphone2_button"
            #else:
                #textbutton "Draft New" action None style "smallphone_button"
            #if current_message and current_message.reply_label:
                #textbutton "Reply" action current_message.reply style "smallphone2_button"
            #else:
                #textbutton "Reply" action None style "smallphone_button"
            if current_message:
                textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)] style "mailboxcommand_button" #style "smallphone2_button"
            else:
                textbutton "Delete" action None style "mailboxcommand2_button" #style "smallphone_button" 
    #vbox ypos -35:
        #hbox:
            #if new_message_count() > 0:
                #textbutton "Mark All Read" action mark_all_read style "smallphone2_button"
            #else:
                #textbutton "Mark All Read" action None style "smallphone_button"
            #textbutton "Restore All" action restore_all style "smallphone2_button"
            #textbutton "Exit" action Hide("mailbox") style "smallphone2_button"
            
            
        
screen contacts():
    #modal True

    image "gui/cell_phone/wallpaper_[wallpaper].png" xpos 380
    imagemap: 
        ground "gui/cell_phone/phone_[phone_choice].png" xpos 380
        alpha False
        #style_group "mailbox"
       
       

        vbox pos (160,100):
            textbutton "{size=+5}Contacts" style "settings_button"
            text " "
            for name in contacts:
                if name.draft_label:
                    textbutton name.name action [name.draft, Hide("contacts")] style "settings_button"
                else:
                    textbutton name.name action None style "settings_button"
        
            
    ######
    imagemap:
        xpos 380
        
        ground "gui/cell_phone/buttons.png"
        hover "gui/cell_phone/buttons_hover.png"
            
        hotspot (135,450,75,50) action Hide("contacts")
        hotspot (220,450,75,50) action (Hide("contacts"),Show("phone"))
    image "gui/cell_phone/shine.png" xpos 380


init -2 python:
    style.mailbox = Style(style.default)
    style.mailbox_vbox.xalign = 0.5
    style.mailbox_vbox.xfill = True
    style.mailbox_hbox.xalign = 0.5
    style.mailbox_label_text.size = 30
    style.mailbox_label_text.xalign = 0.5
    style.mailbox_label.xfill = True
    style.mailbox_frame.xalign = 0.2
    style.mailbox_frame.yalign = 0.2
    style.mailbox_button_text.size = 20
    style.mailbox_button_text.font = "Stanberry.ttf"
    style.mailbox_button_text.drop_shadow=None
    
# updated choice screen    
screen choice:

    if reply_screen or draft_screen:
        # this is the menu for message replies and drafts
        frame:
            style_group "mailbox"

            vbox:
                label "Draft"
                if reply_screen:
                    text ("To: " + current_message.sender)                
                    text ("Subject: Re: " + current_message.subject)
                else:
                    text ("To: " + contact.name)
                    text ("Subject: " + message_title)
                null  height 30

                for caption, action, chosen in items:

                    if action:
                        button:
                            action action
                            style "menu_choice_button" xalign 0.5

                            text caption text_align 0.5

                    else:
                        text caption style "menu_caption"
                        
    else:
        # this is the default choice menu
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