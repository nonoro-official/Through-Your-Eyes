# main 
define yk = Character("Younger Kei", color="#576ca8")

# combined
define ks = Character("Kei's Siblings", color="#590f6c")

# side
define ks1 = Character("Kei's Sibling #1", color="#590f6c")
define ks2 = Character("Kei's Sibling #2", color="#590f6c")

# anon
define t = Character(_("Teacher"), color="#000000")
define cm1 = Character(_("Classmate #1"), color="#000000")
define cm2 = Character(_("Classmate #2"), color="#000000")
define cm3 = Character(_("Classmate #3"), color="#000000")
define cm4 = Character(_("Classmate #4"), color="#000000")
define cm5 = Character(_("Classmate #5"), color="#000000")
define cm6 = Character(_("Classmate #6"), color="#000000")
define cm7 = Character(_("Classmate #7"), color="#000000")
define cm8 = Character(_("Classmate #8"), color="#000000")

# The game starts here.

label kt_start:

    scene blackscreen 
    pause 1.0

    scene bg classroom
    # play sound "audio/car-crash.mp3" fadein 2.0 (noisy classroom)

    "Ruckus greets the homeroom teacher first thing in the morning as soon as they enter the classroom."

    t "Good news, class! Listen up."

    "The classroom quiets down, curious about the good news."

    t "Your exams have been graded. One by one, I will call your name and get your paper in front."

    "Whines and groans can be heard throughout the room."

    t "You guys did well holding up during the exams. Congratulations! You may enjoy your break next week."

    "The classroom buzzed with cheers and excitement."

    t "One more thing. As you all know, annually after break, we host a school exhibition and classes participate by creating their own booths."

    t "This time, the principal has suggested a booth competition wherein the winner wins a grand prize."

    cm1 "Wanna bet on what it is? It’s definitely money!"

    cm2 "Snacks, maybe? That’s what the student council usually gives as their prize."

    cm3 "Seriously? You guys really think they’ll spend that much money for 30 students? Well, I bet it’s just some certificate."

    cm4 "That may be so, but let’s still win first place!"

    t "Ehem! Further details will be announced by the principal in the morning assembly after the break. In the meantime, each class will need to have a representative for their exhibition. Any volunteers?"

    "The clamor instantly died down. After minutes of waiting in silence, the teacher sighed."

    show k neutral with dissolve

    t "Since none of you would like to volunteer… Kei, would it be alright for you to be our class representative?"

    t "The role is nothing too heavy, don’t worry. You’ll just act as the medium between your class, the teachers, and other representatives."

    cm3 "Yeah, dude. You totally got this. You’re, like, the smartest guy in class."

    "Everyone in the class immediately agreed, not wanting to be nominated and bothered by the tasks. With not so much of a choice, Kei reluctantly accepted."

    yk "… I guess I can be the representative…"

    scene bg schoolhallway with fade

    # play sound "kitchen / clanging sounds sfx"
    # play sound "kids laughter sfx"

    "It’s been 2 weeks since the principal explained the school exhibition. The whole school still buzzes with excitement, preparing for the upcoming event."

    show k neutral with dissolve

    "As the classroom representative, Kei’s class deemed him the leader for their booth as well. Kei couldn’t possibly refuse their proposal yet again."

    cm2 "Hey, leader. There’s a slight problem. We’ve run out of paint for the booth sign. What should we do?"

    cm4 "Sorry to disturb you, Kei, but how do you do this again? I know you’ve already taught us, but I just still can’t do it right."

    cm3 "Kei! The other class’s representative is here for you. Said something about poster and handout designs."

    cm1 "Do you know where the props are, Kei? I can’t seem to find them anywhere…"

    "Kei moved from one task to another, whether it was assigned to him or helping the others. Time was limited, after all. The awaited event was already next week."

    cm6 "Sorry, Kei, gotta go. I still have my club activities. I can’t miss them out or else I’m out of the team. I left my work on my table. I’m relying on you."

    cm5 "Urk. I’m going home… I don’t feel so good. Sorry, Kei, but can you help me with these? Please, I don’t think I can finish it…"

    cm7 "I’m getting bored… Wanna hang out at my house?"

    cm8 "Sweet! Let’s go. There’s still plenty of time left until the exhibition anyway. Kei, we’ll leave it up to you, ‘kay?"

    show k upset with dissolve

    yk "Ah, but—"

    "Before Kei can talk it out with them, they’ve already packed their bags and rushed out. Kei sighs in frustration and exhaustion."

    yk "… you could’ve at least brought some work to do at home."

    show k neutral with dissolve

    "Giving up, he continued on to his tasks, finishing everything he could before going home. He still has so much to do at home too."

    show blackscreen with fade

    "Hours later..."

    hide blackscreen 

    play sound "audio/school-bell.mp3"

    "The bell rings indicating the school’s closing hours and that students must be on their way."

    yk "Shoot! It’s already time? I still have a few more things to do… I should just continue them at home."

    "As he rushed to pack his things and the unfinished work, he failed to notice the mess the room was in before he left."

    scene blackscreen with fade

    "Next morning..."

    scene bg classroom with fade

    "Kei decided to go to school early to lessen as much workload as he can, sacrificing sleep in the process."

    "In his hand was a bag of finished work. He stayed up all night, diligently completing each task."

    yk "Ugh. My head hurts… I should’ve just stayed at home and called in sick. But there’s still more to do… At least I finished these…"

    "He stopped at the entrance of his classroom, shocked to see what awaited him."

    "Splashes of paint on the floor, stuff littered everywhere, and props stacked unkempt in one corner."

    # flashback

    scene bg khome_hallway1 with fade

    show k neutral with dissolve

    yk "I'm home!"

    "Kei just arrived home from school, feeling so exhausted. Greeting no one, he proceeded into the living room to leave his things and get ready to prepare dinner.
