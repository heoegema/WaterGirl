#Water Girl 
##Notes:
#make scene changes slower
#BACKGROUNDS
#School
image bg School Gates_Morning =  "School Gates_01.jpg"
image bg School Gates_Afternoon = "School Gates_02.jpg"
image bg School Gates_Evening = "School Gates_03.jpg"
image bg Hallway A_01 = "Hallway A_01.jpg"
image bg Classroom A_01 = "Classroom A_01.jpg"
image bg School Lockers_01 = "School Lockers_01.jpg"
image bg School Cafeteria = "School Cafeteria.jpg"
image bg Roof Top Door_01 = "Roof Top Door_01.jpg"
image bg Stair Well A_01 = "Stair Well A_01.jpg"
image bg Stair Well B_01 = "Stair Well B_01.jpg"
image bg School Rooftop = "School Rooftop.jpg"
image bg School Rooftop Entrance = "School Rooftop Entrance.jpg"
image bg School Rooftop Entrance Top = "School Rooftop Entrance Top.jpg"
#Neighbourhood
image bg Swimming Pool A_1 = "Swimming Pool A (1).jpg"
image bg Swimming Pool A_2 = "Swimming Pool A (2).jpg"
image bg Neighborhood A_1 = "Neighborhood A_01.jpg" 
image bg Neighborhood A_2 = "Neighborhood A_02.jpg" 
image bg Neighborhood A_3 = "Neighborhood A_03.jpg" 
image bg Neighborhood A_4 = "Neighborhood A_04.jpg" 
image bg Park 1 = "Park A_01.jpg" 
image bg Park 2 = "Park A_02.jpg" 
image bg Park 3 = "Park A_03.jpg" 
image bg River Pathway 1 = "River Pathway_01.jpg" 
image bg River Pathway 2 = "River Pathway_02.jpg" 
image bg River Pathway 3 = "River Pathway_03.jpg" 
image bg River Pathway 4 = "River Pathway_04.jpg" 
image bg River Pathway Rain = "River Pathway_Rainy.jpg" 
#Home 
image bg Dining Table 1  = "Dining Table (1).jpg" 
image bg Dining Table 2 = "Dining Table (2).jpg" 
image bg Dining Table 3 = "Dining Table (3).jpg"
image bg Dining Table 4 = "Dining Table (4).jpg" 
image bg Hallway Entrance 1 = "Hallway Entrance (1).jpg" 
image bg Hallway Entrance 2 = "Hallway Entrance (2).jpg" 
image bg Hallway Entrance 3 = "Hallway Entrance (3).jpg" 
image bg Hallway Entrance 4 = "Hallway Entrance (4).jpg" 
image bg Kitchen = "Kitchen.png" 
image bg Living Room 1 = "Living Room (1).jpg" 
image bg Living Room 2 = "Living Room (2).jpg"
image bg Living Room 3 = "Living Room (3).jpg"
image bg Living Room 4 = "Living Room (4).jpg"
image bg MC Bedroom 1 = "MC Bedroom (1).jpg" 
image bg MC Bedroom 2 = "MC Bedroom (2).jpg" 
image bg MC Bedroom 3 = "MC Bedroom (3).jpg" 
image bg MC Bedroom 4 = "MC Bedroom (4).jpg" 
image bg M Residence 1 = "Matsuoka Residence (1).jpg" 
image bg M Residence 2 = "Matsuoka Residence (2).jpg" 
image bg M Residence 3 = "Matsuoka Residence (3).jpg" 
image bg M Residence 4 = "Matsuoka Residence (4).jpg" 
image bg Bathroom = "Bathroom.jpg" 
image bg Changeroom = "Changing Room.jpg" 
image bg Restaurant = "Restaraunt.jpg" 
image bg white = "WHITE.jpg"

#Background Effects
init: 
    
    $ flash =Fade(.25, 1.00, .75, color="fff")
#MISC.
image LOGO = "OFFICIAL LOGO.png"

#CG'S

#SPRITES
#Haruka
image Haru Neutral = im.FactorScale("Haruka Nanase_Expression_01.png", 0.85)
image Haru Happy = im.FactorScale("Haruka Nanase_Expression_02.png", 0.85)
image Haru Annoyed = im.FactorScale("Haruka Nanase_Expression_03.png", 0.85)
image Haru Worried = im.FactorScale("Haruka Nanase_Expression_04.png", 0.85)
image Haru Cry 1 = im.FactorScale("Haruka Nanase_Expression_05.png", 0.85)
image Haru Cry 2 = im.FactorScale("Haruka Nanase_Expression_06.png", 0.85)
image Haru Cry 3 = im.FactorScale("Haruka Nanase_Expression_07.png", 0.85)
image Haru Sad = im.FactorScale("Haruka Nanase_Expression_08.png", 0.85)
image Haru Bashful = im.FactorScale("Haruka Nanase_Expression_09.png", 0.85)
#Makoto
image Makoto Devious = im.FactorScale("Makoto Tachibana_Expression_01.png", 0.90) 
image Makoto Mad = im.FactorScale("Makoto Tachibana_Expression_02.png", 0.90) 
image Makoto Worried = im.FactorScale("Makoto Tachibana_Expression_03.png", 0.90) 
image Makoto Neutral = im.FactorScale("Makoto Tachibana_Expression_04.png", 0.90) 
image Makoto Sad = im.FactorScale("Makoto Tachibana_Expression_05.png", 0.90) 
image Makoto Bashful = im.FactorScale("Makoto Tachibana_Expression_06.png", 0.90) 
#Nagisa
image Nagisa Pouty = im.FactorScale("Nagisa Hazuki_Expression_01.png", 0.75)
image Nagisa Sarcastic = im.FactorScale("Nagisa Hazuki_Expression_02.png", 0.75) 
image Nagisa Upset 1 = im.FactorScale("Nagisa Hazuki_Expression_03.png", 0.75)
image Nagisa Upset 2 = im.FactorScale("Nagisa Hazuki_Expression_04.png", 0.75) 
image Nagisa Determined 1 = im.FactorScale("Nagisa Hazuki_Expression_05.png", 0.75)
image Nagisa Determined 2 = im.FactorScale("Nagisa Hazuki_Expression_06.png", 0.75)
image Nagisa Mad = im.FactorScale("Nagisa Hazuki_Expression_07.png", 0.75)
image Nagisa Bashful 1 = im.FactorScale("Nagisa Hazuki_Expression_08.png", 0.75)
image Nagisa Unamused 1 = im.FactorScale("Nagisa Hazuki_Expression_09.png", 0.75)
image Nagisa Unamused 2 = im.FactorScale("Nagisa Hazuki_Expression_10.png", 0.75)
#Rei
image Rei Neutral = im.FactorScale("Rei Ryugazaki_Expression_01.png", 0.87) 
image Rei Annoyed = im.FactorScale("Rei Ryugazaki_Expression_02.png", 0.87)  
image Rei Reassuring = im.FactorScale("Rei Ryugazaki_Expression_03.png", 0.87) 
image Rei Bashful = im.FactorScale("Rei Ryugazaki_Expression_04.png", 0.87) 
image Rei Upset = im.FactorScale("Rei Ryugazaki_Expression_05.png", 0.87)  
image Rei Sad = im.FactorScale("Rei Ryugazaki_Expression_06.png", 0.87) 
image Rei Mad = im.FactorScale("Rei Ryugazaki_Expression_07.png", 0.87) 
image Rei Mad 2= im.FactorScale("Rei Ryugazaki_Expression_08.png", 0.87) 
image Rei Cry = im.FactorScale("Rei Ryugazaki_Expression_09.png", 0.87)  
image Rei Cry 2 = im.FactorScale("Rei Ryugazaki_Expression_10.png", 0.87)  
#Rin 
image Rin Neutral = im.FactorScale("Rin Matsuoka_Expression_01.png", 0.85) 
image Rin Smile = im.FactorScale("Rin Matsuoka_Expression_02.png", 0.85) 
image Rin Annoyed = im.FactorScale("Rin Matsuoka_Expression_03.png",0.85) 
image Rin Upset = im.FactorScale("Rin Matsuoka_Expression_04.png", 0.85) 
image Rin Bashful = im.FactorScale("Rin Matsuoka_Expression_05.png", 0.85) 
image Rin Reassuring = im.FactorScale("Rin Matsuoka_Expression_06.png", 0.85) 
image Rin Cry = im.FactorScale("Rin Matsuoka_Expression_07.png", 0.85) 
image Rin Annoyed 2 = im.FactorScale("Rin Matsuoka_Expression_08.png", 0.85) 
#Sousuke 
image Sosuke Neutral 1= im.FactorScale("Sousuke Yamazaki_Expression_01.png", 0.90) 
image Sosuke Smile = im.FactorScale("Sousuke Yamazaki_Expression_02.png", 0.90) 
image Sosuke Cry = im.FactorScale("Sousuke Yamazaki_Expression_03.png", 0.90) 
image Sosuke Unsure = im.FactorScale("Sousuke Yamazaki_Expression_04.png", 0.90)  
image Sosuke Annoyed = im.FactorScale("Sousuke Yamazaki_Expression_05.png", 0.90)  
image Sosuke Worried = im.FactorScale("Sousuke Yamazaki_Expression_06.png", 0.90) 
image Sosuke Neutral 2 = im.FactorScale("Sousuke Yamazaki_Expression_07.png", 0.90)  
image Sosuke Bashful = im.FactorScale("Sousuke Yamazaki_Expression_08.png", 0.90) 
#Gou
image Gou Neutral = im.FactorScale("Gou Matsuoka_Expression_01.png",0.70)
image Gou Worried 1 = im.FactorScale("Gou Matsuoka_Expression_02.png",0.70)
image Gou Worried 2 = im.FactorScale("Gou Matsuoka_Expression_03.png",0.70)
image Gou Mad  = im.FactorScale("Gou Matsuoka_Expression_04.png",0.70)
image Gou Determined = im.FactorScale("Gou Matsuoka_Expression_05.png",0.70)
#Miho
image Miho Neutral = im.FactorScale("Miho Amakata_Expression_01.png", 0.75)
image Miho Reassuring = im.FactorScale("Miho Amakata_Expression_02.png", 0.75) 
image Miho Mad = im.FactorScale("Miho Amakata_Expression_03.png", 0.75) 
image Miho Determined = im.FactorScale("Miho Amakata_Expression_04.png", 0.75) 
image Miho Sad = im.FactorScale("Miho Amakata_Expression_05.png", 0.75) 

#ANIMATED SPRITES
#image Makoto_Neutral:
    #zoom .200
    #"Makoto Tachibana_Expression_06.1.png"
    #3
    #"Makoto Tachibana_Expression_06.2.png"
    #.15
    #repeat

# DECLARE CHARACTER NAMES USED IN THIS GAME
#OTHER CHARACTERS
define fc = Character('Female Classmate',show_two_window=True, font="CaviarDreams.ttf")
define mc = Character('Male Classmate',show_two_window=True, font="CaviarDreams.ttf")
define sm = Character('Summi', show_two_window=True, font="CaviarDreams.ttf") 
define js = Character('Jeseri', show_two_window=True, font="CaviarDreams.ttf") 
define ly = Character('Leya', show_two_window=True, font="CaviarDreams.ttf")
define bg = Character('Blonde Girl', show_two_window=True, font="CaviarDreams.ttf") 
define w = Character('Waiter', show_two_window=True, font="CaviarDreams.ttf")
#MAIN CHARACTERS
define y = Character('[povFirstName]', show_two_window=True, font="CaviarDreams.ttf")
define hn = Character('Haruka', show_two_window=True, font="CaviarDreams.ttf")
define nh = Character('Nagisa', show_two_window=True, font="CaviarDreams.ttf")
define gm = Character('Gou', show_two_window=True, font="CaviarDreams.ttf", color="#000000")
define mt = Character('Makoto', show_two_window=True, font="CaviarDreams.ttf")
define ma = Character('Miho Amakata', show_two_window=True, font="CaviarDreams.ttf")
define rr = Character('Rei', show_two_window=True, font = "CaviarDreams.ttf")
define rm = Character('Rin', show_two_window=True, font="CaviarDreams.ttf") 
define sy = Character('Sosuke', show_two_window=True, font ="CaviarDreams.ttf") 
define unknown = Character('???', show_two_window=True, font="CaviarDreams.ttf")
define d = Character(' ',)

init:
    $ haru_relationship = 0
    $ nagisa_relationship = 0
    $ gou_relationship = 0
    $ makoto_relationship = 0
    $ rei_relationship = 0
    $ rin_relationship = 0
    $ sousuke_relationship = 0
    
##PHONE##
    $ mail = []
    $ mail_queue = []
    $ contacts = []    
    
    $ phone_theme = 1
    $ phone_choice = 1
    $ phone_choice_max = 15
    $ wallpaper = 1
    $ wallpaper_max = 15
    
# THE GAMES STARTS HERE
label splashscreen:
    scene bg white 
    with Pause(1)
    
    #play sound "ping.ogg"

    show LOGO with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)

    return
    

