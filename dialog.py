# testi dialog treetä varten jos npc jne..
import textwrap

def wrap(text):
    print(textwrap.fill(text, 80))

def talkShaman(herbs):
    potion = False

    wrap("Shaman: \"Hello stranger.\"")
    if not herbs:
        while True:
            while True:
                wrap("a) Who are you?")
                wrap("b) Do you know who I am?")
                wrap("q) I should go now.")
                answer = input()
                answer = answer.lower()
                if answer in ['a', 'b', 'q', 'quit']:
                    break
            if answer == 'a':
                wrap("Shaman: \"I am a shaman.\"")
                print("")
            if answer == 'b':
                wrap("Shaman: \"No but I have something that may help you remember. Just gather me some herbs and I'll make you the potion of endless memory.\"")
                print("")
            if answer in ['q', 'quit']:
                break
        return potion
    else:
        while True:
            while True:
                wrap("a) Who are you?")
                wrap("b) Do you know who I am?")
                wrap("c) I have some herbs.")
                wrap("q) I should go now.")
                answer = input()
                answer = answer.lower()
                if answer in ['a', 'b', 'c', 'q', 'quit']:
                    break
            if answer == 'a':
                wrap("Shaman: \"I am a shaman.\"")
                print("")
            if answer == 'b':
                wrap("Shaman: \"No but I have something that may help you remember. Just gather me some herbs and I'll make you the potion of endless memory.\"")
                print("")
            if answer == 'c':
                wrap("Shaman: \"Here is a potion made from the herbs\"")
                print("")
                potion = True
                break
            if answer in ['q', 'quit']:
                break
    return potion

def talkBarkeeper(banana):
    tap = False

    wrap("Barkeeper: \"Hello. Do you have banana. I could trade one for a wooden tap.\"")
    while True:
        while True:
            wrap("a) No.")
            if banana:
                wrap("b) Yes.")
            wrap("q) I should go now")
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'q', 'quit']:
                break
            if banana and answer == 'b':
                break
        if answer == 'a':
            wrap("Too bad. I need one.")
            print("")
            break
        if answer == 'b':
            wrap("Thank you! Here is your wooden tap.")
            print("")
            tap = True
            break
        if answer in ['q', 'quit']:
            break
    return tap

def talkTrader(memorypotiondrank):
    mushroom = False
    while True:
        while True:
            wrap("Mushroom trader: \"Hello. Do you want to trade with me?\"")
            wrap("a) Yes.")
            wrap("b) No.")
            if memorypotiondrank:
                wrap("c) No. But do you know the wizard living in the castle?")
            wrap("q) I should go now.")
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'b', 'q', 'quit']:
                break
            if memorypotiondrank and answer == "c":
                break
        if answer == 'a':
            wrap("Mushroom trader: \"Too bad I don't have anything to trade.\"")
            print("")
        if answer == 'b':
            wrap("Mushroom trader: \"Well. Let's trade some other time then.\"")
            print("")
        if answer == 'c':
            wrap("Mushroom trader: \"Yes. I hate him for turning my goods into mud. Here is some magic mushroom.\"")
            print("")
            mushroom = True
            break
        if answer in ['q', 'quit']:
            break
    return mushroom
