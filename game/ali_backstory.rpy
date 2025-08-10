# main
define a = Character("Ali", color="#fab6de")

# side
define af = Character("Ali's Father", color="#8f98a3")
define am = Character("Ali's Mother", color="#8f98a3")
define ag = Character("Ali's Grandmother", color="#8f98a3")

# combined
define ap = Character("Ali's Parents", color="#000000")

# anon
define s = Character("Secretary", color="#000000")
define e = Character("Emcee", color="#000000")
define jd = Character("Judges", color="#000000")
define ch = Character("Chauffer", color="#000000")

# The game starts here.

label ab_start:

    scene blackscreen 
    pause 1.0

    scene bg fancyparty with fade

    "Chatters echo around the hall, varying from greetings to business talk."

    "Ali’s parents walk on the stage and catch the attention of many. Tapping on the microphone, they deliver great news to everyone."

    af "To everyone gathered here today, thank you all for coming. My wife and I would like to share some wonderful news!"

    "The spouses share warm smiles, encouraging each other before the announcement."

    am "We all have been waiting for this moment. After years of waiting, we now can proudly share that I come with a child."

    # play sound "audio/applause.mp3"

    "Rounds of applause and congratulations at the news cover the hall. Smiles can be seen littered across the room in each and every corner."

    "Once off the stage, Ali’s grandmother approached her parents, a proud smile lifting on her face."

    ag "At long last! Congratulations, there will finally be an heir to our corporation. I was worried that I’d have to leave the company to your incompetent brother."

    "Ali’s grandmother continued to slander her other son’s ineptitude, not even trying to hide her frustration. Ali’s parents awkwardly laughed to ease out the tense atmosphere."

    ag "Moving on. What’s its gender? Hopefully not a girl. Who would inherit the company if it was? She’ll be a useless asset. Unless… we arrange her marriage with our rival company."

    "Ali’s father clenched his fist in anger, trying to restrain bursting out. His wife, although clearly upset by her mother-in-law’s suggestion, calmed her husband down, making soothing circles on his arm."

    af "…I apologize, Mother. I’m afraid it is still too early to know our baby’s gender. We’ll let you know once we do."

    ag "Tsk, alright. I expect nothing less from your baby, considering you two as its parents."

    "The already tense atmosphere became heavier as Ali’s grandmother kept yapping. Bystanders seem to notice and try eavesdropping."

    ag "Look at your brother’s son. Surprisingly smart and decent enough. Others say he’s a genius."

    ag "It was a good idea to let him marry that hideous woman. Her looks are… below average, but her brains make up for it, at least—"

    "Ali’s mother cuts her off, offended by the recent remark. She lies her way out, dragging her husband as well."

    am "I’m afraid I have to excuse myself. I’m feeling a little under the weather. My dear, would you please accompany me?"

    af "Of course, dear. If you would please excuse us, Mother."

    "Ali’s father bids her farewell, grateful to his wife for getting them out of his mother’s inconsiderate blabbering."

    scene bg afterparty

    "After helping the guests out, Ali’s parents both stayed behind to have a serious conversation."

    am "We can’t tell her, dear. I don’t think I can bear seeing Ali living her life under mother-in-law’s contempt."

    af "I know… but people will know eventually after our baby is born. Unless…"

    "Ali’s mother looked at her husband’s eyes in desperation, anxiously waiting for his next words."

    af "We let Ali live her life as a boy—"

    am "What!? Are you out of your mind—"

    "Ali’s father successfully cut his wife off, holding her arms and gripping her firmly."

    af "Just until she can confidently fend herself amongst our family. We have to do this for her sake, dear."

    af "With how things are: how most of our family still sides with Mother; how busy we are changing the company’s ways, we won’t be by Ali’s side at all times."

    "Ali’s mother looked broken, but her husband had a point. She stared at her belly for a long time, a sad smile on her face. Caressing her belly, she agreed with her husband’s absurd suggestion."

    am "In order to prove herself, she’ll need to enroll in various lessons as preparation… I’ll call my contacts to find the best tutors there are."

    "Ali’s parents both shared a pained expression, devastated to have to resort to this plan. They embraced each other tightly, anxious for the future of their dearest baby girl."

    scene blackscreen with fade

    scene bg aliroom with fade

    "Standing in front of a mirror, their secretary fixes Ali’s vest. She stares intensely at her reflection, thoughts going miles a minute."

    a "Uhm… Mr. Secretary?"

    s "How may I be of help, Young Master?"

    a "Why can’t I wear a dress like the other girls?"

    "The secretary instantly stopped whatever he was doing and looked Ali straight in her eyes in the mirror."

    a "I want to wear pretty dresses too. Not only that, I want cute and frilly clothes, sparkly shoes, bags, and other girl stuff."

    "The secretary turned away his gaze and resumed fixing Ali’s appearance for the next lesson."

    s "I apologize, Young Master. I am not entirely certain about the reason… However, I do believe that the Master and Miss only wish to protect you."

    a "I don’t… understand."

    s "I suppose it is still too early for you. Should you ask again when you’re older, your parents might give you the answer."

    "Done getting her ready, the secretary patted Ali on the head and smiled. Escorting her out of the dressing room, Ali continued her day full of general education, piano lessons, and business management."

    scene bg concerthall with fade

    "The audience was packed with people of all ages, from toddlers to elders. Chatters echoed throughout the hall while waiting for the program to start."

    e "Please settle down as we begin the Intra School Musical Concours’ Final Selection."

    "The stage then dimmed and the noise turned silent. The emcee proceeds with a short opening and introduces the first performer."

    scene blackscreen with fade

    scene bg concerthall with fade

    e "Performer #4, from the Business Department, Mr. Ali. Performing a Chopin composition, “Nocturne in C minor, Op. 48 No. 1.”"

    "Ali proceeds to the center of the stage, momentarily looking for her parents in the audience."

    a "…absent yet again."

    "With hidden disappointment of not finding them in their reserved spots, she continued with her piece."

    with fade

    e "The judges shall now announce the results in the Intra School Musical Concours’ Final Selection."

    "The judges began with the last place, moving up to the winner."

    jd "And in 1st place, Mr. Ali."

    play sound "audio/applause.mp3" # fix length and add fadeout

    scene bg car wih fade

    "Inside the car, Ali looks out the window with a bored expression."

    a "I thought they said they’d come."

    ch "Pardon me, Young Master. They were already on the way when they were suddenly called in for an urgent business meeting."

    ch "They also wanted me to inform you that they’ll be home in time for dinner."

    "Ali quickly glanced at the chauffeur at the news, a small expectant smile forming on her lips."

    scene bg ahome_diningtable with fade

    "Disregarding table manners, Ali placed her elbow on the table and supported her head, waiting in anticipation. She played and poked at her food, taking small bites once in a while."

    "She then hears a car approaching and asks the servants to heat up the food."

    "Excitedly rushing to the front door, her giddy expression immediately disappeared at the sight of their secretary carrying a tablet."

    # play sound caller ringing

    am "Good evening, Ali. I heard about the competition. Congratulations on winning!"

    a "…thank you, Mother."

    "Ali’s mother noticed her daughter's deflated expression. She showed an apologetic smile through the screen."

    am "We’re so sorry, my dear. There was a sudden call and—"

    a "It’s alright. You don’t have to explain. I understand."

    "There was an awkward silence after Ali interrupted her mother."

    am "…I’m afraid we’ll only be available during the celebration party. There was a problem in one of our branches and we had to go there to see it in person. We’re so sorry."

    a "It’s okay. At least you’ll be able to come."

    a "Promise you’ll be early?"

    am "Promise."

    "She smiled at her daughter’s childish behavior. Looks can be deceiving, as the phrase goes."

    a "…may I ask you something?"

    "Curious at her hesitance, Ali’s mother encouraged her to continue."

    am "What is it? Go on."

    a "Why do I have to dress up like a boy?"

    "Her mother was speechless at the unexpected question."

    a "I asked our secretary before and it has been years since. I’m clearly old enough to understand, but why can’t I still know the reason?"

    "Ali’s mother opened her mouth to answer, but her voice didn't seem to work. Ali sees the discomfort in her mother’s face trying to answer the question."

    # play sound muffled phone ringing

    "Taking the distraction, Ali’s mother answered the call. Ali, watching everything from the screen, knew that it was important. The call ended and her mother sighed."

    am "It was your father. I’m sorry we have to cut this conversation short but—"

    a "You can go. It’s clearly important."

    "Not noticing the sadness flashing on Ali’s face, Ali’s mother soon ended the call after exchanging final goodbyes."

    "Ali and the secretary shared an awkward silence until Ali excused herself."

    a "…I’ve lost my appetite. I’m heading back to my room."

    # timeskip to ali's bday

    scene bg ahome_livingroom with fade

    "As Ali walks down the stairs, she notices something placed in the living room."

    "Bundles of presents lay atop of the table, a single letter on the far edge in the middle."

    ap "To our dearest (son) daughter, Happy Birthday! We got you souvenirs from our trip and also got the other stuff you wanted."

    ap "We’re sorry we won’t be with you in the morning. We still have things to settle, but we promise we’ll be on time for your birthday celebration. We wish you all the best."

    "She stared longer at the end of the note."

    a "…hugs and kisses, huh? Easier said than done."

    "She placed the letter back to where she found it and went back to her room."

    # timeskip to party

    scene bg party with fade

    "As the host of the party, Ali greeted her guests at the entrance. All were wishing her a wonderful birthday."

    "It was already past the agreed time, so she asked their secretary about her parents' whereabouts."

    s "Nothing to worry about, Young Master. Master and Madam are already on their way."

    ag "The happiest of birthdays, my dear grandson!"

    "Ali’s grandmother immediately approached her when she stepped into the venue. Giving Ali a hug, she praises all the accomplishments Ali has received."

    ag "I heard about your recent contest, and I am proud of you for winning 1st place yet again."

    "Ali hid her awkwardness and unease with a smile. Expecting the things her grandmother would talk about, she tries to excuse herself."

    a "Thank you for the congratulations, Grandmother. However, I do have to excuse myself for I have more guests to attend to—"

    ag "Nonsense! We still have so much to talk about. Leave it to those lowly beings, we hired them for a reason."

    "She dragged Ali away from the entrance and closer to the middle of the hall."

    ag "As expected of my grandson, getting 1st place is such an easy effort for a genius like you. Unlike your cousin, that is."

    "She let out a frustrated sigh."

    ag "Another failure born into this family—like father, like son. If only he could be as wonderful as you. Such a disappointment."

    "Ali stared at her with a blank expression, although her insides were burning with fury."

    "Her grandmother caressed Ali’s cheek, with such gentleness one could fall for—if not for her well-known personality."

    ag "However, as the heir, you mustn't disappoint your parents or me. The company falls into your hands."

    ag "You, child, are your parents' treasure; my treasure."

    af "And so he is, Mother."

    "Ali’s father suddenly joined the conversation, his wife beside her. They continued to talk and brag about Ali’s achievements to the point it made her uncomfortable."

    "For her father to skip his greetings to his own child and rather boast to everyone, Ali felt out of place."

    a "Now that you’re here, Father, I must take my leave. I still have guests to welcome."

    a "I hope you keep Grandmother busy. I shall excuse myself."

    am "Very well, my dear."

    "Ali turned her back and felt her chest tighten. It seems like this year’s was the worst celebration out of them all."

    scene blackscreen with fade

    call alieyes1

    return