label start:
    
    stop music
    
    scene bg white
    
    $ povFirstName = renpy.input("What is your first name?\n\n", length=15) or "Sarah"
    $ povLastName = renpy.input("What is your last name?\n\n", length=30) or "Henderson"
    $ povName = povFirstName +" "+povLastName
    
    #play nature
    
    play music "Hamari.mp3"
     
    scene bg School Gates_Morning
    with dissolve
    
    show screen mini_phone
    
    d "Standing at the door of my new school, I can feel the warmth of the sun on my shoulders."
    
    d "It does little to knock away the chill of having to adjust to a new school."
    
    d "And not one in the United States."
    
    d "Though I can only blame myself, as I signed up for the Sister City Student Exchange Program."
    
    d "And here I am in front of Iwatobi High School, surrounded by people I don’t know."
    
    d "I thought I would have walked over with the kids of my host family,
    but they had an early morning commitment. So, I had to go by myself."
    
    d "It couldn’t be helped."
    
    d "It's odd starting school so soon."
    
    d "I imagine my friends back home would be off for Labor Day weekend."
    
    d "Grilling hot dogs and running around in their swimsuits at the pool."
    
    d "I’m in my fresh new school uniform, ready to head into the complete unknown."
    
    d "Guess I’d best get moving."
    
    hide textbox
    
    scene bg School Lockers_01
    with dissolve
    
    with Pause(1)
    
    scene bg Hallway A_01
    with dissolve
    
    d "I enter in and make my way over to class 3-1 as I had been 
    instructed in the email the administration sent me."
    
    d "A young woman by the door spots me, smiles, and waves to flag me down."
    
    scene bg Classroom A_01
    with dissolve
    
    show Miho Neutral at center
    with dissolve
    
    unknown "%(povLastName)s-san? Good morning! So nice to have you in our class."
    
    unknown "I’m Amakata Miho, I’ll be your homeroom teacher."
    
    y "Good morning, Sensei. I’m glad to meet your acquaintance."
    
    d "She laughs slightly before continuing."
    show Miho Reassuring at center 
    with dissolve
    
    ma "I’m about to start class. If you wouldn’t mind, could you sit at the chair 
    next to my desk so I can introduce you?"
    
    d "I don’t really want to be introduced in such a way, but her smile and demeanor seem to urge me forward."
    
    d "I nod to her and make my way to the front as the bell rings."
    
    d "Miho gently closes the door and follows me in."
    show Miho Neutral at center
    with dissolve
    
    
    ma "Good morning class. Before we begin, I have an introduction to make."
    
    ma "As you are aware, we have a new student from the United States who has transferred in."
    
    ma "Please join me in welcoming %(povLastName)s %(povFirstName)s to our class."
    
    d "I take that as my cue to stand." 
    
    d "I bow a little and when I come back up, I notice everyone is looking at me."
    
    d "They appear mostly curious. Maybe a few are disinterested."
    
    y "Hello, my name is %(povLastName)s %(povFirstName)s. I’m from Oregon and 
    I’ll be your classmate starting today. I hope we can get along."
    
    d "Kind of standard for introductions, but sometimes the classic approach is the best."
    
    d "The class gives a small round of applause. When it dies down, Miho speaks again."
    show Miho Reassuring at center
    with dissolve 
    
    ma "Thank you everyone. %(povFirstName)s, you may take the open seat in the back by the window."
    
    d "I nod again to her and make my way to my desk."
    
    hide Miho Reassuring at center
    with dissolve
    
    d "My seating pleases me."
    
    d "I’m in the back, so no one can easily stare at me, and I get to look out the window."
    
    d "Looking at the schedule we have Geography, Language Arts, and Japanese before lunch."
    
    d "I’m pretty good at the first two subjects, and the classes go off without a hitch."
    
    d "Then we get to the Japanese lesson. I thought I had a pretty good grip on the language."
    
    d "It’s only now when I have to write it do I realize that learning by smartphone 
    applications doesn’t prepare you for putting the words to paper."
    
    d "I understand what the teacher is saying, but I’m having trouble writing any of it down."
    
    d "I’ll really need to pay attention."
    show Miho Neutral at center 
    with dissolve
    
    ma "Everyone, please put away your books and leave only a blank piece of paper with a pencil out."
    
    ma "I will administer a short quiz on basic Japanese."
    hide Miho Neutral at center 
    with dissolve
    
    d "That was not what I wanted to hear. I’m really struggling here, and a quiz already?"
    
    d "It becomes the longest 10-minute quiz I’ve ever taken."
    
    d "Also, I’m pretty sure I didn’t even come close to passing, based on my eraser marks 
    and lack of content actually written."
    show Miho Reassuring at center
    with dissolve
    
    ma "Thank you all. Please study quietly while I grade these, I’ll have them back to you just before lunch."
    
    hide Miho Reassuring at center
    with dissolve
    d "I go over my notes, which suspiciously look a lot like what I just tried to pass off as the answers to the quiz."
    
    d "That’s probably not a good sign. I shake my head sadly."
    
    d "Ten minutes later, Amakata-Sensei walks around the classroom, handing back our quizzes."
    
    d "Without looking at me, she slips mine upside down on the desk."
    
    d "Holding my breath, I flip it over to reveal what I pretty much expected."
    
    d "A failing grade, and a rather low one at that."
    
    d "The bell rings, signaling lunch. My classmates hurry to pack up and get out."
    
    d "I fold my quiz in half and sigh, slowly getting ready to go to lunch myself."
    
    unknown "Hey, you don’t look so hot. Are you okay?"
    
    d "I wasn’t expecting anyone to talk to me, being new and all.
    But a gentle voice from the right of me has emerged."
    
    y "I feel fine, thanks for asking."
    
    unknown "Are you sure? You seemed pretty upset the majority of that last hour,
    especially after we got back our quizzes."
    
    d "I hadn’t intended to look at him, but how could he know about my
    struggling with the last class already?" 
    
    d "I turn around to face him."
    
    show Makoto Neutral at center with dissolve
    
    d "I wasn’t expecting to see such a tall, good-looking guy."
    
    d "His hair has an odd, unkempt look to it that sets off his green eyes."
    
    d "I accidently lose my words in my throat for a second, which allows him to continue."
    
    unknown "If you’re having problems with Japanese I’d be glad to help you out. 
    It’s not my strongest subject, but I think I can do it."
    
    y "No, that’s okay. I can go get an independent tutor, or ask for a remedial class. 
    I don’t want to impose on you."
    
    show Makoto Sad with dissolve
    
    unknown "You wouldn’t be imposing. I mean, considering you’re an American you already speak and 
    understand spoken Japanese well. It shouldn’t be too hard to get you writing it."
    
    d "I’m not sure what kind of look I’m giving him, but it must be making him nervous, as he keeps talking 
    like he’s trying to smooth things over with me."
   
    show Makoto Neutral with dissolve
    
    unknown "I’m sorry, I haven’t even introduced myself. I’m Tachibana Makoto. I don’t mind if you just call 
    me Makoto, though. Let me help you become proficient at Japanese this year!"
    
    d "His smile is warm and infectious. Before I know it, I’m shaking his hand that he had offered in greetings."
    
    y "Thanks, but it’s okay. You don’t have to force yourself to be friends with me."
    

    show Makoto Sad at center with dissolve
    
    d "He gives me a puzzled look."
    

    show Makoto Neutral with dissolve
    
    mt "I’m not forcing myself to do that. You look like you need a friend and it just so happens 
    that I like making new friends."
    
    mt "But enough about that. We need to get to lunch! Want me to walk you to the cafeteria?"
    
    d "Glancing at the clock, lunch is already close to being half over."
    
    y "Thanks, but I’ll be okay."
    
    show Makoto Worried with dissolve
    
    mt "Look, it’s alright. You probably don’t realize it, but with how lunch rush is, 
    you’re going to have a hard time getting any food."
    
    mt "And then barely have any time to scarf it down before classes start again."

    show Makoto Neutral with dissolve
    
    y "It’s no big deal, and it can’t be helped anyway."
    
    mt "I’m certain it can be helped. In fact, how about I just share some of my lunch right here with you?"
    
    mt "I’m certain there’s enough for both of us."
    
    d "He gives me a bright smile as he pulls out a neatly-wrapped bento box."
    
    d "This feels just a little too sudden for me, and just a tiny bit awkward."
    
    d "Okay, more like I wore a bikini to a formal dinner awkward."
    
    d "But I still keep my cool."
    
    y "That’s really not necessary. I’ll manage."
    
    show Makoto Worried at center with dissolve
    
    d "Somehow."
    
    d "Any moment now my stomach will roar out what a lie that was."
    
    mt "But really I don’t..."
    
    y "Thanksgottagoseeyoulaterbye."
    
    d "I quickly turn on my heel and leave the room, heading in the direction of the cafeteria."
    
    scene bg Hallway A_01
    with dissolve
    
    with Pause(1)
    
    d "That went well."
    
    d "Really."
    
    d "I’m sure I didn’t come off like a stuck up jerk, right?"
    
    d "I mean, he seemed way too desperate to get friendly with me."
    
    d "I’m clearly not ready for it, and probably not with someone that forward."
    
    d "Best get lunch. There’s the cafeteria."
    
    scene bg School Cafeteria
    with dissolve
    
    with Pause(1)
    
    y "Oh… No…"
    
    d "With this crowd, maybe I should have had some of Makoto’s lunch."
    
    d "I can’t even see the servers from my spot in line."
    
    d "And it appears they aren’t very familiar with “No Cutting” rules in Japan."
    
    d "I keep getting shoved and pushed around like a tackling dummy."
    
    d "I really hope I can keep hold of my spleen and other vital parts in this mess."
    
    d "When I finally get out, all I’ve managed to obtain is one piece of melon bread."
    
    d "And I think it’s from yesterday, if the packaging is correct."
    
    d "No way in hell am I staying in this madhouse."
    
    d "If everything I’ve learned from Japanese entertainment is correct, I should be 
    able to get to the roof and eat my bread there."
    
    stop music
    with dissolve
    
    scene bg Stair Well A_01
    with dissolve
    
    with Pause(1)
    
    scene bg Stair Well B_01
    with dissolve
    
    with Pause (1)
    
    scene bg Roof Top Door_01
    with dissolve
    
    with Pause (1)
    
    play music "Lull.mp3"
    with dissolve
    
    d "Hey, there’s the stairs to the roof. And the door up above is open."
    
    d "Convenient! Something’s going right for once."
    
    d "Stepping outside the crisp autumn air refreshes me from the trials of the morning."
    
    scene bg School Rooftop
    with dissolve
    
    with Pause (1)
    
    d "I break open my slightly squished melon bread and take a bite, enjoying the silence of the 
    empty rooftop and the view of the cherry trees nearby."
    
    d "Been quite a morning so far. Flunked a quiz, fended off a weird guy, got tossed 
    around the cafeteria and flunked a quiz."
                                 
    d "Seems I have a lot of adjusting to do."
    
    d "I have a bad habit of talking to myself. Probably a result of no one else talking to me for a 
    good chunk of my formative years."
    
    d "Working my way through my bread, I hear a faint noise somewhere behind me."
    
    d "But looking back I see nothing. Maybe a bird took off or something."
    
    d "No, there it is again. And I don’t see any birds around here. Maybe a plastic bottle being crunched?"
    
    d "Curiosity gets the better of me and I make my way slowly back towards the entrance."
    
    scene bg School Rooftop Entrance
    with dissolve
    
    d "There it is again. I’m on the right track."
    
    d "Seems like it’s coming from up above the entrance door to the roof, which in itself is situated on a corner 
    and is built like a small shed, having a roof of its own."
    
    d "The noise is coming from up there. But I don’t see a way up."
    
    y "It’s not a huge height, I think I can grab the ledge and pull myself up if I get a running start."
    
    d "Why am I talking to myself again?"
    
    d "I step back a bit, get a good running start and leap as high as I can, grabbing the edge of the 
    entrance door’s roof. "
    
    d "With some effort, I pull myself on top."
    
    scene bg School Rooftop Entrance Top
    with dissolve
    
    d "For some reason, I’m thankful no one was here to look up my skirt, since 
    I’m sure it flipped during all of that."
    
    d "Once situated, I see the silhouette of what appears to be a slender, muscular young man."
    
    d "His back is to me. And if he knows I’m there he’s made no motion to show it."
    
    d "I start walking to him, but my first step manages to land on top of a crunched water bottle, 
    which catches his attention. He turns around to look at me."
    
    show Haru Neutral at center
    with dissolve
    
    d "He’s handsome. Dark eyes and hair. Definitely athletic with the way 
    his uniform accentuates his lean build."
    
    d "And he’s also a mute. Or a mime. I’m not sure which, but he hasn’t bothered to say 
    anything to a girl who appeared out of nowhere."
    
    d "Guess it’s up to me to break the ice."
    
    y "You really shouldn’t leave your trash on the ground."
    
    d "He just looks at me and says nothing."
    
    y "Hey, litterbug, just who are you?"
    
    unknown "..."
    show Haru Sad at center 
    with dissolve
    
    d "He finally opens his mouth and says something, but he’s barely audible."
    
    y "You mind speaking up for those of us who can’t translate the language of the wind?"
    
   
    show Haru Annoyed at center
    with dissolve
    
    unknown "You’re too loud."
    
    y "That’s it? You respond to a question to tell someone they’re too loud? 
    Were you raised in a monastery or something?"
   
    show Haru Neutral at center
    with dissolve
    
    d "He just turns back around and starts gazing over the roof again."
    
    d "I’m getting really pissed off with this guy. Not only does he leave his trash on the ground, 
    but he’s rude and doesn’t even answer a simple question like what his name is."

    d "I step towards him, and the faint sound of water splashing hits my ears."
    
    scene bg Swimming Pool A_2
    with dissolve
    
    d "Looking down, I see the medium sized swimming pool in the school courtyard."
    
    d "It’s right below us, but really far down."
    
    scene bg School Rooftop Entrance Top
    with dissolve
    
    d "I’m about to ask why he’s looking at it when a different noise is made next to me."
    
    d "Turning to face it, I’m completely shocked."
    
    y "WHAT IN THE WORLD ARE YOU DOING?"
    
    play music "Scheming Weasel Faster.mp3"
    
    unknown "What do you mean?"
    
    d "This guy already has his shirt unbutton and his belt buckle undone. 
    He’s stripping right here in front of me on the roof for God knows what reason."
    
    y "WHAT DO I MEAN? WHY ARE YOU STRIPPING IN PUBLIC? STOP THAT!"
    
    d "I’m blushing slightly, but I move to stop this guy from stripping down."
    
    d "Which might not be the brightest idea, as I don’t know why he’s decided to go 
    all natural right here, right now."
    
    d "I’m not the strongest person out there, but I’ve caught him 
    off-guard and he was still trying to undress."
    
    d "As a result, he struggles under my grip and loses his balance, pulling me on top of his bare chest."
    
    scene bg School Rooftop Entrance Top
    with vpunch
    
    d "My first thought is how smooth his abs are."
    
    d "My second thought is what in the heck is going on?"
    
    d "I’ll bet my face is as red as the rising sun on the Japanese flag right now."
    
    show Haru Annoyed at center
    with dissolve
    
    unknown "Ouch. That hurt, you know?"
    
    d "The fact that he’s half naked with a girl on top of him doesn’t even seem to phase him."

    d "That pretty much flips the switch into overdrive."
    
    y "You… You… PERVERT!!! STRIPPING IN PUBLIC!!!"
    
    d "I raise my hand to slap him, but he seems to have anticipated that and 
    grabs it before I can get near his cheek."
    
    unknown "Why are you trying to slap me? And why are you calling me a pervert?"
    
    d "This guy seriously doesn’t get it."
    
    y "Why? WHY? Because you’re getting naked in public in front of me. Why are you stripping down?"
    
    d "He looks back in the direction of the pool."
    show Haru Sad at center
    with dissolve
    
    unknown "I just wanted to go for a swim."
    
    y "Swim? Seriously? And how were you going to do that? Jump?"

    d "He’s still looking at the pool."
    
    y "You seriously were going to jump all the way in from here? You could have been killed!"
    
    d "I mean to go on, but the bell rings, signaling the end of lunch."
    
    d "He quickly gets dressed and heads away from me."
    
    show Haru Neutral at center
    with dissolve
    
    unknown "Lunch is over. Next time, use the ladder."
    
    d "There’s a ladder? I guess so since he’s climbing down."
    
    d "Why didn’t I see it before?"
    
    d "My stomach is growling at me as I climb down and head back towards class."
    
    stop music
    
    scene bg School Rooftop Entrance
    with dissolve
    
    with Pause(1)
    
    scene bg Stair Well B_01
    with dissolve
    
    with Pause(1)
    
    scene bg Stair Well A_01
    with dissolve
    
    with Pause(1)
    
    scene bg Hallway A_01
    with dissolve
    
    with Pause(1)
    
    play music "Hamari.mp3"
    
    d "I barely ate anything at all."
    
    d "And I didn’t even get that strange kid’s name."
    
    d "I guess if I have the misfortune of running into him again, I could call him Litterbug."
    
    d "Or Jumper. Or Stripper."
    
    d "I hope not all Japanese males are as weird as the two I’ve spoken with so far."
    
    scene bg Classroom A_01
    with dissolve
    
    with Pause(1)
    
    d "Back in class I take my assigned seat."
    
    d "Makoto isn’t in his seat for some reason."
    
    d "I’m kind of glad in a way, as it was already awkward at lunch with him."
    
    show Miho Neutral at center
    with dissolve
    
    ma "Okay class, we’ll now begin Classical Lite…"
    
    d "The door opens and Makoto steps in."
    
    show Miho Neutral at left with dissolve
    
    show Makoto Worried with dissolve
    
    mt "Excuse our tardiness, Ama-chan."
    
    show Miho Mad with dissolve
    
    ma "Makoto, I hope you have a good explanation for this."
    
    mt "I don’t know if it’s good as opposed to typical."
    
    mt "I managed to wrangle him back to class again, though."
    
    d "So aside from offering new girls lunch, Makoto also rounds up truants. I wonder who he caught?"
    
    mt "I guess Haru lost track of time again, teacher."
    
    show Haru Neutral at right with dissolve
    
    hn "Pool."
    
    d "Why am I not surprised he dragged clueless Litterbug into class? 
    Of course both weirdos would be in the same homeroom with me."
    
    ma "Nanase-kun, physical education comes AFTER classical literature, not before it. Please go take your seat."
    
    hide Miho
    hide Makoto
    hide Haru
    
    d "The two boys walk back. I’m not surprised at Makoto sitting next to me, but Stripper takes 
    the seat immediately behind me. I turn and point at his face."
    
    show Haru Neutral at center with dissolve
    
    y "What in the world are you doing here now?"
    
    unknown "This is my homeroom."
    
    show Makoto Neutral at right with dissolve
    
    mt "Oh, have you two met already?"
    
    y "We’re acquainted. So intimately acquainted that I don’t know his name."
    
    mt "That’s Nanase Haruka. He seems a bit standoffish but he’s a really cool guy. He’s really into water and…"
    
    y "Stripping?"
    
    hide Makoto
    show Makoto Sad at right
    with dissolve
    
    with Pause(1)
        
    show Makoto Neutral at right
    with dissolve
    
    d "Makoto furrows his brow but also chuckles."
    
    mt "Oh so you’ve seen that? Yeah, Haruka kind of has a habit of stripping down every so often when he gets near water."
    
    show Miho Mad at left with dissolve
    
    ma "Tachibana-kun, I’m glad you’re getting so familiar with our new exchange student, but I’d appreciate it if you’d wait until after class for it."
    show Makoto Worried at right with dissolve
    mt "Apologies Ama-chan. I’ll be more mindful of the lesson."
    
    hide Miho
    hide Makoto
    hide Haru
    
    d "Great. Just great. The two people sitting closest to me are friends, compatriots and absolute weirdos."
    
    d "And the school year is only getting started."
    
    d "Time really does seem to have a way of making you miserable."
    
    d "The phrase ‘Time flies while you’re having fun’ comes to mind."
    
    d "Since this day has not been fun so far, time has done anything but fly."
    
    d "Limp, stagger, crawl or freeze would all be better descriptions for class after lunch."
    
    d "I don’t think it was just me."
    
    d "I swear I think I heard Haru snoring behind me during English."
    
    d "A nap doesn’t seem like a bad idea right about now, but I don’t think I want to start that habit on just my first day."
    
    d "Finally, after what feels like an entire semester, the bell rings."
    
    ma "Do not forget to do the assigned homework tonight. It will be graded."
    
    d "That shouldn’t pose too much of a problem, as I don’t have anything else to do."
    
    d "I slowly start gathering my things into my bookbag."
    
    d "It appears Strip… I mean Haru has already left."
    
    d "He’s probably already half naked and looking for the deadliest way to enter the pool."
    
    d "I feel as if I’m forgetting something…"
    
    show Makoto Neutral at center with dissolve
    
    mt "%(povFirstName)s-chan, I have some spare time before my club starts."
    
    mt "Would you like me to walk you home?"
    
    d "He gives a bright smile that’s kind of infectious."
    
    d "I can almost feel a smile coming across my lips."
    
    d "Still, this guy doesn’t give up, does he?"
    
    y "It’s okay, Makoto-kun, but I don’t want to make you late for your club."
    
    mt "No really, it’s not a bother at all."

    show Makoto Sad at center 
    with dissolve
    
    mt "I mean, you don’t seem to have spoken to anyone today."
    
    mt "I would hate for you to feel lonesome during your stay in Japan."
    
    mt "So please, let me have the honor of walking you home."
    
    y "Really, that’s quite alright."
    
    y "Besides, shouldn’t you be looking for Haru?"
    
    y "Who knows how many young minds he’s defiling by stripping in public right now?"
    
   
    show Makoto Worried at center
    with dissolve
    
    mt "Haru? Ha! No need to worry about him."
    
    mt "I don’t think there’s a female at this school who hasn’t seen him strip to his trunks."
    
    show Makoto Neutral at center
    with dissolve
    
    mt "So let’s go! I can show you some interesting places along the way."
    
    mt "Like where to get the newest manga and the sweetest red bean paste buns."
    
    show Makoto Worried at center 
    with dissolve
    
    mt "Though they’re not in the same shop."
    
    mt "I mean obviously a book seller isn’t going to have baked goods."

    show Makoto Neutral at center
    with dissolve
    
    mt "Sorry for rambling. Anyway, let’s go!"
    
    d "He offers out his arm as to escort me from the room."
    
    d "I don’t think he’s noticed my shortness of breath."
    
    d "Though I’m not sure if it’s from anxiety or how cute he is."
    
    d "Either way, I need to get out of here."
    menu:
        "Push past his arm quickly.":
            
                d "I’ve really got to get out of here."
    
                d "I’ve never dealt with such forward people very well, and this is just getting too uncomfortable."
    
                d "I quickly get the rest of my stuff into my bookbag and head off."
    
                d "I push past his arm as quickly as I can and head for the exit."
    
                d "He kind of gives a grunt as I push past him, but doesn’t say anything."   
                show Makoto Sad at center 
                with dissolve
    
                y "I’ve really got to go, Makoto."
    
                y "Good luck finding the naked kid."
                
                show Makoto Neutral at center
                with dissolve
       
                d "I think I heard him chuckle just a little."
      
                d "What I heard better was some of the other classmates talking."
    
                fc "Well that was rude of her."
    
                mc "What's her problem? Are all Americans so unfriendly?"
    
                fc "And to Makoto-kun! He's so sweet, I wish he'd walk me home."
    
                d "Maybe I shouldn't have been so abrupt to him."
    
                d "My anxiety got the better of me."
    
                d "I should really try to calm down."
    
                d "But there's not much I can about it now."
    
                d "All I can do is head for my locker and meet up with my host sister."
                
                jump makoto_jump_1

        "Carefully walk around him.":
            
            d "I need to keep my composure here."
            
            d "Yes, Makoto is coming off way too strong, but he doesn’t seem to be a bad guy or anything."
            
            d "Just a tad pushy."
            
            d "I gather up the rest of my things while still speaking."
            
            y "I appreciate the offer Makoto-kun, but it’s a bit early for that sort of thing just yet."
            show Makoto Sad at center
            with dissolve
            
            mt "I’m not quite sure I understand what you mean."
            
            mt "Too early for what sort of thing?"
            
            y "Oh you know, escorting me home, looking at each other with adoration..."
            
            d "I’m certain I sound like an idiot. But I keep moving."
            
            d "Carefully, I slide around him, taking care not to bump him or anything."
            
            y "Oh, and I already promised my host sister to go home with her."
            
            y "She had to leave early and wasn’t able to bring me to school."
            
            y "So she wanted to make sure she got to walk me home."
            
            y "You understand right?"
            show Makoto Neutral at center with dissolve
          
            mt "Oh, that’s all? Why didn’t you say so?"
            
            d "He gives another one of his award-winning smiles to me."
            
            mt "I understand completely. You’ll want to get to know each other better."
            
            mt "I can take you home another day."
            
            mt "Have fun!"
            
            y "I will! Have a nice club practice!"
            
            d "That went better than I had hoped."
            
            d "I’d better go meet my host sister at the lockers now."
            
            d "She’s probably been waiting while I was talking with Makoto."
            
            jump makoto_jump_1  
   
        
