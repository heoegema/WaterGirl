#BACKGROUNDS
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
image bg Swimming Pool A_1 = "Swimming Pool A (1).jpg"
image bg Swimming Pool A_2 = "Swimming Pool A (2).jpg"
image bg White = "WHITE.jpg"

#Background Effects
init: 
    
    $ flash =Fade(.25, 1.00, .75, color="fff")
#MISC.
image LOGO = "OFFICIAL LOGO.png"

#CG'S

#SPRITES
#Haruka
image Haru Neutral = "Haruka Nanase_Expression_01.png"
image Haru Happy = "Haruka Nanase_Expression_02.png"
image Haru Annoyed = "Haruka Nanase_Expression_03.png"
image Haru Worried = "Haruka Nanase_Expression_04.png"
image Haru Cry 1 = "Haruka Nanase_Expression_05.png"
image Haru Cry 2 = "Haruka Nanase_Expression_06.png"
image Haru Cry 3 = "Haruka Nanase_Expression_07.png"
image Haru Sad = "Haruka Nanase_Expression_08.png"
image Haru Bashful = "Haruka Nanase_Expression_09.png"
#Makoto
image Makoto Devious = "Makoto Tachibana_Expression_01.png"
image Makoto Mad = "Makoto Tachibana_Expression_02.png"
image Makoto Worried = "Makoto Tachibana_Expression_03.png"
image Makoto Neutral = "Makoto Tachibana_Expression_04.png"
image Makoto Sad = "Makoto Tachibana_Expression_05.png"
image Makoto Bashful = "Makoto Tachibana_Expression_06.png"
#Nagisa
image Nagisa Pouty = "Nagisa Hazuki_Expression_01.png"
image Nagisa Sarcastic = "Nagisa Hazuki_Expression_02.png"
image Nagisa Upset 1 = "Nagisa Hazuki_Expression_03.png"
image Nagisa Upset 2 = "Nagisa Hazuki_Expression_04.png"
image Nagisa Determined 1 = "Nagisa Hazuki_Expression_05.png"
image Nagisa Determined 2 = "Nagisa Hazuki_Expression_06.png"
image Nagisa Mad = "Nagisa Hazuki_Expression_07.png"
image Nagisa Bashful 1 = "Nagisa Hazuki_Expression_08.png"
image Nagisa Unamused 1 = "Nagisa Hazuki_Expression_09.png"
image Nagisa Unamused 2 = "Nagisa Hazuki_Expression_10.png"
#Rei
image Rei Neutral = "Rei Ryugazaki_Expression_01.png" 
image Rei Annoyed = "Rei Ryugazaki_Expression_02.png" 
image Rei Reassuring = "Rei Ryugazaki_Expression_03.png" 
image Rei Bashful = "Rei Ryugazaki_Expression_04.png" 
image Rei Upset = "Rei Ryugazaki_Expression_05.png" 
image Rei Sad = "Rei Ryugazaki_Expression_06.png" 
image Rei Mad = "Rei Ryugazaki_Expression_07.png" 
image Rei Mad 2= "Rei Ryugazaki_Expression_08.png" 
image Rei Cry = "Rei Ryugazaki_Expression_09.png" 
image Rei Cry 2 = "Rei Ryugazaki_Expression_10.png" 


#Gou
image Gou Neutral = "Gou Matsuoka_Expression_01.png"
image Gou Worried 1 = "Gou Matsuoka_Expression_02.png"
image Gou Worried 2 = "Gou Matsuoka_Expression_03.png"
image Gou Mad  = "Gou Matsuoka_Expression_04.png"
image Gou Determined = "Gou Matsuoka_Expression_05.png"
#Miho
image Miho Neutral = "Miho Amakata_Expression_01.png"
image Miho Reassuring = "Miho Amakata_Expression_02.png"
image Miho Mad = "Miho Amakata_Expression_03.png"
image Miho Determined = "Miho Amakata_Expression_04.png"
image Miho Sad = "Miho Amakata_Expression_05.png"

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

#MAIN CHARACTERS
define y = Character('[povFirstName]', show_two_window=True, font="CaviarDreams.ttf")
define hn = Character('Haruka', show_two_window=True, font="CaviarDreams.ttf")
define nh = Character('Nagisa', show_two_window=True, font="CaviarDreams.ttf")
define gm = Character('Gou', show_two_window=True, font="CaviarDreams.ttf", color="#000000")
define mt = Character('Makoto', show_two_window=True, font="CaviarDreams.ttf")
define ma = Character('Miho Amakata', show_two_window=True, font="CaviarDreams.ttf")
define rr = Character('Rei', show_two_window=True, font = "CaviarDreams.ttf")
define rm = Character('Rin', show_two_window=True, font="CaviarDreams.ttf") 
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
    scene bg White 
    with Pause(1)
    
    #play sound "ping.ogg"

    show LOGO with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)

    return
    

