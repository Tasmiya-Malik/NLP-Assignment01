from nltk.chat.util import Chat, reflections
 
pairs = (
    (
        r"I need (.*)",
        (
            # "Why do you need %1?",
            "Ap ko %1 kun chahiye?",
            # "Would it really help you to get %1?",
            "Agar apko %1 miljaye to kia ap behtar mehsoos krenge?",
            # "Are you sure you need %1?",
            "Apko yaqeen hai k apko %1 chahiye?",
        ),
    ),
    (
        r"Why don\'t you (.*)",
        (
            # "Do you really think I don't %1?",
            "Ap ko waqai lagta hai k main %1 nhi krti?",
            # "Perhaps eventually I will %1.",
            "Kia pta, main shayad waqai %1 krlon",
            # "Do you really want me to %1?",
            "Ap waqai chahte hain ke main %1 krlon",
        ),
    ),
    (
        r"Why can\'t I (.*)",
        (
            # "Do you think you should be able to %1?",
            "Ap ko lagta hai ke apko %1 krna chahiye?",
            # "If you could %1, what would you do?",
            "Agar ap %1 krskte hote to phr ap kia krte?",
            # "I don't know -- why can't you %1?",
            "Mujhe nhi maloom -- ap %1 kun nhi krste?",
            # "Have you really tried?",
            "Kia apne waqai koshish ki hai?",
        ),
    ),
    (
        r"I can\'t (.*)",
        (
            # "How do you know you can't %1?",
            "Ap ko kese pta ke ap %1 nhi krskte?",
            # "Perhaps you could %1 if you tried.",
            "Shayad ap %1 krsken agr ap koshish kren to.",
            # "What would it take for you to %1?",
            "Apko %1 krne k liye kis cheez ki zarorat hogi?",
        ),
    ),
    (
        r"I am (.*)",
        (
            # "Did you come to me because you are %1?",
            "Kia ap mere pas isliye aye hain kun k ap %1 hain?",
            # "How long have you been %1?",
            "Ap kitne arse se %1 hain?",
            # "How do you feel about being %1?",
            "Apko %1 hone pe kesa mehsoos hota hai?",
        ),
    ),
    (
        r"I\'m (.*)",
        (
            # "How does being %1 make you feel?",
            "%1 hone se apko kesa mehsoos hota hai?",
            # "Do you enjoy being %1?",
            "Apko %1 hone se maza ata hai?",
            # "Why do you tell me you're %1?",
            "Ap mujhe kun bta rhe hain k ap %1 hain?",
            # "Why do you think you're %1?",
            "Apko esa kun lagta hai k ap %1 hain?",
        ),
    ),
    (
        r"Are you (.*)",
        (
            # "Why does it matter whether I am %1?",
            "Isse kia farq parrta hai k main %1 hoon ya nahi?",
            # "Would you prefer it if I were not %1?",
            "Kia apko lagta hai k mujhe %1 hona chahiye?",
            # "Perhaps you believe I am %1.",
            "Shayad apko yeh lagta hai k main %1 hoon.",
            # "I may be %1 -- what do you think?",
            "Main shayad %1 hoon -- apko kia lagta hai?",
        ),
    ),
    (
        r"What (.*)",
        (
            # "Why do you ask?",
            "Ap yeh kun pooch rhe hain?",
            # "How would an answer to that help you?",
            "Is ka jawab apki madad kese krega?",
            # "What do you think?",
            "Apko kia lagta hai?",
        ),
    ),
    (
        r"How (.*)",
        (
            # "How do you suppose?",
            "Kese? Ap btayen.",
            # "Perhaps you can answer your own question.",
            "Shayad ap apne jawab ka khud jawab deskte hain.",
            # "What is it you're really asking?",
            "Ap poochna kia chah rhe hain?",
        ),
    ),
    (
        r"Because (.*)",
        (
            # "Is that the real reason?",
            "Kia yeh asal waja hai?",
            # "What other reasons come to mind?",
            "Ap ke zehen main aur konsi wajoohat arhi hain?",
            # "Does that reason apply to anything else?",
            "Kia yeh baat kisi aur cheez pe amaldaramad hoti hai?",
            # "If %1, what else must be true?",
            "Agar esa hai, to iske ilawa aur konsi baat sach hoskti hai?",
        ),
    ),
    (
        r"(.*) sorry (.*)",
        (
            # "There are many times when no apology is needed.",
            "Bohot dafa apko mazrat krne ki zarorat nhi hoti hai.",
            # "What feelings do you have when you apologize?",
            "Apki mazrat krte waqt kia tassurat hote hain?",
        ),
    ),
    (
        r"Hello(.*)",
        (
            # "Hello... I'm glad you could drop by today.",
            "Hello... Mujhe apko yahan dekh kr accha laga.",
            # "Hi there... how are you today?",
            "Hi there... aj ap kese hain?",
            # "Hello, how are you feeling today?",
            "Hello, ap ap kesa mehsoos kr rhe hain?",
        ),
    ),
    (
        r"I think (.*)",
        (
            # "Do you doubt %1?", "Do you really think so?", "But you're not sure %1?"
            "Kia apko %1 pe tashweesh hai?", "Kia apko waqai lagta hai?", "Lekin ap ko %1 pe yaqeen nhi hai?"
        ),
    ),
    (
        r"(.*) friend (.*)",
        (
            # "Tell me more about your friends.",
            "Ap mujhe apne doston k baare main aur btayen.",
            # "When you think of a friend, what comes to mind?",
            "Jab ap aik dost ka sochte hain to apke zehen main kia ata hai?",
            # "Why don't you tell me about a childhood friend?",
            "Ap mujhe bachpan k doston k baare main aur kun nhi btate?",
        ),
    ),
    (
        r"Yes", 
        (
            # "You seem quite sure.", "OK, but can you elaborate a bit?"
            "Ap kafi puretmad lagte hain.",
            "Theek hai, lekin ap thora aur btayenge?",
        )
    ),
    (
        r"(.*) computer(.*)",
        (
            # "Are you really talking about me?",
            "Kia ap waqai mere baare main baat kr rhe hain?",
            # "Does it seem strange to talk to a computer?",
            "Kia aik computer se baat krte hoye ajeeb mehsoos nhi hota?",
            # "How do computers make you feel?",
            "Ap ke computers ke hawale se kia khayalat hain?",
            # "Do you feel threatened by computers?",
            "Kia apko computers se khatra mehsoos hota hai?",
        ),
    ),
    (
        r"Is it (.*)",
        (
            # "Do you think it is %1?",
            "Ap ko %1 lagta hai?",
            # "Perhaps it's %1 -- what do you think?",
            "Shayad %1 hi hai -- ap ko kia lagta hai?",
            # "If it were %1, what would you do?",
            "Agr %1 hai, to ap kia krenge?",
            # "It could well be that %1.",
            "Hoskta hai hai ke %1 hi ho.",
        ),
    ),
    (
        r"It is (.*)",
        (
            # "You seem very certain.",
            "Ap kafi puretmaad lagte hain.",
            # "If I told you that it probably isn't %1, what would you feel?",
            "Agr main kahon ke %1 nhi hai, to apko kesa mehsoos hogay?",
        ),
    ),
    (
        r"Can you (.*)",
        (
            # "What makes you think I can't %1?",
            "Ap ko esa kun lagta hai k main %1 nhi krskti?",
            # "If I could %1, then what?",
            "Agr main %1 krskti, to phr?",
            # "Why do you ask if I can %1?",
            "Ap esa kun pooch rhe hain ke main %1 krskti hoon ya nhi?",
        ),
    ),
    (
        r"Can I (.*)",
        (
            # "Perhaps you don't want to %1.",
            "Shayad ap %1 krna nhi chahte.",
            # "Do you want to be able to %1?",
            "Kia ap waqai %1 krna chahte hain?",
            # "If you could %1, would you?",
            "Agr ap %1 krskte to ap kia krte?",
        ),
    ),
    (
        r"You are (.*)",
        (
            # "Why do you think I am %1?",
            "Ap ko esa kun lagta hai ke main %1 hoon?",
            # "Does it please you to think that I'm %1?",
            "Kia apko yeh soch kr khushi horhi hai ke main %1 hoon?",
            # "Perhaps you would like me to be %1.",
            "Shayad ap chahte hain k main %1 banjaon.",
            # "Perhaps you're really talking about yourself?",
            "Shayad ap apne baare main baat kr rhe hain?",
        ),
    ),
    (
        r"You\'re (.*)",
        (
            # "Why do you say I am %1?",
            "Ap ko esa kun lagta hai ke main %1 hoon?",
            # "Why do you think I am %1?",
            "Ap ko esa kun kun lagta hai ke main %1 hoon?",
            # "Are we talking about you, or me?",
            "Hum kis ki baat kr rhe hain? Ap ki ya meri?",
        ),
    ),
    (
        r"I don\'t (.*)",
        # ("Don't you really %1?", "Why don't you %1?", "Do you want to %1?"),
        ("Kia ap waqai %1 nhi krte?", "Ap %1 kun nhi krte?", "Kia ap %1 krna chahte hain?"),
    ),
    (
        r"I feel (.*)",
        (
            # "Good, tell me more about these feelings.",
            "Shabash, mujhe apne ehsasat ke baare main aur btayen.",
            # "Do you often feel %1?",
            "Kia ap aksar %1 mehsoos krte hain?",
            # "When do you usually feel %1?",
            "Ap %1 ziada kab mehsoos krte hain?",
            # "When you feel %1, what do you do?",
            "Jab ap %1 mehsoos krte hain, to ap kia krte hain?",
        ),
    ),
    (
        r"I have (.*)",
        (
            # "Why do you tell me that you've %1?",
            "Ap mujhe yeh kun bta rhe hain?"
            # "Have you really %1?",
            "Kia ap ne waqai %1 kia hai?",
            # "Now that you have %1, what will you do next?",
            "Ab jab ap ne %1 krlia hai, ap aage kia krenge?",
        ),
    ),
    (
        r"I would (.*)",
        (
            # "Could you explain why you would %1?",
            "Ap bta skte hain k ap ne %1 kun kia?",
            # "Why would you %1?",
            "Ap ne %1 kun kia?",
            # "Who else knows that you would %1?",
            "Aur kise maloom hai k ap ne %1 kia hai?",
        ),
    ),
    (
        r"Is there (.*)",
        (
            # "Do you think there is %1?",
            "Kia apko lagta hai k %1 hai?",
            # "It's likely that there is %1.",
            "Esa hai k %1 ho.",
            # "Would you like there to be %1?",
            "Kia ap chahte hain ke %1 ho?",
        ),
    ),
    (
        r"My (.*)",
        (
            "I see, your %1.",
            "Why do you say that your %1?",
            "When your %1, how do you feel?",
        ),
    ),
    (
        r"You (.*)",
        (
            # "We should be discussing you, not me.",
            "Humain apke baare main baat krni chahiye, naake mere.",
            # "Why do you say that about me?",
            "Ap mere baare main esa kun keh rhe hain?",
            # "Why do you care whether I %1?",
            "Ap ko kia farq parrta hai k main %1 hoon ya nhi.",
        ),
    ),
    (r"Why (.*)", 
    #  ("Why don't you tell me the reason why %1?", "Why do you think %1?")
        ("Ap mujhe %1 waja btayen?", "Ap ko %1 kun lagta hai?")
    
    ),
    (
        r"I want (.*)",
        (
            # "What would it mean to you if you got %1?",
            "Ap ke liye %1 ki kitni ehmiyat hai?",
            # "Why do you want %1?",
            "Ap %1 kun hasil krna chahte hain?",
            # "What would you do if you got %1?",
            "Agr apko %1 miljaye to ap kia krenge?",
            # "If you got %1, then what would you do?",
        ),
    ),
    (
        r"(.*) mother(.*)",
        (
            # "Tell me more about your mother.",
            "Apni walida ke baare main mujhe aur btayen",
            # "What was your relationship with your mother like?",
            "Apke apni walida se kese talluqat the?",
            # "How do you feel about your mother?",
            "Ap apni walida ke liye kesa mehsoos krte hain?",
            # "How does this relate to your feelings today?",
            "Yeh ap ke ehsasat se kese munasbat rakhta hai?",
            # "Good family relations are important.",
            "Ghar walon se acche talluqat bohot zarori hote hain.",
        ),
    ),
    (
        r"(.*) father(.*)",
        (
            # "Tell me more about your father.",
            "Apne walid k baare main mujhe aur btayen.",
            # "How did your father make you feel?",
            "Ap ke walid apko ke sath kese rehte the?",
            # "How do you feel about your father?",
            "Ap apne walid k baare main kesa mehsoos krte hain?",
            # "Does your relationship with your father relate to your feelings today?",
            "Kia apke aur walid ke talluqat apke mojooda esasat se kese munasbat rakhte hain?",
            # "Do you have trouble showing affection with your family?",
            "Kia apko apne ghr walo ko apni muhabbat ka ehsas dilane main dikkat hoti hai?",
        ),
    ),
    (
        r"(.*) child(.*)",
        (
            # "Did you have close friends as a child?",
            "Kia bachpan main apke koi qareebi dost the?",
            # "What is your favorite childhood memory?",
            "Apke bachpan ki koi yaadgar baat btayen.",
            # "Do you remember any dreams or nightmares from childhood?",
            "Kia apko apne bachpan se koi accha ya bura khuwab yaad hai?",
            # "Did the other children sometimes tease you?",
            "Kia doosre bachey apko tang kia krte the?",
            # "How do you think your childhood experiences relate to your feelings today?",
            "Apko lagta hai k apke bachpan ke tajurbe apke haal se koi munasbat rakhte hain?",
        ),
    ),
    (
        r"(.*)\?",
        (
            # "Why do you ask that?",
            "Ap yeh kun pooch rhe hain?",
            # "Please consider whether you can answer your own question.",
            "Mera mashwara hoga ke ap is sawal ka jawab khud dene ki koshish kren.",
            # "Perhaps the answer lies within yourself?",
            "Shayad is ka jawab apke andar kahin chupa ho?",
            # "Why don't you tell me?",
            "Ap mujhe kun nhi btate k iska jawab kia hona chahiye?",
        ),
    ),
    (
        r"quit",
        (
            # "Thank you for talking with me.",
            "Mujhse baat krne ka shukria.",
            # "Good-bye.",
            "Khuda Hafiz",
            # "Thank you, that will be $150.  Have a good day!",
            "Shukria, ap $150 ada krdijiyega. Khuda Hafiz!",
        ),
    ),
    (
        r"(.*)",
        (
            "Please tell me more.",
            "Let's change focus a bit... Tell me about your family.",
            "Can you elaborate on that?",
            "Why do you say that %1?",
            "I see.",
            "Very interesting.",
            "%1.",
            "I see.  And what does that tell you?",
            "How does that make you feel?",
            "How do you feel when you say that?",
        ),
    ),
)

eliza_chatbot = Chat(pairs, reflections)


def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print("=" * 72)
    print("Hello.  How are you feeling today?")

    eliza_chatbot.converse()

def demo():
    eliza_chat()

if __name__ == "__main__":
    demo()