label makoto_jump_1:
    
    stop music
    
    scene bg Hallway A_01
    with dissolve
    
    with Pause (1)
    
    scene bg School Lockers_01
    with dissolve
    
    with Pause (1)
    
    play music "Lazy Days.mp3"
    
    d "Fortunately it’s not too long a walk to my locker, and the school was even 
    considerate enough to put it next to my host sister’s locker." 
    
    d "Standing there waiting is Matsuoka Gou."
    
    d "I hope I remember to say her name correctly."
    
    d "I’m not sure why her parents decided to give her such a boyish name, 
    but I know it bothers her when said in the masculine tone."
    
    d "She’s flagging me down now."
    
    show Gou Neutral at center
    with dissolve
    
    gm "%(povFirstName)s-san!"
    
    gm "Finally, I get to see you for a few minutes!"
    
    show Gou Worried 1 at center
    with dissolve
    
    gm "Club is starting a bit late today."
    
    gm "Our supervisor had some urgent errands to run right after class, 
    so I thought I might take you to get a snack on the way to taking you home."
    
    y "Gou-senpai! I’m so happy to see you after the way this day went."
    
    d "I start changing books around in my locker 
    and bookbag for going home as she continues."
    
    show Gou Neutral at center
    with dissolve
    
    gm "No need to call me senpai, you’re a year ahead of me.
    So not a great start today, I take it?"
    
    y "It had its ups and downs, along with general oddness."
    
    y "I found I’m not nearly as proficient at writing Japanese as I need to be.
    And this one guy in my class was really persistent in trying to befriend me."
    
    y "Kind of in an over-the-top way, really."
    
    gm "I hope you weren’t too hard on him."
    

    show Gou Worried 1 at center
    with dissolve
    
    gm "Most of the guys here are pretty cool, even if overly friendly."
    

    show Gou Neutral at center
    with dissolve
    
    y "He wasn’t even the oddest person I met today."
    
    y "I needed some air at lunch so I went to the roof, 
    and this one kid just started stripping out of nowhere."
    
    y "When I found out why, it was because he was going to dive 
    to his death in the school pool."
    
    show Gou Worried 1 at center
    with dissolve
    
    d "I was expecting a reaction out of Gou, but I wasn’t expecting 
    a deep belly laugh."
    
    y "I’m glad you find that funny."
    
    y "If you don’t mind, could you let me in on the joke?"
    
    gm "Hold on… Hahahaha… Ha ha ha…"
    
    gm "Give me a minute…"
    
    gm "…Ha ha… Not even a full day in and you’ve already gotten the Haru 
    experience."
    
 
    show Gou Determined with dissolve
    
    gm "Classic."
    
    y "Come to think of it, that Makoto kid did say Haru 
    was known to do that on occasion."
    
    gm "If by ‘on occasion’ you mean ‘any time Haruka-senpai is near a 
    discernable amount of water’, then you’d be correct."
    
    gm "And did I hear you mention Makoto-kun?"
    
    y "Yeah, he’s the overly-friendly guy I mentioned earlier."
    
    y "It appears they’re both in my homeroom."
    
    show Gou Neutral at center
    with dissolve
    
    gm "So you’re in Ama-chan’s class then?"
    
    y "That’s an awfully familiar way to address a teacher."
    
    y "Won’t she get angry?"
    
    gm "Nah, not at all."
    
    gm "Tell you what, change of plans."
    
    gm "You’re coming with me to club today."
    
    y "Uhm, okay, not that I mind, but why?"
    
    gm "Remember this morning before I left 
    I mentioned that I’m a manager of a club at school?"
    
    d "She reminds me of this as she takes me by the hand."
    
    y "You did, but you never mentioned which one."
    
    gm "Hey have you ever swam before?"
    
    y "You mean, like competitively? Or in general?"
    
    gm "Either works."
    
    y "It’s been awhile but when I was in elementary school I swam a lot."
    
    y "I was actually pretty decent at it."
    
    y "I earned my fair share of ribbons and medals at summer camp swim meets."
    
    show Gou Determined at center
    with dissolve
    
    gm "Oh even better."
    
    y "Uhm, why is that even better?"
    
    gm "Because now you won’t have to go home after school."
    
    gm "You’ve got a club already waiting for you, and they need you in particular."
    
    # transitions to roof where pool is (2) with dissolve
    
    d "I notice we’re almost at the door that leads to…"
    
    y "Why are you taking me to the pool?"
    
    gm "Because that’s the club I manage, and the one you’re about to join."
    
    scene bg Swimming Pool A_2
    with dissolve
    
    d "She pushes open the door to reveal the gorgeous outdoor school pool."
    
    y "Whoa whoa whoa. Whoa. That’s a bad idea."
    
    y "Like really bad."
    
    y "I'm terrible at group events."
    
    show Gou Determined at center 
    with dissolve
    
    gm "Bah. You’ll get over it."
    
    gm "I’ll be here the whole time with you."
   
    show Gou Neutral with dissolve
    
    gm "And the club needs to add some girl swimmers to maximize points at meets."
    
    gm "Besides, you need friends and involvement."
    
    d "She pulls me outside to the pool."
    
    d "Currently, there are four members hanging around the edge."
    hide Gou
    show Haru Neutral at left with dissolve
    show Gou Neutral at right with dissolve
    
    d "All males."
    
    d "All very good looking males."
    
    d "I’m pretty sure my face is flushed right now."
    
    show Makoto Neutral at center
    with dissolve
    
    mt "Gou! You managed to convince %(povFirstName)s-chan to come check out our club!"
    
    d "Oh no. No wonder she was so familiar with Makoto."
   
    show Gou Worried 1 at right with dissolve
   
    gm "And you already know Haru over there, who’s been in the water since 
    10 seconds before the end-of-day bell rang."
    
    gm "Say hi, Haru!"
    
    hn "..."
    
    gm "He’s a man of few words. You’ll get used to it."
    hide Gou
    hide Makoto
    show Makoto Neutral at right with dissolve
    
    show Nagisa Determined 1 at center
    with dissolve
    
    unknown "Well, let me say what Haru should be saying."
    
    unknown "Thanks for bringing this cutie to the pool with you."
    
    d "A blonde male about my height is standing next to me."
    
    d "If I’m not mistaken, I think he’s checking me out."
    
    d "As in I think he’s trying to guess what cup size I am in his head."
    
    y "Who’s the rude kid?"
    
    hide Haru
    show Gou Worried 1 at left with dissolve
    
    gm "Oh, that’s Hazuki Nagisa."
    
    gm "He kind of has a tendency to speak first and then speak some more later."
    
    gm "Don’t worry though, he’s not a pervert or anything."
    
    gm "Well, at least not much of one."
    
    y "I’ll keep that in mind."
    
    d "That leaves just the guy over on the 
    bleachers working on his calculus homework."
    show Gou Neutral at left with dissolve
    
    d "As if reading my mind, Gou points him to me."
    
    gm "That’s Ryugazaki Rei, the quiet one over there."
    
    gm "When he’s not swimming he’s usually doing some sort of mathematics."
    
    d "He looks up at the sound of his name and 
    waves at me before going back to his studies."
    
    y "Well it was very nice to meet everyone."
    
    y "But I should be heading home."
    
    y "You guys have practice and I have homework."
    
    show Gou Determined at left with dissolve
    
    gm "Homework can wait."
    
    gm "I’m serious, I think you should become the first 
    female member of the Iwatobi High School Swimming Club."
    
    gm "You yourself said you used to be good at swimming."
    
    gm "And this will give you a chance to socialize 
    and make the most of your time in Japan."
    
    gm "Wouldn’t you agree, Ama-chan?"
    
    hide Nagisa
    show Makoto Neutral at center 
    with dissolve
    
    show Miho Neutral at right
    with dissolve
    
    d "I hadn’t realized it, but while I was being 
    introduced, Amakata-sensei had arrived behind us."
    
    ma "I think it’s a fabulous idea!"
    
    ma "And we really do need to get some female members in here."
    
    ma "Just think, as a foreigner your name would appear as the 
    very first female member of the club."
    
    ma "How cool does that sound?"
    
    d "I’m shocked, and I’m not really sure how to respond."
    
    y "..."
    
    scene bg School Gates_Afternoon with dissolve 
    scene bg Neighborhood A_2 with dissolve     
    d "It's nice to finally be on the way back to my host's home again." 
    
    d "After the long, crazy day I've had, I want nothing more than to just flop on my bed and get a good nap." 
    
    d "Maybe wake up and take a soak in the bathtub as well." 
    
    d "I just can't wait to do that. My body is practically begging my mind to obey." 
    
    d "But it looks like I'll have other plans..." 
    
    show Makoto Neutral at right with dissolve
    
    show Haru Neutral at left with dissolve
    
    mt "And after all that I still get to walk you home!" 
    
    
    hn "..." 
    
    d "Thinking back I probably should have figured out this would be the end result of the day." 
    
    d "Not that it was my intention or anything." 
    
    d "But when Gou gets an idea in her head, it appears it's hard to go against her." 
    
    scene bg Swimming Pool A_2 with flash 
    
    show Gou Determined at left with dissolve 
    show Miho Neutral at right with dissolve
    
    gm "I think you should become the first female member of the Iwatobi High School Swimming Club." 
    
    show Gou Neutral with dissolve 
    
    gm "This will give you a chance to socialize and make the most of your time in Japan." 
    
    ma "I think it's a fabulous idea!" 
    
    ma "Just think, as a foreigner your name would appear as the very first female member of the club." 
    
    ma "How cool does that sound?"
    
    y "But it's been ages since I've actually been in a swim competition. Are you really wanting me to disgrace the school by coming in last all the time?"
    
    d "I was hoping to work their competitive nature against them and free myself. No dice." 
    
    rr "Actually just having swam before you'd be further ahead of me when I joined." 
    hide Gou 
    hide Miho
    
    show Rei Neutral at center with dissolve
    
    d "Wait a minute, when did he pop his head up from his calculus book?" 
    
    show Rei Reassuring with dissolve
    
    rr "I actually ran track my first year here, and I'd never swam before. It took a while before I could even compete for last place." 
    
    y "So you gave up track to do something you'd never done before?" 
    
    show Rei Bashful with dissolve
    
    rr "What can I say? There's a certain beauty to swimming missing from running." 
    
    rr "Especially when the competitor has the potential for world-class talent." 
    
    d "He appears to be glancing at Haru as he says this." 
    
    y "I'm just not sure I'm ready to do this." 
    
    show Nagisa Pouty at right with dissolve
    show Rei Bashful at left with moveoutleft 
    
    nh "Why not! You're here. You know how to swim. You have people who want you around!" 
    
    nh "So like, carne diet or whatever it is Americans say!" 
    
    y "I think you just told me to become a carnivore in really bad Tex-Mex." 
    
    nh "You know what I Mean. Dive in-literally!" 
    
    y "But I didn't even pack a swimsuit, I mean, I brought my tennis racket on the off-chance of joining the tennis club... But I left my swimsuit at home." 
    
    hide Nagisa with dissolve
    hide Rei with dissolve
    show Gou Determined at center with dissolve
    
    gm "But that's not a problem!" 
    
    gm "We can get you a swimsuit, the only guidelines are it has our school symbol on it, it has to be a one piece and the main color be black like the rest of the team..." 
    
    gm "But you can have whatever color trim you want." 
    
    y "But..." 
    
    show Gou Worried 1 with dissolve
    
    gm "Please, I'll feel like a bad hostess if I let you become a member of the Just Go Home Club." 
    
    y "Is there really a club for that?"
    
    y "I always thought it was a joke, but if there's a club for that, point me towards it." 
    
    d "I thought my joke was kind of funny, but the reaction I got was not from whom I expected." 
    
    hide Gou 
    
    show Haru Annoyed at center with dissolve   
    hn "Coward." 
    
    y "Wait... What did you just say?"
    
    hn "..." 
    
    show Makoto Worried at right with dissolve
    
    mt "That might have been a little too far there, Haru..." 
    
    mt "Maybe you should apologize." 
    
    hn "No." 
    
    d "Well now I'm seriously pissed at this kid." 
    
    y "Coward? COWARD? I'll show you, Naked Boy." 
    
    y "I'll jump in that pool and whoop your butt in a race by the end of the year!" 
    
    show Haru Neutral with dissolve
    
    hn "Good luck." 
    
    hide Haru with dissolve
    hide Makoto with dissolve
    
    d "With that he walks off. I think I saw him smile just a bit as well." 
    
    show Miho Neutral at center with dissolve
    
    ma "And with that, the Iwatobi Swim Club officially has its first female member!"
    
    ma "Welcome to the team, %(povLastName)s-chan!" 
    
    scene bg Neighborhood A_2 with flash 
    
    d "Me and my big mouth. With that slip of tongue in anger, I was now part of the swim club." 
    
    d "Gou and Miho wasted no time ushering me to the back to get my size and measurements for a suit." 
    
    d "I told them I wanted gray trim, but I get the feeling they'll end up making it yellow or pink." 
    
    d "I have to fill out some forms and the nurse gave me a general check-up. Finding nothing wrong phsyically, she cleared me for swimming against my better protests." 
    
    d "Gou then instructed Makoto and Haru to walk me home, as she had some errands to run."
    
    d "One being getting my swimsuit ordered..." 
    
    d "She also mentioned dropping off some things for her older brother at a different school." 
    
    scene bg Swimming Pool A_2 with flash 
    
    show Gou Neutral at left with dissolve 
    
    show Makoto Neutral at right with dissolve
    
    gm "Makoto, could you make sure to get %(povFirstName)s home?" 
    
    show Gou Determined with dissolve
    
    gm "I don't think we want her getting lost on her way back. Or trying to escape by jumping a ship at the harbor." 
    
    y "I heard that!" 
    
    mt "Just leave it to me and Haru, we'll get her back to your house safe!" 
    
    gm "Great! I'll tell Rin you said hi." 
    
    scene bg Neighborhood A_2 with flash 
    
    d "And so here we are, the three of us misfits, walking back to Rin's place." 
    
    d "I guess it's technically my place for the time being as well." 
    
    d "It's kind of tense walking home, and Makoto is trying his best to make conversation."
    
    d "It's just so awkward..." 
    
    show Makoto Mad at right with dissolve
    
    show Haru Neutral at left with dissolve
    
    mt "Haru, did you know what you were doing when you taunted %(povFirstName)s?"
    
    show Makoto Worried with dissolve
    
    mt "I mean, that seemed kind of cold..." 
    
    hn "It was what it was." 
    
    d "That may be a record for the most words in a sentence from Haru." 
    
    d "The awkwardness continues into silence..." 
    
    d "That is until my phone decides to pipe up." 
    
    unknown "Mistress, our quest for the chalice awaits!" 
    
    show Makoto Bashful with dissolve
    
    d "Oh man, I had forgotten I had set the alerts for when my quest energy was full." 
    
    d "Makoto is grinning at me right now." 
    
    mt "Was that what I think it was?"
    
    y "No, I'm pretty sure you're imagining things." 
    
    show Makoto Devious with dissolve
    
    mt "That was an alert from 'Destiny's Ultimate Challenge', wasn't it?"
    
    y "I have no idea what you're talking about." 
    
    d "Makoto is now going through his side pocket." 
    
    d "He pulls out his smartphone and starts tapping. A couple of minutes later he hands it to me." 
    
    d "A familiar start screen brightens the face of his phone." 
    
    y "Okay, okay. Yes, that was an alert from DUC." 
    
    y "...I liked the visual novel and wanted to play the app...." 
    
    y "I had to backdoor my way into the app since it's only available from the App Center in Japan." 
    
    y "So yes... I'm a dork." 
    
    show Makoto Neutral with dissolve
    
    mt "Dork? Then I guess you fit in with us even more. We play it!" 
    
    mt "Even Haru over there, when he isn't climbing into a fountain or something." 
    
    d "Hitting the start key reveals Makoto's character screen." 
    
    y "Oh man! How did you get the Class-A Duelist d'Artagnan?!" 
    
    y "I wanted her so much, but my draws were all unlucky." 
    
    mt "I got lucky and won a secret code drawing that gave me that Champion." 
    
    show Makoto Bashful with dissolve
    
    show Haru Annoyed with dissolve
    
    mt "I don't think I've seen Haru so upset since the time he missed swim practice with a cold." 
    
    hn "..." 
    
    y "You play as well? Who's your primary Champion?"
    
    show Haru Neutral with dissolve
    
    hn "Eliminator. Class-B. Wilkes Booth." 
    
    y "I'm not sure I'm more disturbed that your main Champion is the man who killed Abe Lincoln..." 
    
    y "Or that it totally fits your personality." 
    
    hn "..." 
    
    show Makoto Sad with dissolve
    
    mt "Look, I hope you don't find this too pushy, but maybe I can send you an ally request." 
    
    show Makoto Neutral with dissolve 
    
    mt "BackMakoto is my user ID. And WaterboyHaru is Haru's." 
    
    d "After a few quick flicks and some typing, I've sent the requests." 
    
    y "You should have my requests. My user ID is Silent Gone." 
    
    y "I have a Class-A Sorcerer as my main Champion. Morgan le Fay." 
    
    y "Hey, don't you guys find it odd that a Japanese product uses so many figures from European history in it?"
    
    show Makoto Sad with dissolve
    
    mt "Only a little. But I think they'd run out of epic characters if they stuck to only Japan." 
    
    y "I supposed you're right..." 
    
    show Makoto Neutral with dissolve
    
    mt "Are you into any other video games?"
    
    y "Sure, I left my Station-Xcite console at home, but I had some games I enjoyed." 
    
    mt "Want to join the gang over at Haru's place this Saturday?" 
    
    show Makoto Bashful with dissolve
    
    mt " I just picked up 'Strut, Slide and Slam Master 3'. We were all going to try it out." 
    
    mt "You're part of the team now, so maybe you'd like to hang out. Get to know us, have some fun. Show off your dance moves." 
    
    y "You know what-, you're on!" 
    
    y "I may not be up to speed at swimming with you guys yet, but I'm sure I can be master of the mosh pit." 
    
    hn "Unlikely." 
    
    show Makoto Worried with dissolve
    
    mt "Haru currently owns that title among us. I was so close to beating him last time..." 
    
    mt "But he got just a little extra oomph into his last slam on me and won." 
    
    show Makoto Neutral with dissolve
    
    hn "..." 
    scene bg M Residence 3 with dissolve 
    
    d "We chat a little bit longer as we approach the house I'm staying at." 
    
    d "Once we get there, Makoto looks at me and smiles." 
    
    show Makoto Bashful at center with dissolve 
    
    mt "Hey, is it cool to get your phone number?"
    
    mt "This way, I can text you the plans for this Saturday." 
    
    y "Sure, that makes sense." 
    
    d "He holds up his phone, and I match mine to it." 
    
    d "A few seconds later, our contacts are swapped. Then looking to the other side, I see Haru. He's holding up his phone." 
    
    y "You want my number?"
    show Haru Neutral at left with dissolve
    show Makoto Neutral at right with moveoutright
    hn "..." 
    
    hn "Yes." 
    
    y "Well, okay, just don't send me anything weird." 
    
    d "We use the beam exchange and our contacts are swapped." 
    
    show Makoto Sad with dissolve
    
    mt "Well, we have to get going so we can work on our homework as well." 
    
    mt "Catch you at school tomorrow!" 
    
    hide Makoto with dissolve
    
    hide Haru with dissolve
    
    d "They both wave as they leave me on the doorstep of Gou's house." 
    
    d "Maybe this won't be so bad after all." 
    
    d "I feel a little better about this crazy day as I head through the front door." 
    
    scene bg MC Bedroom 2 with dissolve
    
    d "I decided to practice my Japanese writing for the past couple of hours." 
    
    d "My wrist is paying the price for that." 
    
    d "What's worse is my Japanese still doesn't look any different from doodling stick figures." 
    
    d "Maybe I should ask Makoto for help. Or Gou." 
    
    d "The siren's call of my empty stomach is loud and clear." 
    
    d "However, I'm not sure if there's anything made in the house." 
    
    d "As I head downstairs to look, I hear the front door open." 
    
    scene bg Living Room 2 with dissolve
    
    gm "%(povLastName)s-san, I'm back!" 
    
    scene bg Hallway Entrance 2 with dissolve
    
    d "I quickly go to greet her at the door." 
    
    show Gou Neutral at center with dissolve
    show Sosuke Neutral 1 at right with dissolve
    show Rin Neutral at left with dissolve
    
    d "When I get there, she's not alone." 
    
    d "Flanking her are two young men." 
    
    d "Actually, two rather handsome young men." 
    
    d "It's odd that in the states I barely noticed any guys around me." 
    
    d "I get to Japan and on the first day of school I've run into nothing but dudes who should start a boy band together." 
    
    gm "Let me introduce you to the guys here." 
    
    show Rin Annoyed 2 with dissolve 
    
    unknown "No need, sis, I can introduce myself." 
    
    d "The guy with hair and eyes similar in color to Gou's steps up to greet me." 
    
    show Rin Smile with dissolve
    
    unknown "Matsuoka Rin. I'm Gou's older brother. A pleasure to meet you." 
    
    rm "This is my best friend, Yamazaki Sousuke. We both go to Samezuka Academy." 
    
    show Sosuke Smile with dissolve
    
    sy "Nice to meet you. %(povFirstName)s, was it?" 
    
    y "Yes, nice to meet both of you..." 
    
    d "I think I mumbled that line." 
    
    d "I'm such a dork." 
    
    show Sosuke Neutral 1 with dissolve
    
    show Rin Reassuring with dissolve
    
    rm "Hey, no need to be shy around us." 
    
    rm "After all, since you're living here, I should at least treat you like a sister." 
    
    show Rin Smile with dissolve
    
    rm "Maybe you can be the sister I wanted but never got because I ended up with Gou instead!" 
    
    show Gou Mad with dissolve
    
    gm "Hey! That's totally mean." 
    
    show Rin Reassuring with dissolve
    
    rm "Relax Gou, I was only trying to make %(povFirstName)s feel at ease." 
    
    show Sosuke Smile with dissolve
    
    sy "Don't worry, Gou. You can be my sister instead." 
    
    show Gou Neutral with dissolve
    
    gm "Like I'm not already?"
    
    d "I can't help but laugh. Their familiarity is setting me at ease." 
    
    y "Rin-san, your English is impeccable." 
    
    show Rin Smile with dissolve
    
    rm "Thanks! I actually spent a good bit of time training in Australia." 
    
    rm "I figured it would be a good idea to learn the language so I wouldn't need an interpreter." 
    
    gm "Oh, %(povLastName)s-san, Makoto sent me a text a bit ago." 
    
    show Gou Determined with dissolve
    
    gm "I didn't know you played 'Destiny's Ultimate Challenge' too." 
    
    gm "We all play. Even Rin and Sousuke."
    
    gm "Let's exchange contact info. and user ID's so we can all play and chat together." 
    
    y "Sure, sounds like a plan!" 
    
    d "We all pull out our Smart Phones and exchange contact info and send ally requests." 
    
    d "I'm starting to feel more at home." 
    
    d "Even more so when Rin asks..." 
    
    rm "I'm starving, Sis. Where's mom?"
    
    show Gou Neutral with dissolve
    
    gm "She's working late tonight." 
    
    show Gou Worried 2 with dissolve
    
    gm "And dinner hasn't even been started yet." 
    
    gm "I don't know if we even have any instant ramen left." 
    
    show Gou Worried 1 with dissolve
    
    gm "So, our current dinner options are moan and starve or keep quiet and starve." 
    
    show Rin Neutral with dissolve
    show Sosuke Neutral 1 with dissolve
    
    rm "This sucks. I left my money back at the academy." 
    
    y "Hey Gou, you mentioned not having any easy instant stuff." 
    
    y "But do you think there's ingredients to do normal cooking with?"
    
    gm "Probably, but I bombed Home Economics." 
    
    gm "And don't expect either of those two to know how to cook." 
    
    show Gou Neutral with dissolve
    
    gm "Rin's lucky if he doesn't burn his ramen in the microwave." 
    
    show Rin Annoyed 2 with dissolve
    
    rm "That was only one time three years ago." 
    
    gm "And it's still a hilarious memory three years later." 
    
    show Rin Neutral with dissolve
    
    y "Let me go root around the kitchen." 
    
    gm "You can cook? Really?" 
    
    y "I wouldn't put myself up against Masaharu Morimoto or anything, but I can make some dishes that taste pretty decent." 
    
    scene bg Kitchen with dissolve
    
    d "I check the pantry for dry goods and canned foods first." 
    
    d "I spot several cans of Adzuki beans and grab those." 
    
    d "Looking in the fridge there's a package of lean ground beef." 
    
    d "There's also some onions and peppers." 
    
    d "Gou walks over to see what I'm doing." 
    
    show Gou Neutral at center with dissolve
    
    gm "Looks like you have something in mind." 
    
    y "Point me towards the spice rack and pull me a big pot out." 
    
    y "I'm going to make a pot of Chili Con Carne for everyone!" 
    
    show Gou Worried 1 with dissolve
    
    gm "Seriously? Wow!" 
    
    y "It's not that amazing." 
    
    y "When your parents are prone to working late, you can either learn to cook..." 
    
    y "Or learn not to get tired of instant food." 
    
    d "Gou gets me the pot while I get out the spices." 
    
    show Gou Neutral with dissolve
    
    gm "Come to think of it, I bet one of the guys would get a kick out of this dish." 
    
    gm "Want me to call one of them over for you?" 
    
    y "Hmmmmmm..." 
    
    menu:
        "Haru":
            jump Haru_Romance_Route
           

        "Makoto":
            
           jump Makoto_Romance_Route
            
        "Nagisa":
            
            return
            
        "Rei":
            
            return
            
        "Rin":
            
            jump Rin_Romance_Route
            
        "Sousuke":
            
            return
        
######HARU'S ROUTE

