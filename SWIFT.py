import math
try:
    idesign = 0
    numberdesign = 7
    while idesign < numberdesign + 1:
        idesign = idesign + 1
        print("_SWIFT_" * idesign)
    print("hi i am SWIFT your personal artificial intelligence")
    name = input('to get the best experience please tell me your name\nNAME:')
    print(f"hi {name}, now i am ready to operate there are a lot of things"
          f"that i can do to have a look at all of them enter 'help'")
    ifhelp = input("do you need any help?>")
    if ifhelp.upper() == "HELP":
        print("""
        1) count to 'n' numbers
        2) ask about my creator
        3) ask about the digits of pi
        4)say hi 
        5) ask about monument 'the stonehenge' 
        6)convert into emoji
        7)Play Duke
        8)Play Guess game 
               """)
    else:
        print("to start enter in the arrowhead below")
    command: str = input("to start press enter to exit type 'exit ")
    while command.upper() != "EXIT":
        cmd = input(">>").upper()
        print(f"input = <{cmd}>\n ")
        if cmd == "WHAT IS THE VALUE OF PI":
            print(f"the value of pi is approximately {math.pi}")
        if cmd == "WHO IS YOUR CREATOR":
            print("i was created by a man called Bakul Takthar who is a \n"
                  "nexus being he created me by writing some fancy lines of \n"
                  "code on his computer")
        if cmd == "COUNT TO A NUMBER":
            no = int(input("what is your number>>"))
            for nom in range(no + 1):
                print(nom)
        if cmd == "CONVERT INTO EMOJI":
            print("enter your sentence below")
            message = input(">>")
            words = message.split(" ")
            emojis = {
                ":)": "😊",
                ":(": "😭",
                ";)": "😉"
            }
            output = ""
            for word in words:
                output += emojis.get(word, word) + " "
            print(output)
        if cmd == "LAUNCH DUKE":
            print("""
            XXXXXX          XX            XX     XX           XX        XXXXXXXX
            XX          XX     XX            XX     XX     XX X           XX
            XX          XX     XX            XX     XXXX                   XXXXXXXX
            XX          XX     XX            XX     XX     XXX           XX
            XXXXXX               XXXXX          XX           XX       XXXXXXXX
            """)
            cmduke = input("to start press enter to exit press U >>")
            print("hi welcome to duke the best car game")
            name2 = name
            print(f"your name is {name}")
            print("to get familiar with controls type 'help' or 'HELP' ")
            print(f"there are a heck a lot of things you can do with your car{name}"
                  f" lets "
                  f"get going")
            while cmduke.upper != "U":
                started = False
                command = str(input("DUKE play> ")).upper()
                if command.upper() == 'HELP':
                    print('''
                to enter the car press f 
                 to leave the car press f again
                 to start the car press e
                 to stop the car press q
                 to move forward press w
                 to move backwards press s
                 to turn right press d 
                to turn left press a
                to quit the game press u''')
                inside_car = False
                if str(command.upper()) == "F":
                    if inside_car:
                        print("left the car")
                        inside_car = False
                    else:
                        print("entered the car")
                        inside_car = True
                if str(command.upper()) == "W":
                    print("moved forward")
                if str(command.upper()) == "S":
                    print("moved backwards")
                if str(command.upper()) == "E":
                    if started:
                        print("car already started")
                    else:
                        print("started the car")
                        started = True
                if str(command.upper()) == "D":
                    print("turned right")
                if str(command.upper()) == "L":
                    print("turned left")
                if command.upper() == "Q":
                    if started:
                        print("car stopped")
                        started = False
                    else:
                        print("car already stopped")
                if str(command.upper()) == "A":
                    print("turned left")
                if str(command.upper()) == "U":
                    print("exited the game")
                    break
        if cmd == "PLAY GUESS GAME":
            print("to start press G to leave press U")
            start_guessing = input("GUESS game>>")
            if start_guessing == "U":
                print("left")
            else:
                print("""
                game started 
                rules
                
                1) you only get 3 tries 
                2)if you fail to guess the correct  number all three times you 
                fail
                3)the correct number will be displayed after the game has 
                ended
                """)
            secret_number = 7
            guess_count = 0
            guess_limit = 3
            try:
                while guess_count < guess_limit:
                    guess = int(input('GUESS:'))
                    guess_count += 1
                    if guess == secret_number:
                        print('YOU WON!')
                        break
                    else:
                        print("you failed\n the correct number was 7")

            except ValueError:
                print("invalid input")
        if cmd == "bye":
            break
        if cmd == "what is the stonehenge":
            print(
                '''the stonehenge is an ancient monument having large 
            stones placed in a circular shape each stone of the 
            monument is super heavy and it remains a mystery till now
            how the stones were placed there the monument is 
            perfectly alligned to show the first sunrise of summer solstice''')
        if cmd == "bye":
            print("bye for now but not for long")
            break
except ValueError:
    print("input should be in words")