label start:
    
    stop music
    
    scene bg White
    
    $ povFirstName = renpy.input("What is your first name?\n\n", length=15) or "Sarah"
    $ povLastName = renpy.input("What is your last name?\n\n", length=30) or "Henderson"
    $ povName = povFirstName +" "+povLastName
    
    #play nature
    
    play music "Friendship.wav"
     
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
    
    ma "I’m about to start class, if you wouldn’t mind, could you sit at the chair 
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
    
    d "I’m in the back, so no one can easily stare at me. And I get to look out the window."
    
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
    
    play music "Lazy Days.mp3"
    with dissolve
    
    d "Hey, there’s the stairs to the roof. And the door up above is open."
    
    d "Convenient! Something’s going right for once."
    
    d "Stepping outside the crisp autumn air refreshes me from the trials of the morning."
    
    scene bg School Rooftop
    with dissolve
    
    with Pause (1)
    
    d "I break open my slightly squished melon bread and take a bite, enjoying the silence of the 
    empty rooftop and the view of the cherry trees neaby."
    
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
    
    d "It's nice to finally be on the way back to my host's home again." 
    
    d "After the long, crazy day I've had, I want nothing more than to just flop on my bed and get a good nap." 
    
    d "Maybe wake up and take a soak in the bathtub as well." 
    
    d "I just can't wait to do that. My body is practically begging my mind to obey." 
    
    d "But it looks like I'll have other plans..." 
    
    mt "And after all that I still get to walk you home!" 
    
    
    hn "..." 
    
    d "Thinking back I probably should ahve figured out this would be the end result of the day." 
    
    d "Not that it was my intention or anything." 
    
    d "But when Gou gets an idea in her head, it appears it's hard to go against her." 
    
    scene bg white 
    
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
    
    d "Wait a minute, when did he pop his head up from his calculus book." 
    
    show Rei Reassuring with dissolve
    
    rr "I actually ran track my first year here, and I'd never swam before. It took a while before I could even compete for last place." 
    
    y "So you gave up track to do something you'd never done before?" 
    
    show Rei Bashful with dissolve
    
    rr "What can I say? There's a certain beauty to swimming missing from running." 
    
    rr "Especailly when the competitor has the potential for world-class talent." 
    
    d "He appears to be glancing at Haru as he says this." 
    
    y "I'm just not sure I'm ready to do this." 
    
    show Nagisa Pouty at right with dissolve
    show Rei Bashful at left with moveoutleft 
    
    nh "Why not! YOu're here. You know how to swim. You have people who want you around!" 
    
    nh "So like, carne diet or whatever it is Americans say!" 
    
    y "I think you just told me to become a carnivore in really bad Tex-Mex." 
    
    nh "You know what I Mean. Dive in-literally!" 
    
    y "But I didn't even pack a swimsuit, I mean, I brought my tennis racket on the off-chance of joining the tennis club...but I left my swimsuit at home." 
    
    hide Nagisa with dissolve
    hide Rei with dissolve
    show Gou Determined at center with dissolve
    
    gm "But that's not a problem!" 
    
    gm "We can get you a swimsuit, the only guidelines are it has our school symbol on it, it has to be a one piece and the main colour be black like the rest of the team..." 
    
    gm "But you can have whatever color trim you want." 
    
    y "But..." 
    
    show Gou Worried 1 with dissolve
    
    gm "Please, I'll feel like a bad hostless if I let you become a member of the Just Go Home Club." 
    
    y "I s there really a club for that?"
    
    y "I always thought it was a joke, But if there's a club for that point me towards it." 
    
    d "I thought my joke was kind of funny, but the reaction I got was not from whom I expected." 
    
    hide Gou 
    
    show Haru Annoyed at center with dissolve   
    hn "Coward." 
    
    y "Wait...what did you just say?"
    
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
    
    ma "And with that the Iwatobi Swim Club officially has its first female member!"
    
    ma "Welcome to the team %(povLastName)s-Chan!" 
    
    scene bg white 
    
    scene bg School Gates_Afternoon with flash 
    
    d "Me and my big mouth. With that slip of tonge in anger, I was now part of the swim club." 
    
    d "Gou and Miho wasted no time ushering me to the back to get my size and measurements for a suit." 
    
    d "I told them I wanted gray trim, but I get the feeling they'll end up making it yellow or pink." 
    
    d "I have to fill out some forms and the nurse gave me a general check-up. Finding nothing wrong phsyically, she cleared me for swimming against my better protests." 
    
    d "Gou then instructed Makoto and Haru to walk me home, as she had some errands to run."
    
    d "One being getting my swimsuit ordered..." 
    
    d "She also mentioned dropping off some things for her older brother at a different school." 
    
    
    scene bg white 
    
    scene bg Swimming Pool A_2 with flash 
    
    show Gou Neutral at left with dissolve 
    
    show Makoto Neutral at right with dissolve
    
    gm "Makoto, could you make sure to get %(povFirstName)s home?" 
    
    show Gou Determined with dissolve
    
    gm "I don't think we want her getting lost on her way back. Or trying to escape by jumping a ship at the harbor." 
    
    y "I heard that!" 
    
    mt "Just leave it to me and Haru, we'll get her back to your house safe!" 
    
    gm "Great! I'll tell Rin you said hi." 
    
    scene bg white 
    
    scene bg School Gates_Afternoon with flash 
    
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
    
    d "The awkwardness continues into silence...." 
    
    d "That is until my phone decides to pipe up." 
    
    unknown "Mistress, our quest for the chalice awaits!" 
    
    show Makoto Bashful with dissolve
    
    d "Oh man, I had forgotten I had set the alerts for when my quest energy was full." 
    
    d "Makoto is grinning at me right now." 
    
    mt "Was that what I think it was?"
    
    y "No, I'm pretty sure you're imaging things." 
    
    show Makoto Devious with dissolve
    
    mt "No was, that was an alert from ''Destiny's Ultimate Challenge' wasn't it?"
    
    y "I have no idea what you're talking about." 
    
    d "Makoto is now going through his side pocket." 
    
    d "He pulls out his smartphone and starts tapping. A couple of minutes later he hands it to me." 
    
    d "A familiar start screen brightens the face of his phone." 
    
    y "Okay, Okay. Yes, that was an alert from DUC." 
    
    y "...I liked the visual novel and wanted to play the app...." 
    
    y "I had to backdoor my way into the app since it's only available from the App Center in Japan." 
    
    y "So yes....I'm a dork." 
    
    show Makoto Neutral with dissolve
    
    mt "Dork? Then I guess you fit in with us even more. We play it!" 
    
    mt "Even Haru over there, when he isn't climbing into a fountain or something." 
    
    d "Hitting the start key reveals Makoto's character screen." 
    
    y "Oh man! How did you get the Class-A Duelist d'Artagnan?!?!" 
    
    y "I wanted her so much, but my draws were all unlucky." 
    
    mt "I got lucky and won a secret code drawing that gave me that Champion." 
    
    show Makoto Bashful with dissolve
    
    show Haru Annoyed with dissolve
    
    mt "I don't think I've seen Haru so upset since the time he missed swim practice with a cold." 
    
    hn "..." 
    
    y "You play as well? Who's your primary Champion?"
    
    show Haru Neutral with dissolve
    
    hn "Eliminator. Class-B. Wilkes Booth." 
    
    y "I'm not sure I'm more disturbed that your main Champion is the man who killed Abe Lincoln...." 
    
    y "Or that it totally fits your personality." 
    
    hn "..." 
    
    show Makoto Sad with dissolve
    
    mt "Look, I hope you don't find this too pushy, but maybe I can send you an ally request." 
    
    show Makoto Neutral with dissolve 
    
    mt "BackMakoto is my user ID. And WaterboyHaru is Haru's." 
    
    d "After a few quick flicks and some typing, I've sent the requests." 
    
    y "You should have my requests. My user ID is Silent Gone." 
    
    y "I have a Class-A Sorcerer as my main Champion. Morgan le Fay." 
    
    y "Hey don't you guys find it odd that a Japanese product uses so many figures from European history in it?"
    
    show Makoto Sad with dissolve
    
    mt "Only a little. But I think they'd run out of epic characters if they stuck to only Japan." 
    
    y "I supposed you're right..." 
    
    show Makoto Neutral with dissolve
    
    mt "Are you into any other video games?"
    
    y "Sure, I left my Station-Xcite console at home, but I had some games I enjoyed." 
    
    mt "Want to join the gang over at Haru's place this Saturday?" 
    
    show Makoto Bashful with dissolve
    
    mt " I just picked up 'Strut, Slide and Slam Master 3' and we were all going to try it out." 
    
    mt "You're part of the team now so maybe you'd like to hang out. Get to know us, have some fun. Show off your dance moves." 
    
    y "You know what-you're on!" 
    
    y "I may not be up to speed at swimming with you guys yet, but I'm sure I can be master of the mosh pit." 
    
    hn "Unlikely." 
    
    show Makoto Worried with dissolve
    
    mt "Haru currently owns that title among us. I was so close to beating him last time..." 
    
    mt "But he got just a little extra oomph into his last slam on me and won." 
    
    show Makoto Neutral with dissolve
    
    hn "..." 
    
    d "We chat a little bit longer as we approach the house I'm staying out." 
    
    d"Once we get there Makoto looks at me and smiles." 
    
    show Makoto Bashful with dissolve 
    
    mt "Hey, is it cool to get your phone number?"
    
    mt "This way, I can text you the plans for this Saturday." 
    
    y "Sure, that makes sense." 
    
    d "He holds up his phone, and I match mine to it." 
    
    d "A few seconds later, our contacts are swapped. Then looking to the other side, I see Haru. He's holding up his phone." 
    
    y "You want my number?"
    
    hn "..." 
    
    hn "Yes." 
    
    y "Well, okay, just don't send me anything weird." 
    
    d "We use the beam exchange and our contacts are swapped." 
    
    show Makoto Sad with dissolve
    
    mt "Well we have to get going so we can work on our homework as well." 
    
    mt "Catch you at school tomorrow!" 
    
    hide Makoto with dissolve
    
    hide Haru with dissolve
    
    d "They both wave as they leave me on the doorstep of Gou's house." 
    
    d "Maybe this won't be so bad after all." 
    
    
    
    
    stop music
    
    return