##Chapter 1
label Haru_Romance_Route: 
    
    d "I'm not sure which guy I'd want her to call over for dinner." 
    
    d "The two I know best are Makoto and Haru." 
    
    d "I supposed one of them would be okay." 
    
    d "Maybe Makoto?"
    
    d "Just as I'm about to speak, Gou speaks again..." 
    
    gm "You know, I'll bet Haru is just eating the same fish meal again." 
    
    gm "He could probably use something different for a change." 
    
    y "Haru? Well, I suppose that would be okay." 
    
    y "He's kind of weird though." 
    
    show Gou Worried 1 with dissolve 
    
    gm "Oh, that's just Haru being Haru." 
    
    gm "You'll get used to it though." 
    
    show Gou Neutral with dissolve
    
    gm "He's actually a pretty sweet guy once you get to know him." 
    
    gm "Just don't expect much in the way of chit-chat with him." 
    
    y "Well, okay. But maybe it would be best if you called him over." 
    
    gm "Okay, let me grab my phone." 
    
    hide Gou with dissolve
    
    d "Haru, huh? Maybe I overreacted to him earlier." 
    
    d "Of course, the first time I met him he decided to strip down and dive to his death." 
    
    d "And it is his fault I'm now even on the swim team." 
    
    d "His taunting and my big mouth, that is." 
    
    d "Did Gou say he eats the same fish meal all the time?" 
    
    show Gou Neutral at center with dissolve
    
    gm "Hey Nanase-kun, get your scrawny butt over here." 
    
    gm "The new girl made some chili and wants you to try it out." 
    
    y "Wait a minute! That's not what I said!" 
    
    gm "Of course she does. After all, she figures she's a better cook than you." 
    
    gm "I won't tell her you concede that point readily." 
    
    show Gou Determined with dissolve 
    
    y "Okay, really, I never said anything like that." 
    
    show Gou Worried 1 with dissolve
    
    gm "Fine, I guess you can bring Makoto as well." 
    
    gm "See you in a bit." 
    
    show Gou Neutral with dissolve
    
    y "Why in the world did you phrase it like THAT?" 
    
    gm "Like what?"
    
    y "You made it sound like I was asking him on a date!" 
    
    show Gou Worried 1 with dissolve
    
    gm "I did? Well, don't worry, Haru's kind of thickheaded." 
    
    gm "He probably just heard the word food and figured walking was easier than cooking." 
    
    show Gou Neutral with dissolve
    
    gm "Makoto's coming too." 
    
    y "Well, okay then. Do we have some sort of bread around here?"
    
    y "I can toast that up and add some butter with garlic salt to make as a side." 
    
    gm "Yeah, let me get that for you." 
    
    hide Gou with dissolve 
    
    d "I spend the next 15 minutes or so stirring the chili and making garlic bread." 
    
    d "Gou is talking with Rin and Sousuke, also checking with me every so often." 
    
    show Rin Smile at center with dissolve 
    
    rm "Wow, that smells really good. My mouth's watering." 
    
    hide Rin with dissolve
    
    y "Almost finished. A couple more minutes of stirring and we'll be good." 
    
    y "What are we drinking with this anyway?" 
    
    show Gou Neutral at center with dissolve
    
    gm "There's some juice boxes in the fridge." 
    
    gm "And I guess there's always water." 
    
    gm "We don't keep much in the way of soda, and mom keeps the sake locked down." 
    
    y "That makes sense. I'll set up the table." 
    
    hide Gou with dissolve
    
    d "This is actually kind of fun for me." 
    
    d "I haven't really eaten with a group of friends in a long time." 
    
    d "Just as I'm done setting up the table, there's a knock at the door." 
    
    rm "Well well, Haru. Nice to see you finally showed up." 
    
    rm "A little slow as usual, eh?" 
    
    mt "Aha, It's my fault we're a tad late." 
    
    rm "Is that so, Haru?"
    
    hn "..." 
    
    gm "Now, now, boys, this is supposed to be a friendly dinner." 
    
    gm "You can go about your pathetic display of manhood later."
    
    gm "I was talking to Rin and Haru, mostly." 
    
    d "Now might be a good time to get everyone to the table." 
    
    d "Before Rin and Haru decide to run to the local pool to compare times." 
    
    y "Hey guys, dinner is on the table." 
    
    y "Let me go clean up real quick and I'll meet you there." 
    
    mt "Sounds good, %(povLastName)s-chan!" 
    
    mt "Let's get to the grub, guys!" 
    
    scene bg Bathroom with dissolve
    
    d "I hear them all getting to the table as I'm scrubbing up in the bathroom." 
    
    gm "Haru, could you wait just another minute so %(povLastName)s can get back?"
    
    gm "I mean, sheesh manners much?"
    
    mt "Yeah, Haru. We should wait for her." 
    
    mt "After all, she did cook the meal, it's only polite." 
    
    hn "So... Hungry." 
    
    gm "Deal with it. She won't be long." 
    
    d "Guess I'd best get out there." 
    
    d "Hanging back up the hand towel, I walk back into the kitchen." 
    
    scene bg Dining Table 2 with dissolve
    
    d "The only open chair is by Haru." 
    
    d "Call me suspicious, but I think this was done on purpose." 
    
    d "Well, nothing to be done about it." 
    
    d "I go and take my seat." 
    
    show Gou Neutral at center with dissolve
    
    gm "Hey, thanks for cooking dinner for us!" 
    
    y "Don't mention it. It's the least I can do." 
    
    show Gou Worried 1 with dissolve
    
    gm "No, seriously, I was getting sick of Arkansas Fried Chicken every night." 
    
    d "She glares at Makoto as she says this." 
    
    show Makoto Worried at right with dissolve
    
    mt "What?! I like AFC. It's delicious and affordable." 
    
    show Makoto Neutral with dissolve
    
    mt "God bless Americans for bringing it to Japan!" 
    
    y "Why are you saluting me as you say that?" 
    
    y "I had nothing to do with AFC's international proliferation." 
    
    hide Gou with dissolve
    
    hide Makoto with dissolve
    
    d "I think I heard Haru snort a little after I said that." 
    
    d "We set about to eating dinner." 
    
    d "It turned out better than I had hoped for." 
    
    d "I really got the spices right for that pot, and everyone seems to be enjoying it." 
    
    d "Soon everyone is done, with Rin volunteering to clear up the table." 
    
    d "Gou flops down on the couch moaning." 
    
    show Gou Neutral at center with dissolve
    
    gm "Oooh, that was so good, %(povFirstName)s-chan." 
    
    gm "I could eat that every day." 
    
    d "If my studies have taught me anything, a \"won't you get fat\" comment is coming."
    
    show Makoto Neutral at right with dissolve
    
    mt "Better not follow that idea, Gou, you'd totally get fat." 
    
    d "Predictable." 
    
    show Gou Mad with dissolve
    
    gm "Stop that, Makoto, you idiot! I work out so I'd be fine." 
    
    show Rin Smile at left with dissolve 
    
    rm "Hey sis, I started the dishwasher. Sousuke and I need to get back to campus." 
    
    show Gou Neutral with dissolve
    
    gm "Okay. Be safe going back." 
    
    hide Rin with dissolve
    d "They wave as they head out the front door." 
    
    show Makoto Neutral with dissolve
    
    mt "Yeah, Haru and I better get going, too." 
    
    show Makoto Sad with dissolve
    
    mt "Speaking of which, where did he go?" 
    
    d "Haru seems to be missing in action for the moment." 
    
    show Gou Worried 1 with dissolve
    
    gm "Don't know. Maybe he went home already? It wouldn't be the first time he left without saying anything." 
    
    show Makoto Neutral with dissolve 
    
    mt "True, well then I guess I'll head out. See you both at school." 
    
    hide Makoto
    
    d "Gou turns to me as Makoto heads out." 
    
    show Gou Neutral with dissolve
    
    gm "I prefer to clean up in the morning, so if you want to get a bath or shower, it's all yours." 
    
    y "Thanks! I could really use a bath. Your mom left towels in my room, so I'm gonna clean up." 
    
    scene bg MC Bedroom 2 with dissolve
    
    d "We head back to our bedrooms."
    
    d "Once inside, I grab some fresh pajamas, strip down, then wrap a towel around myself."
    
    d "I'm beat, and a nice long soak sounds good about now." 
    
    scene bg Bathroom with dissolve
    
    d "With a big yawn I open the bathroom door..." 
    
    y "WHAT ARE YOU DOING IN HERE?" 
    
    d "...And I'm greeted to the sight of Haru soaking in the bathtub." 
    
    show Haru Neutral at center with dissolve 
    
    hn "Water. Feels good." 
    
    y "That's besides the point, why are you soaking in another family's bathtub?" 
    
    y "Get out already. Not only is it rude, but I need a bath." 
    
    d "He goes to stand up and I quickly remember I need to turn away." 
    
    hn "Why are you blushing?" 
    
    y "Because I'm standing here naked in the bathroom with a naked guy getting out of the bathtub!" 
    
    hn "I'm not naked." 
    
    d "I turn and look." 
    
    hn "Swim trunks." 
    
    y "Okay, so you're only half naked. Whatever, get out already!" 
    
    hn "Nice towel. See you tomorrow." 
    
    hide Haru Neutral at center with dissolve 
    
    y "Why would you say something like that?" 
    
    d "Oh, he's already gone. What a weirdo." 
    
    d "Well, time to draw a fresh bath." 
    
    d "Once the tub is full, I get in and have a nice relaxing soak." 
    
    d "And yet, I can't get Haru out of my head." 
    
    d "Weird as he is, he's completely gorgeous." 
    
    scene bg MC Bedroom 2 with dissolve
    
    d "I can't stop thinking about that fact as I finish up and lay down to sleep." 
    
    d "..." 
    
    scene bg white with dissolve 
    
    stop music
    
    unknown "Oh look at you, still putting on airs even now, huh?" 
    
    d "Wait a second, this can't be right. This voice shouldn't be here." 
    
    d "I left you behind..." 
    
    unknown "You can't escape from me, you uptight bitch." 
    
    unknown "I'm sick of you always acting like you're so much better than everyone." 
    
    d "Turning around, I see three familiar faces that I would rather never see again." 
    
    d "Two taller girls flanking a shorter, blonde-haired girl, and it's the blonde addressing me." 
    
    y "Summi?" 
    
    sm "So you do remember how to talk. How wonderful." 
    
    sm "I was afraid your uptight way of never speaking to anyone made you forget how." 
    
    unknown "Ha, you tell that bitch, Summi." 
    
    d "The girl on the left pipes in like the butt-kissing lackey she is." 
    
    d "Jeseri always was just a follower." 
    
    js "Look at the stupid look on her face, Summi." 
    
    js "Like she thought she could avoid us forever." 
    
    sm "She always underestimates everyone, but that's normal for her." 
    
    unknown "Come on guys, we'll be late." 
    
    d "The third voice finally speaks, but it's always the same." 
    
    d "Leya was once my best friend, so she won't treat me like the other two." 
    
    d "But she never stands up for me directly." 
    
    d "It hurts worst of all. My former best friend won't even help me." 
    
    d "Even though she knows everything that happened to me before..." 
    
    d "And sees what's happening now." 
    
    ly "You know Coach Welsh makes us run extra laps for every minute we're late." 
    
    sm "Cool it Leya. We'll be on time." 
    
    sm "We just have to make sure we remind this bitch who her betters are." 
    
    sm "So she knows where her real place is." 
    
    d "It goes on like this every day." 
    
    d "I just want to get home as quickly as possible." 
    
    d "I duck out early. I change routes. I scout and hide. Nothing works." 
    
    d "Summi is always there, waiting for me." 
    
    js "Come on Leya, doesn't it make you so angry?" 
    
    js "%(povFirstName)s used to be our good friend, but this year she decided she was so much better than us." 
    
    js "Won't hang out with us. Doesn't talk to us. She even changed her cell number and didn't tell us." 
    
    js "She won't even talk to defend herself, she's so stuck up. Look at her!" 
    
    ly "She looks more like she wants to cry." 
    
    ly "I'm going to practice now. Don't blame me if you two end up running extra laps." 
    
    d "The only one who won't directly hurt me leaves, and it's the worst feeling ever." 
    
    d "Worse than the insults. And worse than..." 
    
    d "SLAP!" 
    
    sm "Show me some tears and I'll stop. Or just keep being arrogant and I'll continue." 
    
    d "SLAP!" 
    
    js "Hey, we've got teachers coming soon. We'd better beat it." 
    
    sm "Well then, better leave my calling card and go." 
    
    d "She balls her fingers into a fist, and draws back for the haymaker." 
    
    d "I don't even say anything as her fist comes flying at my face and just as it's about to strike..." 
    
    y "Aaahhh!"
    
    play music "Natsu No Owari.mp3"
    
    d "...I wake up." 
    
    scene bg MC Bedroom 1 with flash
    
    y "Not again. Why this dream and why now?" 
    
    d "It's morning, and I've woken up just before my alarm." 
    
    d "I'm also in a cold sweat after that nightmare." 
    
    d "Maybe Gou won't notice if I take a quick shower, even though I bathed last night." 
    
    d "I check to see if she's in the bathroom, but she's actually nowhere to be found." 
    
    d "She probably had club business to attend to and left early." 
    
    d "I quickly shower and change into my school uniform." 
    
    scene bg Kitchen with dissolve 
    
    d "In the kitchen I put together a lunch box as I heat up some food." 
    
    scene bg Hallway Entrance 1 with dissolve 
    
    d "I'm tempted to run out the door with a piece of toast in my mouth, just for fun." 
    
    d "Maybe some other time." 
    
    d "I gather up everything I need and step out the front door." 
    
    scene bg M Residence 1 with dissolve 
    
    mt "Good morning!" 
    
    d "I should have known that those two would be there." 
    
    show Makoto Neutral at right with dissolve
    
    show Haru Neutral at left with dissolve
    
    d "Makoto is bright-eyed and bushy-tailed like a scared squirrel." 
    
    d "Haru, on the other hand, looks like he's about to fall asleep on his feet." 
    
    y "Makoto, uhm, hi. What are you and Haru doing here?" 
    
    mt "Gou asked us to accompany you to the bus, so that your experience here would be better." 
    
    d "If my mind were a meme, it would involve Picard around now." 
    
    y "I give up. Let's get going." 
    
    scene bg Neighborhood A_1 with dissolve 
    
    d "The three of us start walking to the station, chatting about the upcoming Destiny's Ultimate Challenge special event." 
    
    d "Actually, Makoto and I talk while Haru grunts every so often." 
    
    d "It isn't long before we run into Rei and Nagisa." 
    
    show Rei Neutral at right with dissolve
    
    show Nagisa Determined 1 at left with dissolve
    
    rr "Good morning everyone!" 
    
    nh "Hey guys. What's new?" 
    
    nh "I see Gou has you guys walking %(povFirstName)s-chan to school today." 
    
    show Makoto Neutral at center with dissolve 
    
    mt "Well, it wasn't just because she asked us to." 
    
    mt "It's good to hang out with our new friend." 
    
    show Nagisa Sarcastic with dissolve
    
    nh "Sure, sure sure. We totally believe that Makoto." 
    
    nh "Like the real reason isn't obvious to anyone looking." 
    
    show Makoto Sad with dissolve
    
    mt "I'm not sure what you're driving at..." 
    
    show Rei Reassuring with dissolve
    
    rr "My dear Makoto, you couldn't be easier to read if you had a huge neon sign over your head." 
    
    show Nagisa Determined 2 with dissolve
    
    nh "Can't you just admit that you dig the new girl and want to be around her?" 
    
    nh "I mean, it was so obvious yesterday." 
    
    nh "You kept looking over at her during class, and trying to study with her." 
    
    nh "You are so crushing on her, man." 
    
    d "I'm pretty sure I'm blushing hard now." 
    
    d "And I'm not even the one getting roasted by the guys here." 
    
    d "Makoto looks kind of flustered. It's cute, actually." 
    
    show Makoto Mad with dissolve
    
    mt "Hey now... I was just trying to welcome %(povLastName)s to Japan." 
    
    mt "I mean, she doesn't have anyone here and her host sister couldn't help her on her first day of school." 
    
    mt "I was just trying to be a good friend is all." 
    
    show Makoto Sad with dissolve
    
    mt "It has nothing to do with her being cute." 
    
    y "Oh, so you admit you think I'm cute." 
    
    show Makoto Worried with dissolve
    
    mt "Wait, what, no. I mean, yes, but no. Uhm..." 
    
    mt "This is not going as well as I'd like." 
    
    show Makoto Sad with dissolve
    
    mt "But y-yeah, of course you're cute. Ask any of the guys here and they'd say the same." 
    
    mt "So it's no indication of any romantic interest that I think you're cute." 
    
    nh "So busted. Much denial." 
    
    rr "Methinks the gentleman doth protest too much." 
    
    mt "It's completely not what you think it is at all." 
    
    d "Makoto is getting a full-on assault from the guys on this." 
    
    d "Lost in the conversation is the ever-silent partner Haru." 
    
    d "I figured he'd sit this one out as it had nothing to do with water, swimming or swimming in water." 
    
    d "Surprisingly, he steps in the middle of the guys." 
    
    hide Rei with dissolve 
    
    show Haru Neutral at right with dissolve 
    
    hn "..." 
    
    nh "Look Makoto, even Haru is coming in here to bust on you." 
    
    show Makoto Worried with dissolve
    
    mt "No way. Haru's not like that. And he knows better." 
    
    hn "I'm not sure why you think Makoto is infatuated with %(povFirstName)s." 
    
    hn "But we already know he can't get a girlfriend." 
    
    hn "He's already got me." 
    
    show Nagisa Upset 2 with dissolve 
    
    d "......" 
    
    d "Well that's an odd statement coming from Haru." 
    
    d "The guys are all just staring at him, trying to comprehend what exactly he just said." 
    
    d "Awkward." 
    
    d "I'd better say something." 
    
    y "Haru, are you saying you and Makoto are gay?" 
    
    y "Not that there's anything wrong with it." 
    
    show Makoto Mad with dissolve
    
    mt "W-what? I'm not gay!" 
    
    y "Okay, then what did you mean, Haru?" 
    
    hn "Isn't it obvious? I'm hydrosexual. It's all about water." 
    
    d "The guys are all laughing at this completely absurd statement." 
    
    show Makoto Neutral with dissolve
    
    show Nagisa Sarcastic with dissolve 
    
    y "That... Doesn't make any sense whatsoever." 
    
    y "Wait, I take that back... Nevermind, no I don't. There is absolutely no cohesion in what you're saying." 
    
    hn "Bus." 
    
    y "Are you going to quip that you're autosexual now?" 
    
    hn "No, the bus is here. We should get on." 
    
    y "Why are we taking the bus today anyway?" 
    
    hide Nagisa with dissolve
    
    hide Makoto with dissolve 
    
    hide Haru with dissolve
    
    show Rei Neutral at center with dissolve
    
    rr "Gou texted us and said that the planned practice today is gonna be brutal." 
    
    rr "So we need to conserve our bodies for later." 
    
    y "Gotcha. Makes sense." 
    
    d "We all settle into our seats and it's mostly quiet, as everyone has logged into DUC." 
    
    d "Looks like I got a couple of backup requests." 
    
    d "I help Nagisa and Rin finish off a couple of quest bosses and level up my champion." 
    
    d "Maybe today will be a good day after all." 
    
    scene bg School Gates_Morning with dissolve
    
    scene bg School Lockers_01 with dissolve 
    
    d "It doesn't take too long for us to get to school." 
    
    d "As we pile off the bus we start heading over towards the lockers." 
    
    d "Most everyone has some sort of decoration on the inside of their lockers." 
    
    d "I recall Gou having photos of the latest American Studio Star in there." 
    
    d "I haven't decided if I'm going to bother decorating mine or not." 
    
    d "It's not long before I hear the locker next to mine being opened." 
    
    d "Turning around I see a familiar face." 
    
    y "Oh, hi Haru. I... Didn't realize your locker was next to mine." 
    
    show Haru Neutral at center with dissolve
    
    hn "It appears that's just so." 
    
    y "Well that's good, I think." 
    
    hn "Are you okay?"
    
    y "I think so. Why do you ask?" 
    
    hn "Your face is kind of red. Are you getting a fever?" 
    
    d "I'm not sure what to tell him, but I know it's not a fever." 
    
    d "Before I can even stammer out something, he's put his hand to my forehead." 
    
    d "He has a gentle touch, and his hand is cool." 
    
    d "Crap, What the hell am I thinking?" 
    
    d "I mean, so what if he has a lean, muscular body, watery blue eyes and has a gentle touch?" 
    
    d "He's weird, right? I mean he strips in public!" 
    
    d "Strips to his rather... Nice... STOP IT ALREADY!" 
    
    hn "You don't seem to have a fever. Maybe dehydration?"
    
    hn "Make sure to drink plenty of water." 
    
    y "Uhm, yeah, great idea! And if I can't find any, I'll follow you to it." 
    
    d "Welcome to Lamesburg. Population: Me." 
    
    d "And yet he smiled a little at that. I think." 
    
    hn "Let's go to class." 
    
    y "Yeah, I should probably wait until next week to start being late to Ama-chan's homeroom." 
    
    d "He chuckles a little as we gather our things to head off to class."
    
    scene bg Classroom A_01 with dissolve
    
    show Miho Neutral at center with dissolve
    
    ma "Good morning %(povFirstName)s and Haru. Wow, this may be a first." 
    
    y "What do you mean, Sensei?" 
    
    show Miho Reassuring with dissolve
    
    ma "Usually Haru either walks in dripping wet..." 
    
    ma "Or Makoto is dragging him in before the truant bell rings." 
    
    ma "And you've brought him here dry and on time."
    
    show Miho Neutral with dissolve
    
    ma "Makoto may want in on your secret to that." 
    
    hn "..." 
    
    y "I don't think I did anything special. His locker is next to mine." 
    
    y "So we just ended up walking here." 
    
    ma "Hmmm, interesting." 
    
    ma "Anyway, go ahead and take your seat, we'll be starting shortly." 
    
    hide Miho with dissolve
    
    d "Not too long after, Makoto arrives, and minutes later class begins." 
    
    d "Just like yesterday, the first two classes go by smoothly." 
    
    d "Then comes the dreaded Japanese class." 
    
    d "I'd say that my handwriting has improved since yesterday." 
    
    d "Instead of looking like bare stick figures, my marks now look like stick figures with clothing." 
    
    d "That's improvement, right?" 
    
    d "At least there wasn't a pop quiz today." 
    
    d "Before I know it, the lunch bell is sounding." 
    
    show Makoto Neutral at center with dissolve
    
    mt "Hey, don't forget, Gou wanted all of us to meet on the roof for lunch today." 
    
    mt "I've got to get mine from the cafeteria. Did you need anything, %(povFirstName)s?" 
    
    y "Thanks Makoto, but I actually packed my lunch today." 
    
    d "I proudly show off my bento box like a kid presenting her latest artwork to a parent." 
    
    show Haru Neutral at left with dissolve
    show Makoto at right with moveoutright
    
    hn "Could you get me something, Makoto?" 
    
    hn "I forgot my wallet. I'll pay you back tonight at home." 
    
    mt "I'll see what I can scrouge up. I didn't bring a lot of money with me." 
    
    show Miho Neutral at center with dissolve
    
    ma "Haru, before you head to lunch I need to check with you on something." 
    
    mt "I'll go to the cafeteria. You head to the roof, %(povLastName)s." 
    
    y "Sounds like a plan." 
    
    scene bg Hallway A_01 with dissolve
    
    d "We head off in opposite directions, with me heading for the stairs." 
    
    d "The ladies room is on the way, so I figure I'll freshen up really quick." 
    
    d "The line's a bit long, though, and I feel like I'm late now." 
    
    scene bg Stair Well B_01 with dissolve
    
    d "Sprinting out I head for the stairs, and once there I see Makoto ahead of me." 
    
    y "Hey Makoto, wait up... Aaahhh!" 
    
    scene bg Stair Well B_01 with vpunch
    
    d "In my haste, I didn't notice someone had left a crumpled water bottle on the steps." 
    
    d "My foot found it and I slip, about to get a special trip to the nurse's office." 
    
    d "Because I'm falling backwards and my head is going to hit something hard." 
    
    d "Wait... This isn't hard at all." 
    
    d "I've been grabbed by a pair of soft hands and strong arms." 
    
    d "My journey to the nurse's office has been postponed!" 
    
    show Haru Neutral at center 
    
    hn "Hey, are you okay?" 
    
    y "Haru!" 
    
    d "It appears Haru has caught me before I added concussion to my list of problems." 
    
    d "He's surprisingly warm." 
    
    
    menu: 
        "Pull back and thank Haru": 
            d "Loathe as I am to remove myself so quickly from what's kept me from a set of head stitches, I slowly get from Haru's grip." 
            
            y "Thank you Haru, I'm so glad you were behind me." 
            
            y "I was running behind and I didn't notice anything on the stairs and I slipped." 
            
            y "If you hadn't been there, I would have cracked my head open." 
            
            hn "You don't have to thank me." 
            
            show Haru Bashful with dissolve
            
            hn "I'm...just glad you're okay." 
            
            y "Yeah, I'm okay now, thanks to you." 
            
            y "Hey let's go eat lunch." 
            
            hn "Good idea. I'm pretty hungry." 
            
            
        "Hug Haru and thank him.": 
            
            d "Maybe it's because of the shock of almost falling down the stairs." 
            
            d "But I'm feeling really insecure, and before I know it, I'm wrapping my arms around Haru." 
            
            d "I'm holding on to him like I'm about to fall off the face of the earth." 
            
            hn "Hey, you're okay. I've got you." 
            
            y "I know, I know. It's just...I'm not normally so careless." 
            
            y "If you hadn't been behind me, things could have gotten really bad." 
            
            y "Thanks for catching me." 
            
            show Haru Bashful with dissolve
            
            hn "Sure thing." 
            
            d "Who keeps leaving these random water bottles around for me to step on, anyway?"
            
            d "That's the second one in as many days." 
            
            hn "Uhm..." 
            
            d "I mean, first there was one on the roof yesterday." 
            
            d "I just assumed it was Haru's because he was the only one there." 
            
            show Haru Neutral with dissolve
            
            hn "Hey.." 
            
            d "Maybe I owe him an apology." 
            
            d "I mean, it could have been left there by someone else." 
            
            show Haru Annoyed with dissolve
            
            hn "Hello..." 
            
            d "Now there's one on the steps heading to the roof." 
            
            d "Though I guess it could be two different people tossing their empties around." 
            
            hn "%(povLastName)s-CHAN!" 
            
            y "Hey, you don't have to yell, Haru." 
            
            show Haru Neutral with dissolve
            
            hn "You don't weigh much, but I can still only hold something for so long." 
            
            hn "Can we go eat lunch?"
            
            y "Ooops. Sorry, Haru." 
            
            d "I let go and we both head up the stairs to the roof." 
    
    scene bg School Rooftop Entrance with dissolve
    
    scene bg School Rooftop with dissolve
    
    d "Everyone else is already at the desginated lunch spot when Haru and I arrive." 
    
    d "There aren't any benches to sit on, so everyone is on the ground." 
    
    d "Gou had warned me about that. The school removed the benches before this year." 
    
    d "Something about a kid with heart problems falling off the roof and getting hurt badly." 
    
    d "Though some say he might have been pushed." 
    
    d "You'd think the school would just close off the roof, but it seems they feel that's a losing battle." 
    
    d "So the hope was with nowhere to sit, the kids would stop going." 
    
    d "Clearly our prescence here today shows the fruits of that policy are also futile." 
    
    show Nagisa Determined 1 at right with dissolve
    
    nh "Took you guys long enough." 
    
    show Rei Neutral at left with dissolve
    
    rr "No need to be rude, Nagisa. Have a seat guys." 
    
    show Gou Worried 1 at center with dissolve
    
    gm "Hey, %(povFirstName)s-chan, your face looks flushed. Are you okay?" 
    
    d "I guess in the excitement of the stairwell accident I turned a tad red again." 
    
    hide Rei with dissolve
    
    show Makoto Neutral at left with dissolve
    
    mt "Yeah, Gou's right. You look a bit red." 
    
    mt "You aren't coming down with a fever are you?" 
    
    d "Makoto stands and reaches for my forehead in a strange case of very recent déjà vu for me." 
    
    d "Didn't I just go through this with Haru this morning?" 
    
    y "No, I'm just feeling a tad ill from the height of the building." 
    
    y "And possibly just a tad hungry, so let's eat, eh?" 
    
    show Nagisa Pouty with dissolve
    
    nh "Eh? I thought you were from Oregon, not Saskatchewan." 
    
    y "Watch it, bub." 
    
    show Nagisa Determined 1 with dissolve
    
    nh "Nagisa gives a chuckle at my well-placed American pop culture reference." 
    
    hide Gou with dissolve
    
    hide Makoto with dissolve
    
    hide Nagisa with dissolve
    
    d "Then we all settle in and start on our lunches." 
    
    d "Opening my bento up the smell of pan-fried mackerel immediately wafts into the air." 
    
    d "I steamed some vegetables and rice to go with it." 
    
    d "Just as I'm about to satiate my stomach's wild call for sustenance, a familiar voice addresses me." 
    
    show Makoto Neutral at center with dissolve
    
    mt "Just when I thought you couldn't top your chili from last night." 
    
    mt "You go and bring something that smells even more delicious." 
    
    y "I'm not that good, really." 
    
    hide Makoto with dissolve
    
    show Rei Neutral at center with dissolve
    
    rr "In all seriousness, the smell from your lunch is delightful." 
    
    show Rei Reassuring  at center with dissolve
    
    rr "Would it be possible to have a small sample, please?" 
    
    y "Well, I guess so." 
    
    d "Rei takes his fork and gets a small bit of fish and pops it in his mouth." 
    
    d "If this were an anime, his reaction would have tears streaming from his blank eyes." 
    
    show Rei Neutral with dissolve
    
    rr "This is simply scrumptious, %(povLastName)s-chan." 
    
    rr "You really need to let everyone else have a taste." 
    
    y "But I really didn't bring that much. I mean, I know how to measure when cooking." 
    
    y "I'm not going to accidentally make enough food for just myself." 
    
    hide Rei with dissolve 
    
    d "It's not use. Just looking at the shine in their eyes and I've got no choice." 
    
    y "Fine, go ahead and carefully get some." 
    
    d "Nagisa, Makoto and Gou all grab a small piece and all agree it's delicious." 
    
    d "I go back to start my lunch when I feel a last set of eyes on me." 
    
    show Haru Neutral at center with dissolve
    
    hn "Saba?"
    
    y "No, I can't summon heroic spirits." 
    
    hn "I mean, is that mackerel?" 
    
    y "Oh, well yes, it's mackerel. I pan fried it in some extra virgin olive oil mixed with a touch of salt, some garlic and bay." 
    
    d "Before I know it, Haru has dipped his fork in and has taken a small piece out." 
    
    d "He pops it in his mouth, but doesn't say anything." 
    
    show Haru Happy with dissolve
    
    d "However, his eyes widen considerably, and everyone notices." 
    
    hide Haru with dissolve
    
    show Makoto Neutral with dissolve
    
    mt "Well, it appears you've gotten the rare Haru 'Seal of Approval' on your mackerel." 
    
    mt "He loves mackerel, but rarely does he eat it if it wasn't cooked by his own hands." 
    
    mt "So you must have done really well to get him to like it." 
    
    y "Really? I don't think I did anything all that special." 
    
    d "Makoto nods and then we all start back on eating lunch." 
    
    hide Makoto with dissolve
    
    d "I'm working slowly through my veggies while Gou and the guys are chatting about DUC." 
    
    d "It appears Nagisa got a bum gacha draw again." 
    
    d "Nothing special about that, the gacha in DUC is brutal." 
    
    d "I'm just about to pull out my phone when Haru walks over." 
    
    show Haru Neutral at center with dissolve
    
    d "He plops himself down next to me and looks my way."
    
    d "He seems fixated on something." 
    
    y "You okay over there, Haru?" 
    
    y "I'd say take a picture it'll last longer, but I'm notoriously camera shy." 
    
    hn "..." 
    
    d "Wait, he's not looking at me. He's looking at my lunch." 
    
    d "The mackerel in specific." 
    
    y "Did you want some more? I'm filling up on veggies." 
    
    y "So you can have it if you want it?" 
    
    hn "Please?" 
    
    d "The way he said that was kind of endearing." 
    
    d "Not unlike some toddler saying please for some ice cream." 
    
    d "I smile and drop the mackerel into his lunch box." 
    
    d "He gives a little bow and I think I saw a tear in his eyes." 
    
    y "If you want I'd be happy to make you some the next time I make it for my lunch." 
    
    show Haru Happy with dissolve
    
    hn "I'd appreciate that, thank you." 
    
    d "Haru may not say much, but his facial expression speaks volumes." 
    
    d "I think I can read him better by watching his face, his eyes in particular." 
    
    d "Before long it's time to head back to class." 
    
    scene bg Classroom A_01 with dissolve
    
    d "The second half of class pretty much resembles yesterday's end of class." 
    
    d "Quiet. Uneventful. Relatively boring. Haru once again snoring." 
    
    d "I think I saw Makoto checking out his DUC team at one point." 
    
    d "Gou also sent me no less than 5 texts reminding me of swim practice." 
    
    d "Guess I won't be slipping out quietly." 
    
    d "The bell rings and Makoto is at my desk like he's first in line for concert tickets." 
    
    show Makoto Neutral at center with dissolve
    
    mt "Time for your first practice with the team!" 
    
    mt "This is so exciting. We're finally branching out into the opposite gender." 
    
    mt "Soon we will dominate both the boys and girls races!" 
    
    y "Funny thing, if someone were to just scan the team's list of names, They'd probably think we were an all girls' school." 
    
    show Makoto Worried with dissolve
    
    mt "You'd have to ask our parents that question." 
    
    mt "To this day I have no idea why they named us like they did." 
    
    scene bg Swimming Pool A_2 with dissolve
    
    d "I nod and follow him to the pool, where everyone is waiting." 
    
    show Gou Neutral at center with dissolve
    
    gm "Welcome to swim club. As you know, I'm the manager of the club." 
    
    gm "Makoto over there is the team captain." 
    
    gm "So basically, just listen to us and you'll be fine." 
    
    gm "Anyway, I have your suit right here." 
    
    show Gou Worried 1 with dissolve
    
    gm "I'm afraid they didn't have gray trim in your size, so I picked up white." 
    
    gm "I hope that works." 
    
    gm "The girls changing room is over that way, so go ahead and get suited up." 
    
    scene bg Changeroom with dissolve 
    
    d "I simply nod, take my swimsuit and head over to the lockers." 
    
    d "There's a few other girls getting changed for other sports inside." 
    
    d "I go to a quiet corner, strip down and start putting on my swimsuit." 
    
    d "Yeesh, I know it's been a while since I wore a swimsuit." 
    
    d "But this one feels ridiculously tight." 
    
    d "Did they get my measurements wrong or something?" 
    
    d "After finally getting into my suit I grab a towel and wrap it over my shoulders." 
    
    d "Guess I'd best head out to the pool." 
    
    scene bg Swimming Pool A_2 with dissolve
    
    show Gou Worried 1 at center with dissolve
    
    gm "%(povFirstName)s, you do realize you'll need to take off the towel to swim, right?" 
    
    y "Yeah, I know that, it's just embarrassing." 
    
    y "I'm the only girl in a swimsuit amongst a bunch of guys." 
    
    y "And did you get the wrong size or something?" 
    
    y "I know I'm not oppai but uhm, the twins are feeling really squished in here." 
    
    gm "Oh, that's because that's a competition swimsuit." 
    
    gm "It's designed to be tighter so there's less movement underneath." 
    
    show Gou Neutral with dissolve
    
    gm "And I also got you a cup size down one from your current size." 
    
    gm "Since you'll be swimming every day it's likely you'll lose some body fat..." 
    
    gm "That includes your chest." 
    
    gm "Think of it as shrinking in to fit the suit as you practice." 
    
    y "Well great. I never said I wanted to become a loli, either." 
    
    gm "Please, you'll be fine. Just drop the towel already. We've got the practice to get to." 
    
    y "Fine." 
    
    d "Naturally, as if in a manga, the guys chose the exact moment I drop my towel to walk out." 
    
    d "I feel like I'm removing the towel for them to inspect because of this." 
    
    show Gou Worried 1 with dissolve
    
    gm "What are you complaining about? You look great." 
    
    gm "The suit really brings out how sleek your legs are. They look toned." 
    
    gm "Were you doing another sport before coming over here?" 
    
    show Gou Determined with dissolve
    
    gm "And what is it American guys are fond of saying over there?" 
    
    gm "Dat ass? Right?" 
    
    y "Gou, really? Are we going to meme my body now?" 
    
    y "Anyway, I was taking hakido lessons, and we warmed up with yoga." 
    
    y "So that's probably the main reason why you're drooling over my butt." 
    
    show Gou Neutral with dissolve
    
    gm "I'm not drooling, though I wish my butt was that tight." 
    
    show Gou Worried 1 with dissolve
    
    gm "However, the same can't be said of certain members of the male persuasion in proximity to us." 
    
    d "Oh damn, I forgot the guys just stepped out." 
    
    d "Makoto's face is beet red, yet he can't turn away from me." 
    
    d "Rei also seems fixated on ogling me, but at least he's trying to avert his eyes." 
    
    d "The same cannot be said about Nagisa." 
    show Gou Worried 1 at right with dissolve
    show Nagisa Determined 1 at left with dissolve
    
    nh "Damn, Gou. Nice job of maximizing the hotness factor with the new girl." 
    
    nh "Now if we could just get you to manage practices in a swimsuit we'd be all set." 
    
    gm "I'd say only in your dreams, but I don't think I want to place that seed in your conscience." 
    
    d "And then there's Haru." 
    
    d "Haru..." 
    
    d "Haru is already in the pool." 
    
    d "I have no way of knowing if he's noticed me or not." 
    
    d "Why do I feel a bit disappointed about that?" 
    
    show Rei Neutral at center with dissolve
    
    rr "Hey, %(povLastName)s, what stroke do you feel most comfortable with?" 
    
    y "I'd prefer not to have a stroke like I just did with you guys checking me out." 
    
    rr "The lady makes a jest. You know what I mean." 
    
    rr "What swimming style do you prefer to start with?" 
    
    y "I guess I'd prefer freestyle. I never was a fan of breast or back." 
    
    nh "I'm a fan of your breast and back!" 
    
    y "Hey Gou, what are sexual harassment laws like in Japan?" 
    
    show Nagisa Pouty with dissolve
    
    nh "Aw come on now, I was just teasing." 
    
    show Gou Mad with dissolve
    
    gm "Nagisa, stop making lewd comments and get swimming." 
    
    hide Rei with dissolve
    
    hide Nagisa with dissolve
    
    show Gou Neutral at center with dissolve
    
    gm "Okay, %(povFirstName)s, as you've indicated freestyle that means you'll be working with Haru." 
    
    gm "He's our top freestyle swimmer, and frankly he needs practice teaching." 
    
    show Gou Worried 1 with dissolve
    
    gm "He didn't exactly do a very good job teaching Rei." 
    
    show Gou Neutral with dissolve
    
    gm "But first, let's warm up. Basic breathing exercises followed by some laps." 
    
    y "If you say so." 
    
    hide Gou with dissolve
    
    d "We get in and I already feel like I'm dragging them down." 
    
    d "No way do they need to do remedial breathing training and water adjustment." 
    
    d "But they suffer through it for my sake, or so I think." 
    
    d "After that and some laps, Haru swims over to me." 
    
    show Haru Neutral at center with dissolve
    
    hn "You said you've swam before, right?" 
    
    y "Yes, though it has been a little while since I've done it." 
    
    hn "Let's go over the basic motion and see how quickly you can pick it back up." 
    
    hide Haru with dissolve
    
    d "Haru goes over the routine of correct diving and freestyle form with me." 
    
    d "I think I'm picking it back up quickly, and Haru seems satisfied." 
    
    d "After about an hour or so Gou tells us to go take a short break." 
    
    d "I go to the water fountain, and Haru follows me there." 
    
    show Haru Neutral at center with dissolve
    
    hn "I'm glad you've swam before, it really shows." 
    
    hn "Unlike Rei, who had never swum in his life, you already have the form in your head." 
    
    hn "So it's just your body readjusting to using the stroke again." 
    
    y "Thanks, but I dont' think I'm doing that well." 
    
    hn "Trust me, you are." 
    
    d "He takes a long swig from the fountain and walks back." 
    
    hide Haru with dissolve
    
    d "That actually made me feel more comfortable." 
    
    d "I mean, about as comfortable as I can be swimming for the first time in years." 
    
    d "As the only female amgonst a pool full of dudes." 
    
    d "In a competition suit that's squishing my chest." 
    
    d "With the team manager ready to take a picture of my butt to post on Chirper." 
    
    d "Makoto's waving everyone in, so I head back." 
    
    show Makoto Neutral at center with dissolve
    
    mt "So for fun, we're going to have an initial race between %(povLastName)s and Haru." 
    
    mt "This will give us an idea of how much time $(povLastName)s has to shave to even get close to Haru's time." 
    
    y "Hey, me and my big mouth intend to beat Haru, you know." 
    
    hide Makoto with dissolve
    
    show Gou Worried 1 at center with dissolve
    
    gm "I know, but the reality is that the best male swimmer is still faster than the best female." 
    
    gm "Guys tend to be faster from the get-go due to their strength." 
    
    gm "Maybe if it were endurance and distance you'd have a better shot, since girls tend to be better in those respects." 
    
    show Gou Neutral with dissolve 
    
    gm "But anyway, it's just for fun. Plus it'll help you get used to actual racing again." 
    
    y "Well, okay." 
    
    hn "..." 
    
    hide Gou with dissolve
    
    show Nagisa Determined 1 at center with dissolve
    
    nh "Anyway, get your caps and goggles on." 
    
    nh "We don't have a starters pistol available right now, so I'll count down from three and you dive on Go." 
    
    hide Nagisa with dissolve
    
    d "I put on my equipment and walk to the block next to Haru, who is already ready to go." 
    
    d "He seems a bit disinterested." 
    
    y "Hey, you okay? You really want to do this?" 
    
    show Haru Neutral at center with dissolve
    
    hn "Hm? Oh, I guess. I don't really care about competing, really." 
    
    hn "I just like swimming, but I guess competition comes with being in the club." 
    
    nh "The race is 100 meters, which is two laps." 
    
    nh "Racers to your marks." 
    
    d "Haru and I take our positions on the blocks." 
    
    nh "And three..." 
    
    nh "two..." 
    
    nh "one..." 
    
    nh "GO!"
    
    hide Haru with dissolve
    
    d "We both dive off into the clear water and try to push as much under as we can before coming up." 
    
    gm "She had a really nice dive into the pool there." 
    
    gm "She's extending her arms nicely, too." 
    
    gm "She's faster than I thought she'd be for not having been in the pool for a while." 
    
    gm "Of course, she was doing hakido and yoga so she's probably in decent shape." 
    
    nh "Her legs seem to be keeping an even rhythm, too." 
    
    nh "That seems to really help her stroke point." 
    
    nh "She's actually not too far off the pace." 
    
    d "We're coming up to the turn, and I realize that I'm actually enjoying this." 
    
    d "Not so much the race, but just swimming in general." 
    
    d "When we go underwater for the turn I notice that Haru is looking at me." 
    
    d "I can't tell his expression through his eyes underwater though." 
    
    d "He seems to be lingering his gaze just a little." 
    
    d "Soon enough he's up and off again." 
    
    mt "Wow. She's really good." 
    
    mt "She won't beat Haru but I'd give her a decent shot at winning in competitions." 
    
    nh "Haru touches the wall first, winning the race." 
    
    nh "%(povLastName)s follows up a mere 4 seconds behind." 
    
    nh "Wow, that's not bad at all." 
    
    d "I take a moment to relax after the race." 
    
    d "Back when I was younger I didn't take losing so well." 
    
    d "This time, though, I just don't care." 
    
    d "It was really fun just swimming and getting my mind off of everything else." 
    
    d "Like nightmares. And writing Japanese. And crumpled water bottles stalking my feet." 
    
    show Haru Neutral at center with dissolve
    
    hn "Hey, %(povFirstName)s." 
    
    d "Haru has extended his hand out to help me out." 
    
    d "I grab hold and climb up, and Rei hands me my towel." 
    
    hn "Nice job out there. You did great." 
    
    y "Well, you did help me remember how it was done, senpai." 
    
    hn "Cut it out, we're in the same grade." 
    
    y "I know, I was just teasing." 
    
    d "The rest of the club has caught up to us, and they're raving about my performance." 
    
    hide Haru with dissolve
    
    show Makoto Neutral at center with dissolve
    
    mt "You looked like an old pro out there." 
    
    show Gou Neutral at left with dissolve
    
    gm "You were so cool." 
    
    show Nagisa Sarcastic at right with dissolve
    
    nh "You are so hot!" 
    
    y "Really, Nagisa?" 
    
    show Nagisa Pouty with dissolve 
    
    nh "I only speak the truth." 

    y "Well thanks everyone. Really. I mean it. I'm going to try my best to make us the best swim club we can be." 
    
    gm "Of course you will! I Knew you would from the start." 
    
    mt "I think that's enough for one day." 
    
    mt "Let's clean up and get going home." 
    
    d "Everyone starts filling out. Just as I head for the girls locker room. I see Haru waiting and looking at me." 
    
    scene bg School Lockers_01 with dissolve
    
    show Haru Neutral at center with dissolve
    
    hn "By the way, %(povFirstName)s, welcome to Japan, and to Swim club." 
    
    hn "Hope you enjoy it." 
    
    return
    
