# main 
define yj = Character(_("Younger Judi"), color="#F1DD5F")
define j = Character(_("Judi"), color="#F1DD5F")

# side 
define jm = Character(_("Judi's Mother"), color="#f77e33")
define jf = Character(_("Judi's Father"), color="#f77e33")
define js = Character(_("Judi's Siblings"), color="#f77e33")

# anon
define go = Character(_("Guidance Officer"), color="#000000")
define cm = Character(_("Classmate"), color="#000000")

# The game starts here.

label jb_start:

    play music "audio/Story.mp3" fadein 3.0 volume 0.5

    scene blackscreen 
    pause 1.0

    scene bg guidanceoffice with fade

    show oj neutral with dissolve

    "Alone in the guidance office, Judi sits alone in front of the Guidance Officer, a warm, yet concerned expression on their face."

    go "Judi, we’ve noticed your bandages… They never seem to go away."

    show oj happy with dissolve

    "They look intently at Judi, who quickly flashes them a smile."

    yj "Hehe, that’s just me. I’m a bit clumsy, always tripping over something."

    show oj neutral with dissolve

    "The guidance officer gives her a gentle, worried look. Judi holds her smile, unflinching."

    go "…Alright, but remember, I’m here if you ever need anything."

    "Judi thanked the officer, still keeping that smile on her face."

    stop music fadeout 1.0

    show bg schoolgate with fade

    play sound "audio/school-bell.mp3"

    play music ["<silence 4.0>","audio/Story.mp3"] fadein 3.0 volume 0.5

    "The bell rings, signaling the end of classes for the day. Students can be heard walking about, saying their goodbyes to one another."

    cm "Bye, Judi! See you tomorrow!"

    yj "See you!"

    stop music fadeout 1.0

    play music ["<silence 4.0>","audio/Story_NO_MELODY.mp3"] fadein 3.0 volume 0.5

    show oj sad with dissolve

    "Once she was out of sight, the smile Judi had been wearing had disappeared."

    yj "*sigh*"

    yj "I don’t wanna go home yet… I wish the day lasted a little longer…"

    scene bg jhome_hallway with fade

    show oj neutral with dissolve

    stop music fadeout 1.0

    "Judi arrives home and quietly enters inside, hoping not to be found by her parents."

    play music ["<silence 4.0>","audio/Eerie_NO_MELODY.mp3"] fadein 1.0 volume 0.5

    "However, luck isn’t on her side."

    play sound "audio/bottle-shatter.mp3"

    show oj sad with dissolve

    with hpunch
    pause 0.5
    
    "As she crosses the hallway, a beer bottle flies past her and shatters, a shard grazing her arm. Her younger siblings cry at the noise."

    jm "JUDI! WHERE HAVE YOU BEEN!?"

    "Judi puts a hand on her grazed arm, legs trembling as she answers her mother’s question."

    yj "I-I was at school."

    jm "How DARE you leave me alone to take care of them! You’re the oldest child! That is YOUR responsibility!"

    yj "I’m sorry, Mom."

    jm "You know I love you, right? You know how much effort I put into raising you and giving birth to your siblings."

    yj "Yes, Mom."

    jm "You can't leave me alone with them, Judi. Your father doesn't give us enough attention already, and you know how hard I have to work to make up for that too, right?"

    yj "Yes, Mom."

    jm "You little brat. Do you even understand what I’m saying? Are you even listening or do I have to knock some sense into you again?"

    "Before her mother does something else, Judi rushes to grab her siblings, bringing them into her room."

    show bg judiroom with fade

    "Judi closes the door quickly as they enter, but her siblings are still crying."

    yj "Can you two STOP CRYING?!"

    "Her siblings look at her, startled, on the verge of sobbing even louder. Panicking, Judi grips them tightly, trying to silence their cries."

    "Once they quiet down, they huddle together in a corner, tears still streaming down their faces."

    jm "JUDI! DO YOUR CHORES NOW!"

    scene blackscreen with fade

    "Years later..."

    scene bg jhome_diningtable with fade

    show oj sad with dissolve

    "Everyone sits around the dining table, eating in silence. Tension’s in the air as Judi’s father, irritated and barely looking at her, breaks that silence in a cold tone."

    jf "So, got a call from the school today. Mind explaining why you’re slacking off?"

    "Judi stares down at her plate, tensing up. Her mother shifts nervously and shoots her a glance."

    j "Um..."

    jf "Absences, failing grades… Judi, do you not care about us at all? I’ve been working myself to the bone here and this is what you give me?"

    j "B-but—"

    "Her mother cuts her off, shifting her husband’s attention to her."

    stop music fadeout 1.0

    jm "Oh, honey, I’m sorry. It’s all my fault. I promise I’ll do better—"

    play sound "audio/table-slam.mp3"

    with vpunch 
    pause 0.3

    "Judi’s father slams the table, cutting her off and startling everyone."

    play music ["<silence 2.0>","audio/Eerie_NO_MELODY.mp3"] fadein 1.0 volume 0.5

    jf "SHUT UP! All you’ve done is make excuses. Look at your daughter! She’s a reflection of yourself, a disappointment. You never do anything right!"

    "Judi hunched over in her seat, slamming her eyes shut. In a desperate attempt to silence their shouts, she covered her ears with her shaking hands, heart pounding and breathing heavily."

    jf "You’ll do better? The only thing you’ve ever been good at is screwing things up. Like mother, like daughter. You’re both failures!"

    "Feeling tears were about to form, Judi gets up and storms out of the house."

    # play sound "door slam sfx"

    scene bg park with fade

    show oj sad with dissolve

    "Judi wanders around aimlessly to escape the situation and sees children having fun playing with their parents in a nearby park. She scoffs at her situation."

    j "I don’t know how much longer l can take this."

    "She looks up at the sky and feels tears freely flowing down her cheeks, eyes blank and expressionless."

    window hide
    show screen judi_parkhand with fade
    pause

    show screen judi_parkfull with dissolve
    pause

    j "I’m so tired. Why do I have to put up with this…"

    hide screen judi_parkhand
    hide screen judi_parkfull with fade

    stop music fadeout 1.0

    play sound ["<silence 3.0>", "audio/babylaugh.mp3"]

    "Closing her eyes, she feels the gentle breeze flow on her face, cooling her tear-stricken face. An image pops in her mind as she softly hears a baby’s laughter."

    play music ["<silence 2.0>","audio/Hope_NO_MELODY-2.mp3"] fadein 1.0 volume 0.5

    j "Ah."

    "She runs back home and opens the door, hearing soft cries calling her name."

    scene bg judiroom with fade #jsiblingspscene

    show oj sad with dissolve

    "Though beaten, scratched, and bruised, faces stained with tears, Judi and her siblings huddle together in bed."

    j "I’m sorry for leaving you two."

    js "We’re the ones who should say sorry! We cried too much, which made both Mom and Dad angry. If we didn’t, maybe you wouldn’t have gotten hurt when you got back."

    j "No, you shouldn’t apologize for that. Heh, Mom’ll still hit me anyway since I left the house. I’m sorry you two got caught up in that."

    "Her siblings then cling to her, speaking softly."

    js "We love you, no matter what."

    "Feeling the tears well up again, Judi pulls them closer and hugs them."

    j "…I love you both. I won’t leave you two like that again, I promise. I’ll protect you."

    "They stay huddled together like that, holding on until they eventually drift off to sleep."

    scene blackscreen with fade
    
    call judieyes1 

    return