"

    scene bg khome_livingroom with fade

    show yk upset with dissolve

    "He flinched and felt nauseated when he smelled alcohol once he stepped into the space. What he saw was an utter mess."

    "There were bottles on the floor, one seemed to have spilled; a bag of leftover chips on the table, crumbs scattered along the carpet; outside clothes tossed around everywhere; and the TV was still running."

    "He noticed two drunk people sleeping: one body awkwardly lying on the couch, and one splayed near the table."

    yk "You have got to be kidding me."

    yk "Wake up! Come on, get up. You guys gotta go to your rooms."

    "After struggling getting his brothers in their respective rooms, Kei cleaned up after them."

    show k neutral with dissolve

    yk "Can’t they clean up after themselves for once? They’re literally older than me."

    yk "*sigh*"

    yk "Now for my own chores…"

    # flashback end

    scene bg classroom with fade

    show k neutral with dissolve

    "After cleaning the room, Kei moves on to work. Too much on both his mind and hands, his head pounds."

    show k upset with dissolve

    yk "Ugh… my head…"

    yk "Tsk.. there’s too much to do… I can’t focus."

    # sfx laughter & door slam open

    "He hears laughter slowly approaching and the door being slammed open. The sound made his head pound more, hammering through his skull."

    show k neutral with dissolve

    "Ignoring the dull throb, he continues on his tasks after greeting them."

    # sfx chatter

    cm3 "Morning, guys! Want some? My cousin got back from his business trip…"

    cm2 "Hey, have you seen the new action series on TV? That really famous actor is the main character and…"

    cm4 "Omg! Did you hear they’re going to release a new album this month? I’m so excited…"

    "Noise starts to flood the classroom as Kei’s classmates enter the class one by one."

    # sfx throb ? 

    "Noise starts to flood the classroom as Kei’s classmates enter the class one by one."

    yk "Ugh..."

    # sfx muffled sound + ringing

    "No one noticed as he closed his eyes and pressed his palms against his temples, rubbing them to ease the pain. The noise in the background became muffled and he could hear a high-pitched ringing."

    # flashback

    scene bg keiroom with fade

    show k neutral with dissolve

    # music - loud music

    "Kei was studying in his bedroom when he suddenly heard loud music reverberating throughout the house."

    show k confused with dissolve

    "Skeptical, he went downstairs and saw his siblings with some guests."

    scene bg khome_livingroom with fade

    show k neutral with dissolve

    ks1 "Oh, there he is! We were just talking about you."

    ks2 "Guys, meet our little brother, Kei."

    "Kei waved back when his siblings’ friends introduced themselves."

    yk "Can you lower the music a little? I’m kinda trying to study…"

    ks2 "Pshh, you’re too sensitive. Loosen up for once."

    ks1 "Oh, and can you clean up a little? It’s kinda messy. And have you cooked dinner? We’re starving."

    "Kei’s siblings and their friends scattered throughout the room, looking and chattering about stuff."

    yk "I’m going back to my room."

    show bg keiroom with fade

    "He went and locked the door, not wanting to be disturbed. He tried to wear headphones to cancel out the loud music but the sound still came through."

    "Feeling a headache forming, he tries to blast his ears with white noise and focuses on his studying."

    # flashback end

    scene bg classroom with fade

    show k nooo with dissolve

    "Kei’s breathing got heavier as the ringing in his ears got louder and the throbs got quicker."

    "Unbeknownst to Kei, his classmate approached him for a favor, placing their hand on his shoulder."

    cm1 "Hey, Kei, can I ask for a small favor—"

    show k upset with dissolve

    yk "Just shut up!"

    yk "I’m so tired of trying to cover for you guys! Can’t you do it on your own!? You’re not babies anymore!"

    yk "I thought you guys wanted to win, but all you do is blabber and play around without getting anything done. Don’t you realize the event is just a week away!?"

    yk "Why is it always me… why do I always have to be the one to sacrifice myself for your sakes. I can’t even take a second to rest!"

    "The entire room goes quiet, surprised by Kei’s sudden outburst."

    yk "I-I didn’t mean— I’m so sorry…"

    "He then runs out of the room, devastated, realizing what he’d done."

    call demoend 
    with fade

    return
