# main 
define j = Character("Judi", color="#f1dd5f")
define k = Character("Kei", color="#576ca8")
define a = Character("Ali", color="#fab6de")

# combined
define jk = Character("Judi & Kei", color="#b45f06")
define jka = Character("Judi, Kei, & Ali", color="#660000")

# side / anon
define t = Character("Teacher", color="#000000")
define ch = Character("Chauffer", color="#000000")

# define
define slow_fade = Fade(0.5, 0.0, 0.3)  # 3 seconds fade transition

# The game starts here.

label intro_start:

    play music "audio/Story.mp3" fadein 3.0 volume 0.5

    scene bg classroom with fade

    "The classroom buzzes with chatter. The teacher steps up front, clapping hands to get everyone’s attention."

label proj_topics: 
    t "Alright everyone, today I will assign you your groups for this week’s project. This project will be on"

menu:
    "Generational Trauma":
        jump intro_cont
    "Spaces, Places, and Territories":
        jump intro_cont

label intro_cont:
 
    "The teacher then starts assigning everyone into groups."

    t "Judi, Kei, Ali—you’re together."

    show j neutral at left
    with dissolve

    j "Hehe, nice! We’re together! This is gonna be fun!"

    show k happy with dissolve

    k "Alright. Now, let’s start this thing."

    show a happy at right
    with dissolve 

    a "Okay."

    "The three kids huddle around a table to brainstorm on their newly assigned project."

    stop music fadeout 1.0

    show bg schoolgate with fade

    show k neutral 
    show a neutral
    with dissolve

    play sound "audio/school-bell.mp3"

    play music ["<silence 4.0>","audio/Story.mp3"] fadein 3.0 volume 0.5

    "The last bell rings, signaling the end of classes for the day. Students can be heard walking and chattering about while leaving the classrooms."

    k "Okay, so that’s about it for the project. Everyone good with it for now?"

    j "Yep! It looks pretty good to me."

    a "Same here."

    k "Nice, nice. We can work and revise it another time. How about book cafe after class at around 4pm?"

    j "Sure, sure! I’m good with that."

    a "Same."

    "A car pulls up, with Ali recognizing it to be her chauffeur."

    ch "Sir Ali, time to go."

    a "Alright, guys. I’m out. See you."

    jk "See you!"

    hide a neutral with dissolve

    "Ali enters and leaves, the car driving away, leaving Judi and Kei standing together."

    j "I gotta go now too."

    k "Same. Take care. And don’t forget about the meet-up!"

    j "I won’t, I won’t! See you!"

    scene bg cafe with fade

    show k neutral at left

    show j neutral

    show a neutral at right
    with dissolve

    "The group is gathered around a table with materials scattered about, discussing the project."

    k "So what we could do for this part is—"

    show j happy with dissolve

    "Judi suddenly jumps up from her chair, cutting him off."

    j "I think we should take a snack break. How about the convenience store?"

    show k confused with dissolve

    "Kei gives her an annoyed look."

    k "Judi. Let’s just stay indoors, yeah? We gotta focus."

    j "Oh c’mon, Kei. Look at Ali—she’s down."

    show a happy with dissolve

    "Ali’s eyes sparkle in interest."

    show k upset with dissolve

    k "Seriously? Ugh, fine. But this can’t be long."

    show j silly with dissolve

    j "Yay! I promise that this will be worth it."

    show k confused with dissolve

    "Kei gives her a skeptical look but stands up anyway as the three head out together."

    scene bg conveniencestore with fade

    show j neutral at left

    show a happy

    show k confused at right
    with dissolve

    "The group exits the store, Judi and Ali content with their bought snacks and Kei looking both annoyed and defeated."

    show j happy with dissolve

    j "See? Didn’t take long at all!"

    k "Whatever. Let’s just go back now so we can continue working on the project."

    scene bg street with fade

    "They walk down the street, heading back to the meeting place when suddenly—a cat darts by and snatches Kei’s bag of snacks."

    window hide
    show screen cat_thief with fade

    play sound "audio/meow.mp3"

    pause

    hide screen cat_thief with fade

    show j shocked at left

    show a surprised

    show k confused at right
    with dissolve

    k "Just great."

    j "After the cat! Those snacks ain’t free!"

    "Judi dashes off chasing after the cat, with Ali following close behind."

    hide j shocked
    hide a surprised
    with dissolve

    show k upset with dissolve

    k "This is gonna take longer than planned now, isn’t it..."

    show k confused with dissolve

    "Kei sighs, reluctantly joining the chase, running after his friends and the stolen snacks."

    scene bg abandonedentrance with fade

    show k upset at right
    with dissolve

    "Kei finally catches up with Judi and Ali, panting as he arrives at what looks like an abandoned building."

    k "Finally, I caught up with you two."

    show j neutral at left

    show a neutral
    with dissolve

    j "Where’s that cat thief?"

    "The cat slips through an open window, and Judi quickly points."

    show j shocked with dissolve

    j "There! It went inside!"

    stop music fadeout 1.0

    play music "audio/Eerie.mp3" fadein 3.0 volume 0.5

    show k confused with dissolve

    k "This feels like a bad idea. Are we allowed to be here? Where even are we?"

    show j neutral with dissolve

    j "Um… it’s abandoned, right? Even though it looks really clean?"

    "The trio hesitates, staring at the suspiciously neat building. Despite this, Ali moves toward the entrance, uninterested in waiting."

    show k upset with dissolve

    k "Ali, wait!"

    play sound "audio/door-opening.mp3"

    show a surprised with dissolve

    "She pushes the door, and it swings open easily."

    a "It’s unlocked. C’mon, let’s see if we can get those goods back."

    j "…okay then."

    k "This is definitely a bad idea."

    "Kei reluctantly follows as the three head inside the strange yet mystical abandoned building."

    scene bg abandonedmirror with fade

    show j neutral at left

    show a neutral

    show k confused at right
    with dissolve

    "The trio steps into the open space. In the middle of the room, Kei spots their bag lying on the floor, the cat nowhere in sight. He goes to grab it."

    show k neutral with dissolve

    k "‘Kay. Got it. Now let’s go."

    play sound ["<silence 0.5>", "audio/locked-doorknob.mp3"]

    "They make a run for the exit—only to find it locked."

    show j shocked with dissolve

    j "Uh oh…"

    show k confused with dissolve

    k "How about the windows?"

    "They rush to the windows, frantically trying to pry them open, only to no avail."

    show j sad with dissolve

    j "Guys, I am so sorry. You were right, Kei. We should’ve just stayed indoors. Now we’re stuck here."

    show k neutral with dissolve

    k "Hey, it’s not like we expected this to happen anyway. It isn’t your fault. Let’s calm down, okay?"

    a "At least we’re together, right, Judi?"

    stop music fadeout 1.0

    play music "audio/Hope_NO_MELODY-2.mp3" fadein 3.0 volume 0.5

    window hide
    show screen friend_comfort with fade

    pause

    hide screen friend_comfort with fade

    j "Y-yeah. Sorry… I’m just pretty worried about my siblings, you know? I don’t want to leave them alone at home."

    j "I mean… your parents must be waiting for you at home too, right?"

    k "Nah. My mom’s at work. My older siblings are the ones at home."

    a "My chauffeur will fetch me. My parents are busy with work, so I’ll just be alone at home."

    stop music fadeout 1.0

    play music "audio/Eerie_NO_MELODY.mp3" fadein 3.0 volume 0.5

    "The room falls silent, tension hanging in the air as they all process each other’s lives."

    show k nooo with dissolve

    show a upset with dissolve

    "They share one unspoken thought."

    jka "I wish I had their life."

    # play sound "jka thought audio"

    stop music fadeout 1.0

    play sound "audio/glow.mp3" 

    "Suddenly, the mirror hanging in the middle of the wall begins to glow, casting an eerie light over the room."

    show flash with slow_fade
    pause 0.5

    scene blackscreen with fade

    # show character / color choices

    call screen character_selection

    # This ends the game.

    return