label Makoto_Romance_Route:
    
    #Chapter 1
    y "I guess." 
    
    y "How does Makoto sound?" 
    
    y "He's been wanting to hang out ever since we met." 
    
    d "Gou's contemplating this in her head." 
    
    show Gou Worried 1 at center with dissolve
    
    gm "Sure, I believe he's over at Haru's place right now." 
    
    gm "Although, he may bring Haru over with him." 
    
    gm "The two of them are basically attached at the hip." 
    
    d "Gou dials Makoto's number as I stir the chili, pretending to be uninterested." 
    
    show Gou Neutral with dissolve
    
    gm "Hey Makoto, %(povFirstName)s is dying for you to try this meal she is making." 
    
    y "Gou, stop it!" 
    
    d "Gou flashes me a sly smile as she continues her conversation." 
    
    gm "Are you avilable to come over for dinner?"
    
    mt "Sure! Is it ok if Haru tags along? He seems eager to come." 
    
    d "Haru, eager? I don't think I want to know what that looks like." 
    
    gm "Great! %(povFirstName)s is gonna be thrilled!" 
    
    y "Stop it!" 
    
    gm "See you guy's in a bit." 
    
    d "Gou hangs up as Rin walks in behind her." 
    
    show Gou Neutral at left with moveoutleft
    
    show Rin Smile at right with dissolve
    
    rm "Who's coming over?"
    
    gm "Makoto and Haru, %(povFirstName)s is eager to have Makoto try her chili." 
    
    d "Gou turns to me and winks." 
    
    y "Only you could turn something as pure as a chili cookout into something dirty." 
    
    show Rin Neutral with dissolve
    
    rm "I'm a little offended. Is the two of us eating your chili not good enough?" 
    
    gm "Ew, I don't want to think about you eating anybody's chili!" 
    
    y "If one more person says something dirty about the chili, I'm gonna throw it out the window!" 
    
    rm "Alright, I'm sorry." 
    
    show Rin Smile with dissolve
    
    rm "I was hoping to talk to you more, you'll have to spare some time for me later." 
    
    y "No promises." 
    
    d "Rin smirks at me and heads back to the living room." 
    
    hide Rin with dissolve
    
    hide Gou with dissolve    
    
    d "Geez, I go from having practically no friends in the U.S. to having far too many here in Japan." 
    
    d "With all the excitment finally calming down, I can get to work on the chili. I gather the ingredients and get to work. Sooner than I expected, the door rings." 
    
    rm "I'll get it." 
    
    d "Rin heads to the door, stops to put on a disinterested face, and opens it to reveal Haru and Makoto." 
    
    rm "We don't want any." 
    
    d "Makoto smiles weakly at Rin, unable to tell if his greeting was meant to be rude or humorous." 
    
    mt "Hi Rin, good to see you." 
    
    hn "...." 
    
    mt "May we come in?"
    
    rm "I'm not gonna stop you." 
    
    d "Makoto and Haru enter as Rin walks away from the door and back to the couch." 
    
    d "As they walk further into the house Makoto's gaze meets mine." 
    
    show Makoto Neutral at center with dissolve 
    
    mt "%(povLastName)s, there you are!"
    
    d "My god, his face just lit up. Is this normal? Is he part light post? He's tall enough to be." 
    
    d "Who on Earth exudes this much positivity?!" 
    
    show Makoto Sad with dissolve
    
    mt "%(povLastName)s, are you ok?" 
    
    d "Oh god. How long was I staring?" 
    
    y "Yea, I was just thinking about all the work I still have to do. Hehe...I better get back to it!" 
    
    d  "Just as I was about to scramble away I hear Makoto call out to me." 
    
    show Makoto Worried with dissolve
    
    mt "Wait %(povLastName)s! Do you need any help?" 
    
    d "I could use the help..." 
    
    y "Sure, mind cutting some onions? I hate doing it." 
    
    show Makoto Neutral with dissolve
    
    d "Makoto lights up once again at the chance to help." 
    
    mt "Sure, it would be my pleasure." 
    
    d "I lead Makoto into the kitchen and show him where I've laid out the cutting board." 
    
    y "Alright, while you work on those I'll start mixing some of the other ingredients." 
    
    mt "Sounds like a plan." 
    
    d "We both set to work. It's a little awkward with no one talking." 
    
    mt "So, any idea what stroke you're going to specialize in? I'm really looking forward to seeing you swim." 
    
    y "I wouldn't set your hopes too high, I haven't swam in a whle, I'm probably rusty." 
    
    mt "No way, swimming is like riding a bicycle, you never really forget." 
    
    y "What if I've never learned how to ride a bicycle?" 
    
    mt "Well then you're out of luck, I'm not sure what to tell you." 
    
    d "I smile slightly at that." 
    
    y "I actually am really excited to swim competitively again. Although, I'm a little disappointed that I won't be able to compete with you guys." 
    
    mt "It'll still be fun, you'll see! There's tons of solo competitions for women in the area, and we'll be there to cheer you on. YOu should see Haru when he's fired up, it's inspiring!" 
    
    y "Haha!" 
    
    d "We each go back to our task and soon return to working in silence." 
    
    d "After a while, I turn around to check on Makoto's progress with the onions." 
    
    show Makoto Worried with dissolve
    
    d "He seems to be struggling. As I walk closer, I realize that he's rubbing his eyes vigorously to fight back tears." 
    
    d "I grab his wrist in concern." 
    
    y "Makoto! Why don't you say something? I'm so sorry for asking you to cut all of these onions yourself, it's obviously a two person job." 
    
    mt "No, I'm a man. I can do this!" 
    
    d "Makoto rubs his eyes and strikes a heroic pose as he continues. I can't help but laugh at his antics." 
    
    y "Hahahahaha!" 
    
    d "I laugh wholeheartedly, for the first time in a while, and Makoto looks at me like I've grown a second head." 
    
    d "I try to calm myself so I can make sure Makoto is ok." 
    
    y "Hehe...oh. Are you ok Makoto? Is something wrong?" 
    
    show Makoto Bashful with dissolve
    
    mt "No...I mean...it's just." 
    
    d "He blushes slightly as he fumbles to find the right words." 
    
    d "I feel heat pooling in my cheeks as my face turns bright red." 
    
    d "As I struggle to find a response, I hear the chili pot boiling over." 
    
    y "Oh No!" 
    
    show Makoto Worried with dissolve
    
    mt "I'll get it!" 
    
    d "Makoto and I both rush to turn down the heat." 
    
    d "I reach the knob first but Makoto rushes besides me and bumps into me as he too reaches for the knob." 
    
    d "I quickly turn only to realize I'm flush against Makoto's chest." 
    
    show Makoto Bashful with dissolve
    
    d "We both blush at our closeness." 
    
    y "I..." 
    
    d "I'm about to apologize when Haru suddenly enters the kitchen." 
    
    show Haru Neutral at left with dissolve
    
    hn "Hey is the food almost...What are you guys doing?"
    
    d "Makoto and I yank ourselves away from each other." 
    
    show Makoto Worried at right with moveoutright
    
    mt "Nothing!" 
    
    y "Nothing!" 
    
    hn "Haru looks confused, but quickly gets over it." 
    
    hn "Whatever, is the special dish you're making going to have mackerel in it?" 
    
    y "No Haru." 
    
    d "Makoto and I look at each other and begin to laugh." 
    
    show Makoto Bashful with dissolve
    
    hn "Whatever, you guys are acting weird." 
    
    hide Haru with dissolve
    
    show Makoto at center with moveoutleft
    
    d "Haru walks back into the living room as Makoto and I continue laughing." 
    
    d "Finally, we calm down and meet each other's gaze." 
    
    mt "I guess we better take the food out." 
    
    y "Yea, I hope everyone likes it. Apparently Haru is already disappointed." 
    
    mt "Aw, don't mind him. He just has very particular taste. I'm sure everyone will love it." 
    
    y "Yeah." 
    
    d "We fill bowls for everyone and yell for them to head to the dining room. As Makoto leaves I call out to him." 
    
    y "Wait! Makoto!" 
    
    mt "Makoto stops and turns to look at me." 
    
    mt "Yea?" 
    
    d "I look down at my feet as I feel my cheeks growing hot again." 
    
    y "Thanks for helping!" 
    
    show Makoto Neutral with dissolve
    
    mt "Anything for you %(povFirstName)s." 
    
    d "With that said, Makoto walks out to meet Haru." 
    
    hide Makoto with dissolve
    
    scene bg Dining Table 2 with dissolve
    
    d "I rub my cheeks as I walk to the dining room." 
    
    y "I guess the chili isn't going to be the only hot thing at the dinner table." 
    
    d "I walk in to find the table set and everyone sitting." 
    
    d "Rin and Sousuke are sitting across from each other at the ends of the table, while Makoto and Haru sit next to each other on one side of the table." 
    
    d "That leaves me the spot next to Gou on the side of the table opposite Makoto." 
    
    d "I wonder if Gou planned this." 
    
    d "Seeming to read my thoughts, Gou turns to me and winks." 
    
    d "I take my seat as Makoto smiles at me from across the table." 
    
    y "Alright everyone, dig in!" 
    
    d "Everyone fills their bowl and stares." 
    
    show Gou Worried 1 at center with dissolve
    
    gm "Is it...supposed to look like this?" 
    
    y "Yes Gou. Geez, if you keep talking like that you're going to hurt the chili's feelings." 
    
    hide Gou with dissolve
    
    d "Despite my use of humor, it's my own feelings that are being hurt. I had really hoped everyone would like it." 
    
    d "Everyone is looking, horrified, at their bowls and I feel my heart begin to sink." 
    
    d "Across from me, Makoto is holding his spoonful of chili to his mouth as if it were a spoonful of poison." 
    
    y "Psst...Makoto." 
    
    show Makoto Worried at center with dissolve
    
    d "Startled, Makoto puts down his spoon to look at me." 
    
    mt "Yeah %(povFirstName)s?"
    
    y "You don't have to eat it if you don't want to." 
    
    d "Suddenly, Makoto perks up and his eyes glow with a newfound confidence." 
    
    show Makoto Neutral with dissolve
    
    mt "No %(povFirstName)s, it's like the onions, I am a man and I can do this." 
    
    d "Makoto bravely picks up his spoon and takes a large bite." 
    
    d "His eyes widen as he chews, and swallows." 
    
    show Makoto Bashful with dissolve 
    
    mt "Wow %(povFirstName)s, this is really good!" 
    
    hide Makoto with dissolve
    
    d "Makoto starts to eagerly eat his meal, which encourages the others to dig in." 
    
    show Rin Smile at center with dissolve
    
    rm "Wow %(povLastName)s, this is really good!"
    
    show Gou Neutral at left with dissolve
    
    gm "It's so spicy, I love it!"
    
    show Makoto Neutral at right with dissolve
    
    mt "We never should have doubted you you %(povFirstName)s. If you made it, it's bound to be great." 
    
    d "Makoto shoots another blinding smile from across the table and all of my insecurities melt away as I begin to enjoy my dinner." 
    
    d "Once everyone decided that their food wouldn't kill them, it went pretty fast." 
    
    gm "I'm stuffed!" 
    
    mt "I couldn't eat another bite." 
    
    d "Everyone is holding their stomach contently." 
    
    rm "Who knew something so disgusting looking could taste so good." 
    
    hide Makoto with dissolve
    
    hide Rin with dissolve
    
    hide Gou with dissolve
    
    show Haru Neutral at center with dissolve
    
    hn "It was no mackerel, but it wasn't bad." 
    
    hide Haru with dissolve
    
    show Sosuke Smile at center with dissolve
    
    sy "You'll have to cook for us again sometime %(povLastName)s." 
    
    y "I'd be happy to." 
    
    hide Sosuke with dissolve
    
    show Makoto Neutral at center with dissolve
    
    mt "Why don't I clean up the dishes?" 
    
    show Gou Worried 1 at right with dissolve
    
    gm "Nonsense, you and $%(povFirstName)s did all the work cooking. Rin and I will clean up while you four relax." 
    
    show Rin Neutral at left with dissolve
    
    rm "What, why me?!" 
    
    show Gou Neutral with dissolve
    
    gm "Because they're our guests you jerk. Come on." 
    
    hide Gou with dissolve
    
    hide Rin with dissolve
    
    hide Makoto with dissolve
    
    d "Gou and Rin begin clearing the table while Makoto, Haru, Sousuke, and I head to the living room." 
    
    d "I'm starting to think I'll really enjoy my time here in Japan." 
    
    scene bg Living Room 2 with dissolve
    
    d "After dinner, we all sat in the living room and talked." 
    
    d "As the sun began to set, everyone began to file out." 
    
    scene bg MC Bedroom 2 with dissolve
    
    d "Finally time to get some sleep." 
    
    scene bg white with dissolve 
     
    y "I don't understand! Why do we have to leave?!" 
     
    unknown "Hush %(povFirstName)s, we don't get a choice." 
     
    y "But I don't wanna go!" 
     
    unknown "Neither do I Hun." 
     
    y "Then make dad change his mind!" 
     
    unknown "Come on honey, get in the car." 
     
    y "Nooo!" 
     
    scene bg MC Bedroom 1 with dissolve
     
    y "Ah!" 
     
    d "I jolt upright, breathing heavily." 
     
    d "I haven't thought of that day in a while." 
     
    d "I use the breathing techniques I've learned to try to calm myself down." 
     
    d "Looking at the clock, I realize that it's about time for me to get up anyway." 
     
    scene bg Bathroom with dissolve
     
    d "I change into my uniform and head to the bathroom to continue getting ready." 
     
    scene bg Hallway Entrance 1 
     
    d "Once ready, I grab my bag and open the door." 
     
    d "Only to see Haru and Makoto standing on the other side of it." 
     
    y "Ah!" 
     
    d "Startled, I slam the door in their faces." 
     
    d "I've had enough surprises for one day, thank you!" 
     
    d "What do they even want?" 
     
    d "I decide that shutting the door in my new friends faces, may not be the best way to keep them." 
    
    d "I slowly open the door again." 
     
    scene bg M Residence 1 with dissolve
     
    y "Hey guys, what do you want?" 
     
    show Makoto Neutral at right with dissolve
     
    show Haru Neutral at left with dissolve
     
    d "Makoto smiles at me, in his usual luminescent fashion." 
     
    mt "All we want is to accompany you to school." 
     
    y "How did you even know I was leaving?" 
     
    mt "Gou may have helped with that." 
     
    d "Of course she did." 
     
    y "Well, since you came all this way, I supposed I can give you the pleasure of accompanying me to school." 
     
    show Makoto Bashful with dissolve
     
    mt "We're honored." 
     
    hn "..." 
     
    scene bg Neighborhood A_1
     
    d "Makoto, Haru and I start walking to the station, where we meet with Rei and Nagisa." 
     
    show Nagisa Sarcastic at center with dissolve
     
    nh "Hey lovebirds, you're gonna miss the bus!" 
     
    y "Who are you calling lovebirds Nagisa?" 
     
    nh "Isn't it obvious?" 
     
    nh "Makoto is just using Gou as an excuse, he'd have come to walk you to school anyway." 
     
    nh "Cause he's in love~!" 
     
    d "Everyone goes wide eyed at Nagisa's statement, and poor Makoto looks mortified." 
     
    show Makoto Worried at right with dissolve
     
    mt "What, Nagisa, don't you think that's going too far?!" 
     
    nh "Hey, I call it like I see it." 
     
    show Haru Neutral at left with dissolve
     
    hn "Pft, what do you need a girlfriend for Makoto. You have me." 
     
    d "Haru's comment makes me think." 
     
    d "Maybe he's gay, that would explain why he was so comfortable stripping in front of me." 
     
    y "Hey Haru, in all seriousness, can I ask you a question." 
     
    hn "Sure." 
     
    y "Are you gay?" 
     
    hn "I'm water sexual." 
     
    d "Everyone laughs, but Haru's face seems pretty serious." 
     
    d "Maybe he just doesn't think about romance very much." 
     
    show Makoto Sad with dissolve
     
    mt "As much as I would love to continue embarassing myself, the bus is here." 
     
    d "We all pile onto the bus and head to school." 
     
    scene bg School Gates_Morning with dissolve
     
    scene bg School Lockers_01 with dissolve
     
    d "Once we arrive, we change our shoes and stop by our lockers." 
     
    scene bg Classroom A_01 with dissolve
     
    d "As I'm entering the door to homeroom, I brush up against Makoto's shoulder." 
     
    d "He smiles, and gestures for me to enter first." 
     
    d "As the bell rings, we all take our seats and take out our books." 
     
    d "Today goes a lot better than yesterday. I think my Japanese is improving." 
     
    scene bg Hallway A_01 with dissolve
     
    scene bg Stair Well A_01 with dissolve
     
    scene bg Stair Well B_01 with dissolve
     
    d "Once the lunch bell rings, I head to the roof." 
     
    d "According to Gou, the club meets on the roof to eat." 
     
    d "Either anime isn't lying or these guys are weirder than I thought." 
     
    d "As I'm walking up the stairs I notice Makoto at top of the stairs about to open the door leading to the roof." 
     
    d "I'm about to call out a greeting when I feel myself lose footing and start to fall backwards." 
     
    y "Makoto!" 
     
    d "I briefly see him turn around before my vision drifts to the roof." 
     
    d "Suddenly, I feel a pressure on the small of my back and something wrapped around my wrist."
     
    show Makoto Sad with dissolve
     
    d "I tilt my head up to find Makoto's concerned eyes looking into mine." 
     
    d "He had grabbed my hand and back, which put us in a bit of a salsa dancing situation." 
     
    y "Makoto..." 
     
    hn "Is someone dead?" 
     
    d "Haru must have heard the commotion." 
     
    d "Makoto lifts me up." 
     
    y "No, we're ok." 
     
    hn "That's good, I guess." 
     
    d "Haru turns in the doorway and goes back to the roof; Makoto and I follow him." 
     
    scene bg School Rooftop Entrance with dissolve
     
    scene bg School Rooftop with dissolve
     
    show Gou Neutral at center with dissolve
     
    gm "Hey %(povFirstName)s!" 
     
    show Gou Worried 1 with dissolve
     
    gm "Gosh, are you ok? You look like you might have a fever." 
     
    y "I'm fine. I think it might be the start of a cold." 
     
    d "I do feel a little light headed, but I know it's not because of a cold." 
     
    hide Gou with dissolve
     
    show Makoto Worried at center with dissolve
     
    mt "Oh no, %(povFirstName)s, is that why you fell back there?" 
     
    mt "Do you feel lightheaded?" 
     
    d "Makoto reaches up to feel my forehead, which grows hotter every second his hand remains." 
     
    y "I'm fine, I think I just need to get some food in me." 
     
    hide Makoto with dissolve
     
    d "I sit down and open my bento, which encourages everyone to sit and eat." 
     
    d "After I made the chili last night I started to miss food from home." 
     
    d "I ended up making a little smorgasbord of my favorite foods for lunch." 
     
    show Gou Neutral at center with dissolve
     
    gm "%(povFirstName)s, that looks so good!" 
     
    gm "Can I try some?" 
     
    y "Sure, you all can if you'd like." 
     
    hide Gou with dissolve
     
    d "Everyone goes in to try a bit of everything." 
     
    show Nagisa Determined 1 at center with dissolve
     
    nh "So yummy, Makoto will be lucky to have you as a wife." 
     
    show Makoto Mad at right with dissolve 
     
    mt "Nagisa!" 
     
    show Makoto Neutral with dissolve
     
    mt "It's really good %(povFirstName)s." 
     
    show Haru Neutral at left with dissolve 
     
    hn "Is that mackerel?" 
     
    d "Haru is scrutinizing a piece of fish from my bento." 
     
    y "Yea, I fried it in oil, lemon, and fennel." 
     
    d "Haru, tenatively, takes a bite." 
     
    d "Surprisingly, his face brightens a bit and his eyes widen." 
     
    hn "Not bad." 
     
    d "Haru grabs another piece." 
     
    mt "Wow %(povFirstName)s, Haru is really picky about his mackerel, you should feel really proud." 
     
    d "Actually, I do feel kind of proud. Maybe I should consider culinary school." 
     
    d "I see Haru eyeing the mackerel and gesture for him to come over to grab more." 
     
    d "He sits down next to me to continue eating." 
     
    d "I see Makoto gives Haru a surprisingly dirty look, but it's gone in an instant." 
     
    d "Haru continues eating the mackerel until there is only one piece left." 
     
    d "Just as he is about to grab it, I snatch it away." 
     
    d "Everyone laughs as Haru mopes." 
     
    d "The bell rings, signaling the end of lunch, so we all pack up our lunches and head back to class." 
     
    scene bg Classroom A_01 with dissolve
     
    d "The rest of the school day was, surprisingly, uneventful." 
     
    scene bg Swimming Pool A_2 with dissolve
     
    d "I pack up my supplies and follow Makoto and Haru to the school pool." 
     
    show Gou Neutral at center with dissolve
     
    gm "Alright everybody, Let's get to work!" 
     
    gm "As we all know, we have a new member with us." 
     
    d "The team stops to applaud." 
     
    gm "Now, as team manager, I have decided that the best person to help %(povFirstName)s get back in shape would be out team captain, Makoto." 
     
    d "Why am I not surprised." 
     
    gm "Oh, but first!" 
     
    d "Gou reaches into her bag and pulls out a swimsuit." 
     
    gm "Tada!" 
     
    gm "You're new swimsuit %(povFirstName)s!" 
     
    d "Guess, I'd have to put one on eventually." 
     
    scene bg Changeroom with dissolve
     
    d "Hesitantly, I take the suit from Gou and go to the bathroom to change." 
     
    scene bg Swimming Pool A_2 with dissolve
     
    d "I peek out the door to make sure the entire team isn't waiting to see me." 
     
    d "Thank goodness, everyone's started to warm up." 
     
    d "Gou is the eexception; she's waiting outside eagerly." 
     
    d "I sign, resignedly, and exit the bathroom." 
     
    show Gou Neutral with dissolve 
     
    gm "Wow %(povFirstName)s, you look so cute!" 
     
    d "At least the swimsuit isn't too flamboyant. It's the same navy like color that the boys' suits are, but it has a white trim, and is a one piece." 
     
    gm "You know, you have surprisingly good muscle tone for someone who hasn't swam in a while." 
     
    y "The suit feels really tight. I feel like a sausage, and I asked for gray trim." 
     
    show Gou Worried 1 with dissolve
     
    gm "Hey, there's no moping during training." 
     
    show Gou Neutral with dissolve 
     
    gm "You're gonna do great!" 
     
    gm "Alright everyone, enough stretching, time to get in the water!" 
     
    hide Gou with dissolve
     
    show Rei Neutral with dissolve
     
    rr "Hey %(povLastName)s, as a pretty new swimmer myself, I'm curious; which stroke are you thinking of specializing in?" 
     
    y "I hadn't really thought about it much, I guess freestyle for now, that way I can get to know all the strokes, and can use whichever I feel most comfortable with." 
     
    gm "Enough chit chat %(povFirstName)s, get in the pool!" 
     
    hide Rei with dissolve
     
    y "*Grumbles*" 
     
    show Gou Determined with dissolve
     
    gm "That better not be moping I hear!" 
     
    y "No." 
     
    d "She sure does take her job seriously." 
     
    hide Gou with dissolve
     
    mt "Come on %(povFirstName)s, the waters great!" 
     
    d "I hear Makoto call out to me from the pool." 
     
    d "Let's get this over with." 
     
    d "I enter the water slowly to get adjusted to the temperature." 
     
    show Makoto Neutral with dissolve
     
    mt "Alright, I heard you mentioned to Rei that you are thinking about swimming freestyle." 
     
    mt "The most popular stroke people use in feestyle is the front crawl, because of how fast it is." 
     
    mt "Want to give it a shot?" 
     
    y "Seems like a good place to start." 
     
    d "Turns out the front crawl is pretty much the first thing every person learns when they're taught to swim." 
     
    d "The trick is doing it fast without hurting yourself." 
     
    mt "Alright %(povFirstName)s, you're looking good." 
     
    d "He's right, I can do this. One arm up, other arm up." 
     
    y "Ouch!" 
     
    d "Suddenly, I feel a sharp pain in my side." 
     
    show Makoto Worried with dissolve
     
    mt "%(povFirstName)s!" 
     
    d "Makoto swims over to me and rests me against his chest." 
     
    mt "Are you ok?" 
     
    d "The new view is helping, who knew such hard muscles could feel so soft." 
     
    y "Yea, just a pulled muscle." 
     
    show Makoto Sad with dissolve
     
    mt "You've got to watch your form. Make sure you're lengthening your body and moving your torso with each arm." 
     
    y "Ok." 
     
    hide Makoto with dissolve
     
    d "After learning the front crawl, I'm ready to try other strokes." 
     
    d "Makoto takes me through the basics of the backstroke, and the breaststroke." 
     
    show Gou Neutral at center with dissolve
     
    gm "I like what I'm seeing %(povFirstName)s!" 
     
    gm "Why don't we have a friendly race?" 
     
    mt "It would be excellent way for you to prepare for actual competitions." 
     
    show Gou Determined with dissolve 

    gm "I'm glad you feel that way Makoto, because you'll be her opponent." 
     
    mt "Me?!"
     
    gm "Yep, let's do this." 
     
    d "Everyone gets out of the pool to watch the race." 
     
    d "Makoto and I take our places at one end of the pool." 
     
    gm "Alright you two, To keep it fair you'll both be using the backstroke." 
     
    gm "Because %(povFirstName)s is just getting started, and her stamina is lower, we'll keep it short." 
     
    gm "One lap, first one back wins." 
     
    show Nagisa Determined 2 at right with dissolve
     
    nh "Gou, Gou! Can I do the countdown!" 
     
    gm "Sure Nagisa, knock yourself out." 
     
    hide Gou with dissolve
     
    hide Nagisa with dissolve
     
    d "Makoto and I crouch down in preparation to jump." 
     
    mt "Hey, %(povFirstName)s." 
     
    d "I glance over at Makoto." 
     
    show Makoto Neutral with dissolve
     
    mt "Good luck." 
     
    y "I don't need it. I learned from the best." 
     
    d "Makoto chuckles and gets back into position." 
     
    nh "Ready guys, one!" 
     
    d "I adjust my goggles." 
     
    nh "Two!" 
     
    nh "Three!" 
     
    hide Makoto with dissolve
     
    d "I leap into the water." 
     
    d "Right before I hit the water, I hear Gou yelling at Makoto." 
     
    gm "Makoto!" 
     
    gm "Quit staring at %(povFirstName)s and get in the water!" 
     
    d "I can hear Makoto hit the water behind me." 
     
    d "Despite my lead, I can tell the distance between us is closing." 
     
    gm "They're coming back around." 
     
    gm "%(povFirstName)s's strokes are impressive she's staying in perfect form!" 
     
    d "Makoto and I kicked off the opposite wall at about the same time, but Makoto's superior lower body strength pushes him into the lead." 
     
    d "I struggle to keep up. Pushing myself to go faster." 
     
    nh "It's gonna be close!" 
     
    nh "Go %(povFirstName)s!" 
     
    d "The world suddenly moves in slow motion as I approach the end of the lap." 
     
    d "I use my last burst of energy to rocket to the wall and throw my hand out of the water." 
     
    d "I raise my head out of the water, only to see that Makoto had already reached the wall." 
     
    gm "Wow %(povFirstName)s, you only lost by three seconds!" 
     
    mt "You really gave me a run for my money." 
     
    nh "You were amazing %(povFirstName)s." 
     
    rr "You claimed to be rusty, but I saw no evidence of that in your race." 
     
    hn "You're pretty good." 
     
    d "I hear everyone talking to me, but I'm not fully processing it." 
     
    d "I can't get over how amazing it felt to race again." 
     
    gm "%(povFirstName)s, are you ok?" 
     
    y "Yea, It's just..."
     
    y"I forgot how nice it is to be in the water." 
     
    y "It makes me feel..."
     
    y "Free." 
     
    d "I feel a huge grin spread across my face and watch it spread to each team member." 
     
    d "Makoto gets out of the pool and offers me his hand." 
     
    d "I accept it, and he helps me out of the pool." 
     
    d "We stand together as he places his free hand on top of our already intertwined hands." 
     
    show Makoto Bashful at center with dissolve
     
    mt "I'm proud of you %(povFirstName)s." 
     
    y "You should be proud of yourself for being such a good teacher." 
     
    nh "Hey %(povFirstName)s, it's time for your initiation!" 
     
    d "The rest of the team encircles Makoto and I, and begins shouting." 
     
    d "Welcome to the Swim Club!" 
     
    d "I feel the ethereal feeling that enveloped me in the water spread over me again." 
     
    y"Thank you guys. I'll do my best!" 
     
    d "The team continues chanting and, in the excitement, I didn't notice that Makoto never ever let go of my hand." 
     
    #Chapter 2 
     
    scene bg MC Bedroom 4 with dissolve
     
    d "After practice, the team dispersed and headed home." 
     
    d "I was finally getting a peaceful night's sleep, when a knock on the door woke me up." 
     
    d "Seriously, I feel like I got run over by a truck, I deserve to sleep!" 
     
    d "After a bit of mumbling and grumbling, I get up to see who it is." 
     
    show Gou Worried 1 at center with dissolve
     
    gm "What are you doing %(povFirstName)s? You're going to be late!" 
     
    y "...To what?"
     
    gm "*sigh* You're hopeless." 
     
    gm "You promised to meet Makoto at Haru's place for game day!" 
     
    hide Gou with dissolve
     
    d "...Crap."
     
    d "I scramble to get dressed and make myself presentable." 
     
    scene bg Hallway Entrance 1 with dissolve
     
    y "I can't believe I forgot!" 
     
    show Gou Neutral at center with dissolve 
     
    gm "I can't believe you forgot either!" 
    
    y "I'm gonna be late!" 
     
    gm "You probably are!" 
     
    y "Don't you have something better to do?"
     
    gm "Nope, you're my new hobby." 
     
    hide Gou with dissolve
     
    d "I roll my eyes at Gou's comment and race to the front door." 
     
    hide Gou with dissolve
     
    d "Before I can exit, my mind is flooded by memories of yesterday." 
     
    d "Makoto holding my hand, Makoto letting me rest on his chest, Makoto and his blinding smile!" 
     
    d "Suddenly, I feel my heart begin to beat rapidly, and my hands begin to shake." 
     
    d "I try to calm myself down." 
     
    d "It's nothing. I can't let this feeling ruin my new friendships." 
     
    d "Using a new found burst of confidence, I throw the door open and run out." 
     
    scene bg M Residence 1 with dissolve
     
    y "I'm going!"
     
    gm "Wait, you forgot your phone!" 
     
    d "Gou runs out the door." 
     
    show Gou Worried 1 at center with dissolve
     
    gm "How are you going to get there without your GPS?!"
     
    hide Gou with dissolve
     
    d "After making a couple of wrong turns, I manage to find Haru's house." 
     
    scene bg Neighborhood A_1 with dissolve
     
    scene bg M Residence 1 with dissolve 
     
    d "It's a cute little house. Like the rest of the town, it's quaint and old-fashioned."
     
    d "I'm surprised. I never expected Haru to live somewhere so homey." 
     
    d "After admiring the house for a bit, I knock on the door." 
     
    scene bg Hallway Entrance 1 with dissolve
     
    show Haru Neutral at center with dissolve
     
    hn "You're late." 
     
    y "Hello to you too Haru." 
     
    y "Can I come in?"
     
    hn "Yea, come on." 
     
    d "The house is nice, but something feels off." 
     
    d "I notice there are only two pairs of shoes at the door and I don't hear any movement in the house." 
     
    y "Do you live alone Haru?" 
     
    hn "Yea, I used to live with my grandmother, but she died a couple of years ago." 
     
    show Haru Worried with dissolve
     
    y "Oh, I'm sorry I asked." 
     
    hn "It's fine, it's been awhile since it happened." 
     
    hn "My parents were overseas at the time. THey offered to come back, but I told them I would be fine." 
    
    y "Don't you get lonely?"
     
    show Haru Neutral with dissolve 
     
    hn "No, it's hard to be lonely with Makoto around." 
     
    d "I could see that." 
     
    d "Hearing Haru talk like that makes me a little jealous. I wish I had a friend I was that close with." 
     
    y "You and Makoto remind me of a friend of mine." 
     
    y "Before her new relationship tore us apart." 
     
    d "Suddenly, I'm reminded of all the pain my 'friendships' have brought me." 
     
    hn "Relationships will do that." 
     
    y "Sadly, I'm used to it." 
     
    hn "What about you?"
     
    y "What?" 
     
    hn "Have you ever been in a relationship?"
     
    y "Why do you want to know that all of a sudden." 
     
    hn "It's relevant to our conversation." 
     
    d "That's true." 
     
    y "I've had a couple boys ask me out, but I've never accepted." 
     
    y "I don't see the point in wasting my time dating if the person isn't special." 
     
    hn "Interesting." 
     
    y "Really?"
     
    hn "Yea, I agree with you." 
     
    y "Yay, we have something in common!" 
     
    y "We can bond over it!" 
     
    d "Haru rolls his eyes." 
     
    d "I finally hear some noise in the house as Makoto comes out of the bathroom." 
     
    show Haru at left with moveoutleft
     
    show Makoto Neutral at right with dissolve
     
    mt "Oh, %(povFirstName)s, I didn't know you were here." 
     
    y "Yep, Haru and I were just bonding." 
     
    d "Jokingly, I throw my arms around Haru's shoulder." 
     
    d "He quickly squirms from me and stands next to Makoto." 
     
    mt "So, how are you today?" 
     
    d "Makoto looks strangely flushed." 
     
    d "I hope whatever was going on in the bathroom wasn't serious." 
     
    y "I'm fine. Sorry I'm late." 
     
    hn "Enough chit-chat. It's time to play." 
     
    d "Haru had apparently slipped away and managed to, already get the game setup." 
     
    y "Alright Makoto, you may have beaten me at our race yesterday, but I will not lose to you here." 
     
    show Makoto Devious with dissolve
     
    mt "Challenge accepted." 
     
    scene bg Living Room 1 with dissolve
     
    d "We play a couple different games, and, surprisingly, Haru wins them all." 
     
    y "My god, video games, and swimming. Is there anything Haru can't do?" 
     
    show Makoto Neutral at right with dissolve 

    show Haru Neutral at left with dissolve
     
    mt "Apparently not." 
     
    hn "I'm bored." 
     
    mt "We could go see a movie or something." 
     
    y "Sure, I'm tired of getting my butt handed to me anyway." 
    
    y "You know, besides school and Gou's place, I haven't seen much of the town." 
     
    y "I'd love to see what theaters are like in Japan." 
     
    show Makoto Worried with dissolve
     
    mt "Whoa, you've been here for this long, and you haven't gone to see the sights." 
     
    y "There just hasn't been much time." 
     
    show Makoto Neutral with dissolve 
     
    mt "Well we have the time now, right Haru." 
     
    hn "It would be a waste to be in Japan, and not actually see Japan." 
     
    y "Really? Let's go!" 
     
    scene bg Park 1 with dissolve
     
    d "Haru and Makoto take me to a train that runs into a city a couple miles away." 
     
    d "We check out a few cafes and stores, before we decide to stop in a park for a break." 
     
    y "I didn't think it was possible for me to feel more sore." 
     
    show Makoto Neutral at center with dissolve
     
    mt "Don't worry %(povFirstName)s, a couple more practices and you'll be back in shape." 
     
    y "I don't think I'll survive!" 
     
    hn "I'll go get us some drinks." 
     
    d "Haru walks across the park to the vending machine, leaving Makoto and I alone together." 
     
    d "Makoto takes a seat next to me on the bench, and wrings his hands nervously." 
     
    show Makoto Bashful with dissolve
     
    mt "...So it's a lovely day isn't it?" 
     
    y "Is that the best you could come up with?" 
     
    d "Makoto blushes shyly." 
     
    mt "Hey, I'm trying." 
     
    mt "I know I've said it before, but you really do have a beautiful smile." 
     
    d "I feel myself getting nervous as well." 
     
    y "It's nothing compared to yours, yours is blinding." 
     
    mt "What can I say, I like to smile." 
     
    mt "I've noticed you seem to like smiling too." 
     
    mt "At least, more than you did when you arrived here." 
     
    y "Yea, sorry for being so tense when we first met." 
     
    y "It's always been kinda hard for me to make friends, but you guys have made it more easy." 
     
    y "it's hard not to smile when you all are around." 
     
    d "Thoughtfully, I look down at the ground." 
     
    y "I really like you guys, especially you Makoto." 
     
    d "Makoto is taken aback." 
     
    d "His face turns beat red and he begins to flail his arms nervously." 
     
    mt "%(povFirstName)s, I'm...I'm flattered really. I don't know what to say!" 
     
    d "I decide to let Makoto off the hook." 
     
    y "Makoto, it's ok. I meant I really like you as a friend." 
     
    y "Especially since you were the first to talk to me." 
     
    d "Makoto seems relieved when I say that, but also a little bit disappointed?" 
     
    mt "Oh...good. Sorry I panicked like that." 
     
    y "It's fine. I think Haru is coming with the drinks." 
     
    y "Let's just try to relax." 
     
    show Makoto at right with moveoutright
     
    show Haru Neutral at left with dissolve
     
    hn "You ok Makoto? You look like a tomato." 
     
    mt "It's nothing, just thirsty." 
     
    d "We all sip on our drinks and enjoy light conversation." 
     
    d "All the awkwardness from me and Makoto's conversation seems to have dissipated." 
     
    d "Makoto and I were listening to Haru's tips on how to beat the video game we were playing earlier, when I notice three girls walking towards us." 
    
    d "I feel my stomach churn with anxiety at their approach." 
     
    d "The shortest girl, who seems to be leading the other two, has long blonde hair and a perfect tan." 
     
    d "The tallest girl has wavy brown hair and pale skin, while the middle one has short, colorful, curly hair and a naturally dark pallor." 
     
    d "They don't seem to notice me as they strike up a conversation with Makoto and Haru." 
     
    bg "Hey you two, I could see your muscles from across the park." 
     
    d "Makoto becomes flustered at her fowardness, while Haru seems ambivalent." 
     
    mt "Oh, really. Wow, thank you." 
     
    bg "Aw, you're shy. So Cute." 
     
    bg "You gotta name cutie?" 
     
    show Haru Annoyed with dissolve
     
    show Makoto Worried with dissolve
    
    d "Makoto looks absolutely frightened at this point and Haru seems to be getting annoyed." 
     
    bg "I'd love to get together with you some time." 
     
    d "Haru's silence seems to have turned her off." 
     
    d "Now she is focusing on Makoto." 
     
    d "Makoto turns to me with a pleading look on his face." 
     
    menu: 
        "Help Makoto": 
             y "Excuse me ladies, I hate to interrupt, but you seem to be making my boyfriend very uncomfortable." 
             
             d "The girls look at me, as if noticing me for the first time." 
             
             d "Makoto and Haru look shocked." 
             
             bg "Boyfriend?" 
             
             bg "How come he didn't say anything about you?" 
             
             y "You said it yourself, he's very shy and very polite." 
             
             y "I'm sure he just didn't want to hurt your feelings." 
             
             y "Right honey?" 
             
             d "I give Makoto a knowing look hoping he'll play along." 
             
             show Makoto Bashful with dissolve
             
             mt "Yea...That's right." 
             
             mt "I'm sorry I made you sit through that darling, but you know how I hate to disappoint people." 
             
             y "It's fine dear." 
             
             y "You see, he's not interested." 
             
             d "The blonde girl looks me up and down, and decides to back off." 
             
             bg "Oh, alright." 
             
             bg "But if you ever change your mind, here's my number." 
             
             d "The lader gives Makoto a slip of paper and leads her posse away." 
             
             show Haru Neutral with dissolve
             
             hn "Nice work %(povFirstName)s." 
             
             y "Thanks. You ok Makoto?" 
             
             mt "Yea, thanks for saving me %(povFirstName)s!" 
             
             y "No problem, I'd pretend to be your girlfriend anytime." 
             
             d "Makoto laughs and even Haru smiles a little." 
             
             y "Now, why don't we get home. I think I've had enough of the city." 
             
             d "The three of us head to the station, eager to get back to our little town by the sea." 
             
             
        "Remain Silent.": 
            
            d "I decide it would be best for me to keep quiet." 
            
            d "I turn away from Makoto, and hope he can fend for himself." 
            
            mt "I...I...I"
            
            hn "Hey you're scaring my friend. He's not interested." 
            
            show Haru Annoyed with dissolve
            
            bg "Ugh, rude. Why would he be scared of me?" 
            
            hn "Because you're attaching yourself to him like a leech." 
            
            bg "Whatever, you both aren't worth this much work." 
            
            d "The blonde girl leads her posse away." 
            
            mt " I guess we should start heading home, right %(povFirstName)s?" 
            
            y "Yea, I've had enough of the city." 
            
            d "The three of us head back to the station, eager to get back to our tiny town by the sea." 
            
    scene bg M Residence 1 with dissolve 
     
    d "Makoto, Haru and I finally arrive back in town." 
        
    d "The train ride over had helped ease any lingering tension from our awkward encounter with those oddly familiar girls." 
        
    d "We reach Haru's house first." 
     
    y "Thanks for showing me around guys, I appreciate it." 
     
    hn "Sure." 
     
    mt "No problem %(povFirstName)s." 
     
    d "Haru walks to his front door, and turns to wave." 
     
    show Makoto Neutral at center with dissolve
     
    mt "Why don't I walk you home %(povFirstName)s? My house is back that way anyway." 
     
    d "We both wave goodbye to Haru and head back towards our houses." 
     
    scene bg Neighborhood A_1 with dissolve 
     
    show Makoto Neutral with dissolve 
     
    mt "What was your favorite part of the day %(povFirstName)s?"
     
    y "Hmmm, I'd have to say when we..." 
     
    d "*growl*" 
     
    d "We both go silent and look towards my stomach." 
     
    y "Hehe, guess my stomach wants to join the conversation." 
     
    mt "Don't worry, I happen to speak stomach fluently." 
     
    y "Really?" 
     
    mt "Of course." 
     
    d "Makoto leans his head near my stomach and pretends to be listening to it intently." 
     
    mt "Uh huh, of course." 
     
    mt "As I thought, your stomach is in desperate need of some food." 
     
    mt "We have to stop somewhere." 
     
    y "It's that serious?" 
     
    mt "Absolutely." 
     
    y "Ok, let me just clear it with Gou." 
     
    d "Some alone time with Makoto, this day just keeps getting better and better!" 
     
    d "I grab my cell and call Gou." 
     
    gm "Hey %(povFirstName)s, what's up?" 
     
    y "Not much, Makoto just asked me to go get something to eat. Is that ok?" 
     
    gm "Oh my god, it's you're first date! AHHHHH!" 
     
    d "Gou's excited squealing pierces my eardrum." 
     
    y "Gou, Gou, I'm gonna take the screaming as a yes. Ok?" 
     
    gm "AHHH, tell me everything when you get back." 
    
    y "Ok, I promise. I gotta hang up though, your screaming is giving me tinnitus." 
    
    d "I hang up my phone." 
    
    y "She said it's cool, let's go." 
    
    mt "Cool, I think there's a really good Korean barbeque place nearby." 
    
    scene bg Restaurant with dissolve
    
    d "It takes a while to find the place, but the smell coming from it makes me think it will be worth it." 
    
    show Makoto Neutral at center with dissolve
    
    mt "I think I see a table over there." 
    
    d "We take our seats and a waiter stops by not long after." 
    
    w "Here are your menus, any drinks to start with?"
    
    mt "Waters fine." 
    
    y "Water for me too, please." 
    
    d "The waiter heads off to get our drinks while we peruse the menu." 
    
    mt "Get anything you want, the meals on me." 
    
    y "Wow, how gentlemanly. You may want to rethink that though." 
    
    mt "Why?"
    
    y "Because I'm eyeing the number twelve." 
    
    show Makoto Worried with dissolve
    
    mt "The number twelve?"
    
    mt "But that's a group platter for up to four people!" 
    
    y "Only four?"
    
    y "I thought it said six, maybe I should go with number 14." 
    
    show Makoto Neutral with dissolve
    
    mt "Heh, I never would have thought you'd order something like that." 
    
    y "What can I say, I love to cook and I love to eat." 
    
    d "The waiter comes back by and takes our orders." 
    
    mt "I'm glad we're doing something together like this. Learning more about you has become my new favorite past-time." 
    
    y "Really?"
    
    mt "Yea, it's always interesting. Who knew you'd like to eat like it's going out of style." 
    
    y "If you like that, just wait until you learn about my killer karaoke skills." 
    
    mt "Haha!" 
    
    d "For a little while, we ogle other people's food and make small talk." 
    
    mt "So the whole team was shopping for swimsuits, when suddenly, Haru sees an aquarium and starts to strip down, in the middle of the store!"
    
    y "Haha!" 
    
    mt "It didn't even have water in it!" 
    
    y "Haha!" 
    
    mt "Haha!" 
    
    mt "That's enough of my stories, I want to hear more about you." 
    
    y "Alright, what do you wanna know?"
    
    mt "Hmmmm..." 
    
    mt "Favorite color?"
    
    y "Yellow." 
    
    mt "Cheerful, I like it. Cookies or cake?"
    
    y "Cake, obviously." 
    
    mt "Heh, any friends back home you miss?"
    
    d "I freeze up at the question. Makoto seems to notice." 
    
    show Makoto Sad with dissolve
    
    y "I..." 
    
    d "Suddenly, the waiter apears." 
    
    w "Here's your food!" 
    
    d "They begin setting our plates down." 
    
    y "Oh, the food!" 
    
    d "Thank goodness." 
    
    mt "Yea, looks good." 
    
    d "We eat in silence for a while." 
    
    d "Makoto seems to know that his question upset me." 
    
    mt "Hey %(povFirstName)s, I'm sorry if I made you uncomfortable." 
    
    y "No, it's fine. You didn't know." 
    
    mt "No, I shouldn't pry so much." 
    
    mt "I've been told my friendliness can get to the point where it seems, pushy." 
    
    y "I thought that at first, but now I really appreciate it. If you hadn't pushed me to talk the first day I got here, I don't think I would have had the courage to join the swim team." 
    
    mt "Oh, I don't know about that." 
    
    y "No it's true!" 
    
    y "You're really great at encouraging people. It's something I love about you." 
    
    show Makoto Bashful with dissolve
    
    d "Makoto blushes at the word love." 
    
    mt "Oh, ugh, thanks!" 
    
    d "Makoto's embarrassment spreads to me." 
    
    d "We spend the rest of the meal looking at our plates, only glancing up to comment on the food." 
    
    d "After Makoto takes care of the check, we start back home." 
    
    scene bg Neighborhood A_3 with dissolve
    
    d "The sun has gone down at this point, so the temperature has dropped considerably." 
    
    d "I try to warm my hands by breathing in to them and rubbing them together." 
    
    d "Makoto looks over and notices me shivering." 
    
    d "Shyly, he slips his hand into mine." 
    
    show Makoto Bashful at center with dissolve
    
    mt "I hate to seem cliché, but I've heard sharing body heat is the best thing to do in a situation like this." 
    
    d "I look up at him and smile, gently lacing my fingers with his." 
    
    d "We spend the rest of the trip home quietly enjoying our newfound closeness." 
    
    scene bg M Residence 2 with dissolve
    
    d "We reach Gou's place faster than I would have hoped."
    
    y "Guess we're here." 
    
    show Makoto Sad at center with dissolve
    
    mt "Guess so." 
    
    d "I move to go inside but find myself unable to." 
    
    d "Makoto has not released my hand." 
    
    y "Ugh, Makoto?"
    
    d "Makoto looks down and quickly releases my hand." 
    
    mt "Woops, sorry." 
    
    show Makoto Bashful with dissolve
    
    d "Makoto becomes flustered and looks down at his feet as I walk to the front door." 
    
    d "As I'm about to enter, I hear Makoto call out to me." 
    
    y "%(povFirstName)s!" 
    
    d "I turn around curious as to what he has to say." 
    
    y "Yes?" 
    
    mt "I just..."
    
    d "Makoto rubs the back of his head and, once again, becomes fascinated by the floor." 
    
    mt "I had a really nice time tonight." 
    
    y "Me too." 
    
    mt "Really?!"
    
    d "Makoto looks up in surprise, and then immediately bows his head." 
    
    mt "Does this mean you'd like to do this again sometime?"
    
    y "Absolutely." 
    
    d "Makoto raises his head again and shoots me his signature, blinding, smile." 
    
    mt "I hoped you'd say that." 
    
    hide Makoto with dissolve
    
    scene bg Hallway Entrance 3 with dissolve
    
    d "I wave goodbye to Makoto and enter the house." 
    
    d "Before I can even begin to process all that has happened today, Gou peeks in from another room." 
    
    show Gou Neutral at center with dissolve
    
    gm "Sooo, how'd it go?"
    
    y "Come on, I'll tell you all the juicy details." 
    
    d "Gou squeals happily and leads me to her room." 
    
    gm "Tell me everything!" 
    
    y "Honestly, not much." 
    
    show Gou Worried 1 with dissolve 
    
    gm "What, no way!" 
    
    y "It's true!" 
    
    y "The three of us went in to the city for a while, to do some sightseeing, and then Makoto and I went to get something to eat after we dropped Haru off." 
    
    gm "What? No love confessions? No tentative first kiss?"
    
    y "We held hands for a while."
    
    show Gou Neutral with dissolve
    
    gm "Humph, I guess that's soemthing." 
    
    y "There was one odd thing that happened." 
    
    gm "Really?"
    
    y "Yea, these three girls showed up and started flirting with Haru and Makoto." 
    
    gm "Not surprising, have you seen their muscles?"
    
    y "The flirting wasn't that weird, it was the fact that they were oddly familiar." 
    
    gm "How could that be? You don't know anyone here besides us." 
    
    y "I think they may have been foreign." 
    
    show Gou Worried 1 with dissolve
    
    gm "Weird, maybe they were on your plane or something." 
    
    y "I guess..." 
    
    gm "I wouldn't worry about it. Come on, let's go to bed." 
    
    d "Gou and I head to our rooms to try and get some sleep." 
    
    scene bg Neighborhood A_1 with dissolve
    
    d "Another day, another opportunity to be escorted to school by two goregeous men." 
    
    d "Life is good." 
    
    show Haru Neutral at right with dissolve
    
    show Makoto Neutral at left with dissolve
    
    hn "What are you smiling about?"
    
    y "Oh, nothing." 
    
    d "Hehe!" 
    
    mt "Are you ready for the quiz today %(povFirstName)s?"
    
    y "I think so, my Japanese is really improving." 
    
    scene bg Classroom A_01 with dissolve
    
    d "The three of us say our goodbyes as we take our seats." 
    
    d "It's just a normal day, which is odd for this school, aced my quiz, learned some math." 
    
    d "Just as I'm about to fall asleep, during a particularly boring lecture on Japanese literature, the lunch bell rings." 
    
    d "I don't see any of the gang, so I decide to go to the roof myself." 
    
    scene bg Stair Well A_01
    with dissolve
    
    with Pause(1)
    
    scene bg Stair Well B_01
    with dissolve
    
    with Pause (1)
    
    scene bg Roof Top Door_01
    with dissolve
    
    with Pause (1)
    
    scene bg School Rooftop 
    with dissolve
    
    d "From my spot just behind the door I can hear flirtatious giggling, and hushed voices." 
    
    d "Ooo, I wonder who brought their girlfriends to lunch!" 
    
    d "I peek around to see an unfamiliar girl leaning towards...." 
    
    d "Makoto?"
    
    d "I can't quite make out what they're saying, but the girl sure does think it's funny." 
    
    d "I feel my stomach clench." 
    
    d "He was petrified of that flirty girl yesterday, now he's acting like a regular Casanova!" 
    
    d "I take a deep breath, I shoudln't rush to any conclusions, I'm just going to go in and say hi." 
    
    y "Hey Makoto, stealing another young maiden's heart I see." 
    
    d "They both jump in surprise." 
    
    show Makoto Worried at center with dissolve 
    
    mt "%(povFirstName)s!" 
    
    mt "What are you doing here?"  
    
    y "I eat lunch here, the whole team does." 
    
    d "I give them both a long look." 
    
    y "Although, you seem to be doing something else up here." 
    
    d "The girl gives me a dirty look for that comment, but I elect to ignore it." 
    
    mt "What no!" 
    
    mt "It's nothing like that!" 
    
    y "It's fine, you don't have to explain yourself to me." 
    
    y "After all, I'm just a team mate." 
    
    d "With that cutting response I decide to make my exit." 
    
    mt "Wait %(povFirstName)s!" 
    
    d "For the first time, I don't look back when he calls me." 
    
    
       
    return 
   
###Rin's Route
label Rin_Romance_Route:
    #Chapter 1
    
    d "I knew it. I shoot Gou a deathly glare in response." 
    
    y "Whatever you say, sis-in-law." 
    
    hide Gou with dissolve
    
    d "Gou chuckles, then she spins around and leaves the kitchen." 
    
    d "I hear her calling for Rin while I switch on the stove, put the big pot on it and let some oil drip on the ground." 
    
    y "Let's see...First, cutting the onions." 
    
    rm "I can do that." 
    
    d "In the next moment, Rin stands right beside me." 
    
    show Rin Smile at center with dissolve 
    
    d "Whoa, where did he even come from that fast?!" 
    
    d "He shifts his head to me and grins." 
    
    rm "I like meat and spicy food overall, so let's make a delicious dinner together!" 
    
    d "Flooded with motivation, Rin rolls up his sleeves and takes an onion into his hand." 
    
    show Rin Neutral with dissolve
    
    d "For the break of a second, I swear I can see hesitation flashing over his expression as if he's unsure of something." 
    
    d "Then, he puts the onion down again and grabs for a knife." 
    
    rm "So, then I'll cut the onion." 
    
    d "He pins the vegetable down on the chopping board and is about to cut it in half with the knife." 
    
    d "He has no idea how to cut onions, does he?" 
    
    d "I chuckle lightly, but cannot hide the sounds coming out, and Rin notices." 
    
    d "He casts his sight down and only murmurs." 
    
    show Rin Upset with dissolve
    
    rm "I haven't cooked much until now, you know..."
    
    d "His voice is quieter and also lesss enthusiastic as before. His hair sways lightly while speaking."
    
    d "Is he being embarassed about it?"
    
    y "I'm sorry, I didn't want to make fun of you. It's totally fine, I'm going to show you." 
    
    d "While I take the onion and peel off the skin's layers one by one, I steal a secretive glare from Rin from the corner of my eyes." 
    
    d "His cheeks are faintly flushed, but he is watching my instructions intently." 
    
    d "I've made him feel uncomfortable." 
    
    y "Have you ever eaten chili con carne before, Rin-san?" 
    
    d "I try to change the subject." 
    
    show Rin Neutral with dissolve
    
    rm "One time only in Australia, as far as I can remember. Though, I've forgotten the taste of it already." 
    
    show Rin Smile with dissolve
    
    rm "That's why I'm especially looking forward to this dish." 
    
    y "Then let's make this the best chili con carne you've ever eaten so that you'll never forget the taste of it again!" 
    
    d "He stares at me with furrowed brows." 
    
    d "Oops, that was too much, right? I truly am a dork." 
    
    d "But Rin starts laughing light-heartedly." 
    
    rm "Sure, let's do it! I think I get it now with the onions." 
    
    d "Rin peels the skin off the other onion while I reach for the peppers and start washing then chopping them." 
    
    rm "So...What's America like? I don't imagine it to be much different from Australia, though there are surely many different places for a country this big." 
    
    rm "Is the weather nice where you're from? How about the landscape?" 
    
    y "The weather? Average. I'd say. Just like the weather here in Japan. Cold in the winter and warm in the summer." 
    
    y "But the landscape...well, where I'm from, I cannot watch the sea like here at Iwatobi. So I hope I'll get to go to the sea very often for my stay." 
    
    rm "Sounds like you like the sea very much." 
    
    y "I do. It makes me feel at ease and calm when I go there. It also gives Iwatobi quite a peaceful atmosphere. Which I like very much." 
    
    rm "Yeah, Iwatobi is quite a small and peaceful town. How was your life in your hometown? Was it such a huge contrast to here?"
    
    d "Instinctively, whenever someone asks me a question referring to my hometown, I freeze in motion." 
    
    d "But after all this time, I have come to learn quite well how to dodge an answer too." 
    
    y "Yes, it was quite lively over there since it's a huge city." 
    
    rm "Ah, I can imagine after having lived in such a huge city myself. Being new here now, do you miss your friends and family?"
    
    y "Yeah." 
    
    d "The reply I've given lacks emotion, and I can literally feel the air getting heavy between us." 
    
    d "I somehow can sense that he knows my answer is only half-hearted, but he luckily doesn't push the topic and stays silent." 
    
    d "Still, to avoid having him digging deeper into that matter, I get myself busy with gathering together the vegetables we've sliced up and throwing them into the pot while I quickly find an ask to turn the attention away from me." 
    
    y "So you've spent some time in Australia yourself? How was it there? Maybe you can give me any tips?" 
    
    d "I try to smile and luckily, I don't have much difficulty in doing so when I meet Rin's own smile that he's shooting at me." 
    
    d "He picks up the topic right away, and I can't be more grateful for that, regardless whether it is intentional or not." 
    
    rm "When I first came to Australia, looking at the ocean relaxed me somehow." 
    
    rm "I was pretty anxious when I left Japan, even though I had talked big before. A country I didn't know....a language I did not speak..."
    
    rm "But when I came to the ocean, I immediately felt calmer. So for this part, we have something in common, %(povLastName)s-Chan."
    
    d "I watch Rin attentively as he speaks, his gaze focused, but somehow still dreamy while reminiscing about his past." 
    
    d "I, too, think that at some level, we understand each other, because we have similar experiences despite only knowing each other for barely an hour." 
    
    rm "I had a home stay with amazing parents and a puppy named Winnie who's a big dog now." 
    
    rm "I went to school during the day and to train under a coach afterwards. There were amazing swimmers from around the world there." 
    
    rm "And I learned that, even if I was pretty fast in Japan, it didn't need to mean anything at all." 
    
    d "Although I expect him to continue as it seems he has gotten carried away, Rin stops talking, and even after waiting for a few seconds, he doesn't continue." 
    
    d "Maybe I'm not the only one who needs to carry around a huge package after all." 
    
    d "Having been in the same situation shortly before, I do what he has done and don't push." 
    
    y "Australia sounds amazing. I wouldn't mind visiting there one day when I get teh chance to." 
    
    d "Even though he doesn't let it slip, I still notice how relieved he is about my casual reply that doesn't connect to the last part of his story." 
    
    rm "You definitely should! I will also take you to a sightseeing-trip then." 
    
    d "Wait, did we just make a promise?!"
    
    d "Still I nod willingly, unable to refuse as he looks at me with this gentle gaze." 
    
    d "It doesn't sound bad at all, now that I think of it. It could be pretty fun going there together with everybody..." 
    
    show Gou Neutral at left with dissolve
    
    show Rin Neutral at right with moveoutright
    
    gm "Hey you two, stop billing and cooing, and get dinner ready!" 
    
    d "Where did she come from?" 
    
    rm "It wouldn't take us so long if you'd stop sneaking around and help us!" 
    
    d "Gou snickers with a meaningful gaze." 
    
    gm "No way! I'd only interrupt what's going on here, so I'll be gone again!" 
    
    rm "You...!" 
    
    hide Gou with dissolve
    
    d "Rin grabs for a towel and throws it after his sister, but before it can hit her, she has already closed the door." 
    
    show Rin Upset at center with dissolve 
    
    rm "Please, don't listen to all the stuff she says, she's just-" 
    
    d "But he doesn't come to finish his sentence, because I can't suppress a laugh anymore." 
    
    d "I've almost forgotten how it's like to be around people my age and actually have fun with them..." 
    
    show Rin Smile with dissolve
    
    rm "There it is. You smiled again. I'm glad." 
    
    d "So he did notice before... Has he been trying to cheer me up all this time?"
    
    d "Not knowing how to respond, I hope to remain that smile on my lips for a little while longer so that his effort won't all go to waste." 
    
    rm "So, what's the next step? The ground meat?"
    
    d "Thank you, Rin..." 
    
    y "Yeah. Take the wooden spoon and fry the vegetables. I'll prepare the ground meat." 
    
    d "He nods and we finish making dinner together." 
    
    scene bg Dining Table 2 with dissolve
    
    d "After having set up the table, everybody takes a seat. Rin seats himself beside me, as Gou and Sousuke sit opposite of us." 
    
    d "They both eye the dish on their plates rather suspiciously, obviously wondering whether it would taste good at all." 
    
    show Gou Worried 1 with dissolve
    
    gm "Looks... Interesting." 
    
    d "Gou still tries to sound optimistic." 
    
    d "Sousuke doesn't even say a word, but his face speaks more than he is probably able to express verbally right now." 
    
    d "I feel my heart sinking a bit. Of course, it's a western dish and must look rather unfamiliar to them, and the mix of meat and vegetables with that sauce is also not what they're used to taste in Japan." 
    
    d "Although, I still wish they'd give it a try." 
    
    show Gou at right with moveoutright
    
    show Rin Neutral at left with dissolve
    
    rm "Hey, stop complaining. I even tried your poor attempt of stew which looked way more unsavory than this!" 
    
    gm "But it tasted okay! You can't say anything against it!" 
    
    rm "See? Then how about tasting this first before judging?"
    
    hide Gou with dissolve
    
    hide Rin with dissolve
    
    d "Rin silences Gou with that single sentence." 
    
    d "He really has a way with people, doesn't he?"
    
    d "More enthusiastic, and also less prejudiced, Gou and Sousuke take a spoonful of chili and lead it to their mouths." 
    
    d "Rin and I follow suit. Immediately upon tasting the dish, the spicy and aromatic flavor spreads inside my mouth." 
    
    d "It's delicious! But will the others share the same opinion?"
    
    show Rin Smile at center with dissolve
    
    rm "Woh..." 
    
    d "When I glance at Rin, he has immediately taken another spoonful, chewing happily while the others watch him in surprise." 
    
    hide Rin with dissolve 
    
    d "Then it's Sousuke who also speaks out." 
    
    show Sosuke Smile at center with dissolve
    
    sy "I've never tasted anything like this before. It's unfamiliar, but I can't deny that the flavor is delicious." 
    
    sy "It's spicy as well, but I can taste that you used other varieties of spices of what we're usually seasoning with here." 
    
    hide Sosuke with dissolve
    
    y "Yes, it's a Mexican dish." 
    
    show Gou Neutral at center with dissolve
    
    gm "Wow, %(povFirstName)s-san, this tastes amazing!" 
    
    d "Gou suddenly blurts out and takes another spoon with chili." 
    
    gm "I'm sorry for having been so prejudiced and judging too fast just by the look." 
    
    gm "I think I can say now that this is my favorite foreign dish ever!" 
    
    show Gou at left with moveoutleft
    
    show Rin Smile at right with dissolve
    
    rm "No need to be so humble, Gou!" 
    
    gm "No, I truly mean it! You two did a great job!" 
    
    d "She winks at me and I sink my head in slight embarrassment." 
    
    y "I'm glad you like it as well. Thank you." 
    
    d "I let out an almost inaudible sigh of relief and start eating myself now that I'm more at ease." 
    
    d "Everybody finishes his plate until nothing is left in the pot anymore, and I feel very happy about it since I've eaten much myself." 
    
    gm "I'd like you to cook more for us %(povFirstName)s-san! I want to taste all the foreign dishes you know!" 
    
    rm "She did not come here to be our cook!" 
    
    gm "But if you help her all the time, you'll learn how to cook yourself as well, and we don't need to rely on %(povFirstName)s anymore." 
    
    rm "In your dreams!" 
    
    d "I snicker slightly, clearly enjoying their banter. If this is what's going on in the Matsouka-household each day, I'm sure I'll be having a good time staying here." 
    
    rm "Since %(povFirstName)s-chan and I were cooking, how about you and Sousuke do the dishes?" 
    
    d "Gou opens her mouth to protest, but then realizes she can't actually say anything against this suggestion since it's only fair for either party, so she stands up and starts collecting the plates with the help of Sousuke." 
    
    hide Gou with dissolve 
    
    show Rin Smile with dissolve 
    
    rm "Hey, Sousuke..." 
    
    show Sosuke Neutral 1 at left with dissolve
    
    sy "Hm?" 
    
    d "Rin leans back in his seat and crosses his arms behind his head, shifting his sight aside so that I cannot see his expression anymore as he asks his friend."
    
    rm "Want to spend the night here instead of going all the way back to the dorms?" 
    
    sy "Why?" 
    
    rm "I thought...because it's kind of late already, we ate too much delicious food, and %(povFirstName)s-chan might need some company since she's still new here." 
    
    rm "Who knows what weird things my little sis would try on her when they're left alone." 
    
    gm "I heard that!" 
    
    y "Actually..." 
    
    d "I want to say it's okay if we're left alone, and that he doesn't need to worry about me, but before I can finish, Sousuke already answers cooly himself." 
    
    sy "Fine with me." 
    
    hide Sosuke with dissolve
    
    show Rin at center with moveoutleft
    
    y "Uhm...guys, I really don't want to be a bother. I feel really grateful, but I don't want you to worry about me too much and get into your way." 
    
    rm "You're not getting in anybody's way." 
    
    d "He turns around and smiles at me." 
    
    rm "It's going to be really fun, we can all play 'Destiny's Ultimate Challenge' together!" 
    
    hide Rin with dissolve
    
    d "Now that he talks so causally about it, I can't deny his offer. Besides...playing together, having something like a sleepover..." 
    
    d "I haven't experienced this kind of gathering in a long time. Actually, I doubted I'd ever want to experience this again." 
    
    d "But this...these people...I feel happy when I'm with them. Can I give this another chance?" 
    
    y "Then...Yes! Let's do it!" 
    
    d "From the kitchen, I can hear Gou grumble again, or was it only my imagination?"
    
    scene bg MC Bedroom 4 with dissolve
    
    d "*Grumble, Grumble*" 
    
    d "I twist and turn around in bed, unable to sleep." 
    
    d "Playing 'Desinty's Ultimate Challenge' together with everybody this evening was great." 
    
    d "Not even once have I felt left out despite being the foreign host sister." 
    
    d "Maybe at Iwatobi, I can really start anew." 
    
    d "I push the blanket aside and stand up. I can't sleep with my stomach rumbling around like this." 
    
    d "And now, it even starts hurting." 
    
    d "Ugh, I ate way too much again, didn't I...But I cannot say no to delicious food..." 
    
    scene bg Kitchen with dissolve
    
    d "Making my way to the kitchen with my phone in one hand, I leave my room. In the kitchen, I open the refrigerator and get out a bottle of water." 
    
    d "I fill the liquid into a glass and take a sip." 
    
    d "Immeditately, I feel slightly better, but the stomachache may still take a while to vanish." 
    
    d "And since I cannot sleep like this, I decide to stay here and glance out the window." 
    
    d "The moon shines beautifully here at Iwatobi, and I can feel a somehow satisfying feeling wash over me as I close my eyes." 
    
    d "A moment later, my phone beeps and shows one new message as I pick it up." 
    
    d "A message so late? Is it from home?"
    
    d "'It's Rin. I wanted to thank you again for the chili, it truly tasted delicious.'" 
    
    d "Huh? Where is that coming from in the middle of the night?"
    
    d "But the message continues." 
    
    d "'Turn around.'" 
    
    y "What?" 
    
    unknown "Turn around." 
    
    d "This time, it's a real person speaking behind me, and I almost let out a shriek in shock if I hadn't known the voice as I instinctively spin around." 
    
    y "Rin! You scared me!" 
    
    show Rin Neutral at center with dissolve
    
    rm "Sorry, sorry! I heard you coming out of your room. Why are you up so late? Or should I say so early?"
    
    y "I have a stomachache, because I ate too much, and thus I cannot sleep." 
    
    d "Rin is lost for words for a moment as he stares at me with furrowed brows." 
    
    d "I sound like a baby, don't I? How embarrassing...He must think I'm weird." 
    
    show Rin Smile with dissolve
    
    d "Then, he bursts out laughing." 
    
    rm "A..hahahahahaha...hahahaha! Do you always eat that much?" 
    
    y "Well...it's what rids of my emotional tensions built up in my life." 
    
    rm "You really are a weird one, aren't you?" 
    
    d "I knew it!" 
    
    d "But the sparkles in his eyes reflecting the moonlight give his mien something so gentle that doesn't match his words, and I can tell he means it in a kind way." 
    
    y "Maybe I am." 
    
    d "I turn around and point out of the window." 
    
    y "Look, Rin-san. No matter where you are on earth, in Japan, America or Australia...you always look at the same moon. It's fascinating somehow, isn't it?"
    
    rm "You're a really interesting girl coming up with such kind of thoughts, %(povFirstName)s-chan." 
    
    y "Huh? What did you say?"
    
    d "IHe has spoken so quietly, I didn't hear each word." 
    
    rm "I said same with the ocean." 
    
    d "Within a second, he stands beside me and watches the moon as well." 
    
    rm "The ocean connects all continents. So wherever you are in the world, it connects you to your beloved ones." 
    
    rm "When I was in Australia and missed my friends, I felt like the ocean connected me to them. Because I knew they were on the other side." 
    
    y "You're right. I haven't thought about that before." 
    
    d "Saying such deep things, what have you been through so far?" 
    
    d "But experiencing this myself, I don't ask. I've always believed people would open themselves if they felt the right time has come, if they trust the person whole-heartedly." 
    
    d "Maybe our time will come as well..." 
    
    rm "How long are you gonna stay here?" 
    
    y "For until my third year. So half a year." 
    
    rm "Mmmmhm. You think you can catch up on me until then?"
    
    y "Huh? What do you mean?"
    
    rm "Gou causally dropped that you've joined the Iwatobi Swim Club." 
    
    d "This girl...!" 
    
    y "Well...I was more forced to join than willingly accepting. But...I don't mind, actually. Truth be told, I missed the thrill of swimming competitively and would like to do it again." 
    
    y "It's been quite some time since I last swam in a race, so I hope the team doesn't expect too much of me. I don't want to disappoint them in the end." 
    
    y "But I'm positive I can learn much while I'm here!" 
    
    d "Rin smiles brightly upon this proclamation as if he has sensed another challenge." 
    
    rm "Then do you best. Because I'd like to race you one day." 
    
    y "What-?? Me against you, one of the best swimmers in Samezuka, who even went to Australia to train?!"
    
    y "This is a joke right? I have no chance against you!" 
    
    rm "You're going to train with one of the best teams in Japan. If anything, I need to train even harder!" 
    
    d "In this moment, I cannot say wehther he is being polite or truly means it, but there is something in his tone that makes me believe him regardless." 
    
    y "Then...challenge accepted! I will give my best to beat you! But don't go easy on me just because I'm a girl!" 
    
    d "Rin's eyes flicker and he lowers his gaze as he smirks." 
    
    rm "I never go easy on anyone." 
    
    y "Then it's set." 
    
    rm "It is." 
    
    d "We laugh quietly together before my yawn shows me that it's time to finally go back to bed." 
    
    y "It's really bedtime for me now." 
    
    rm "How about your stomachache?"
    
    d "Oh, I've totally forgotten about it in the first place!" 
    
    y "it's gone...thank god, now I can sleep in peace." 
    
    rm "I'm glad." 
    
    y "Then...Goodnight, Rin-san." 
    
    d "I pick up my phone and am about to head towards the bedroom, when I feel a warm touch on my arm and then soft fingers wrapping around my wrist." 
    
    show Rin Upset with dissolve
    
    rm "Wait." 
    
    y "Hm? What is it?"
    
    d "In the semi-darkness, I cannot read his expression, because he has his head shifted aside, and the moonlight is only illuminating his maroon-colored hair." 
    
    d "He seems to struggle with something as he doesn't answer directly, but before I can even speak to him again, he finally questions me." 
    
    rm "Could we...chat more? I mean...is it okay for me to text or call you?"
    
    y "Uh...sure, why not? If you have any questions, just-" 
    
    d "He vehemently shakes his head." 
    
    rm "No, not like this. I mean...without an important reason. Can I...text or call you just casually? Wihtout an important reason?"
    
    rm "Just to...talk?"
    
    d "I'm a bit taken aback by this request." 
    
    d "Who even asks it like this? Isn't it normal to just casually start talking if you feel like it?" 
    
    d "But somehow, it's kind of funny as well. He seems slightly helpless." 
    
    d "It's kinda cute." 
    
    y "Sure!" 
    
    show Rin Smile with dissolve
    
    rm "Okay! Goodnight, %(povFirstName)s-chan!" 
    
    d "He heads off to bed even before me in the speed of light." 
    
    d "I smile to myself and head to my room right after." 
    
    return 
    
            
                
                
         
         
         
         
             
             
         
         
         
        
        
        
        
        
        
      
        
        
        
        
