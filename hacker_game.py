import time
import random
stars = 2
print("===================================")
print("        HACKER TERMINAL GAME V2      ")
print("===================================")

# =========================
# ACCOUNT SYSTEM
# =========================
wrongans = 0
userpass = input("Login or Create new account: ").lower()

while userpass not in ["login", "create", "create account", "create new account"]:
    print("Invalid reply")
    userpass = input("Login or Create new account: ").lower()

name = ""
username = ""
password = ""

if userpass == "login":
    name = input("What is your name - ")
    username = input("Username - ")
    password = input("Password - ")
    print("ACCESS GRANTED")
else:
    print("Create your account")
    name = input("What is your name - ")
    username = input("Username - ")

    while True:
        password = input("Password (min 8 chars, 1 number) - ")

        if len(password) < 8:
            print("Too short!")
            continue

        has_number = False
        for n in "0123456789":
            if n in password:
                has_number = True

        if not has_number:
            print("Must include a number!")
        else:
            print("Account created!")
            break

# =========================
# GAME VARIABLES
# =========================

money = 0
de = False
num123 = 0  # FIX: prevents NameError

print("\nYou are an undercover hacker.")
print("Make money by hacking systems.\n")

# =========================
# MAIN LOOP
# =========================

while True:
    print("==============================")
    print("Money: $", money)
    print("Double Earnings:", de)
    print("Options: CALL | BUY | MISSION | QUIT")
    if wrongans >= 100:
        wrongstar = 5
    elif wrongans >= 50:
        wrongstar = 4
    elif wrongans >= 25:
        wrongstar = 3
    elif wrongans >= 10:
        wrongstar = 2
    elif wrongans >= 5:
        wrongstar = 1
    else:
        wrongstar = 0

    if money >= 10000:
        moneystar = 5
    elif money >= 5000:
        moneystar = 4
    elif money >= 3500:
        moneystar = 3
    elif money >= 1000:
        moneystar = 2
    elif money >= 500:
        moneystar = 1
    else:
        moneystar = 0

    stars = max(wrongstar, moneystar)

    if stars == 1:
        print("Bounty is ★")
    if stars == 2:
        print("Bounty is ★★")
    if stars == 3:
        print("Bounty is ★★★")
    if stars == 4:
        print("Bounty is ★★★★")
    if stars == 5:
        print("Bounty is ★★★★★")
    print("==============================")

    response = input("What do you want to do? ").lower()

    # =========================
    # CALL SYSTEM
    # =========================
    if response == "call":
        print("\nCalling...\n")
        print("Say your name")

        who = input("Who is this? ").lower()

        if who == name.lower():
            if stars == 0:
                num123 = random.randint(1, 4)
            if stars == 1:
                num123 = random.randint(1, 5)
            if stars == 2 or stars == 3:
                num123 = random.randint(1, 6)
            if stars == 4:
                num123 = random.randint(1, 7)
            if stars == 5:
                num123 = random.randint(1, 8)
            else:
                num123 = random.randint(1, 5)

            # ================= VIRGIN MEDIA =================
            if num123 == 1:
                print("You are a Virgin Media employee")

                reason = input("Why are you calling? ").lower()

                if "internet" in reason or "virgin" in reason or "media" in reason:
                    print("They trust you.")

                    code = random.randint(100000, 999999)
                    print("Ask them for a code")

                    ask = input("What do you say? ").lower()

                    if any(word in ask for word in ["code", "access", "number", "card"]):
                        print("Access code:", code)

                        entered = input("Enter code: ")

                        if entered.isdigit() and int(entered) == code:
                            print("Hack successful!")
                            money += 200 if de else 100
                        else:
                            print("Wrong code!")
                            wrongans = wrongans + 1
                    else:
                        print("They refuse to help")
                        wrongans = wrongans + 1
                else:
                    print("They don't trust your reason")
                    wrongans = wrongans + 1

            # ================= LAWYER =================
            elif num123 == 2:
                print("You are a fake lawyer and you are going in court")

                reason = input("Why are you calling? ").lower()

                if "court" in reason or "money" in reason or "lawyer" in reason:
                    print("They trust you.")

                    code = random.randint(100000, 999999)
                    print("Ask them for a code")

                    ask = input("What do you say? ").lower()

                    if any(word in ask for word in ["code", "access", "number", "card"]):
                        print("Access code:", code)

                        entered = input("Enter code: ")

                        if entered.isdigit() and int(entered) == code:
                            print("Hack successful!")
                            money += 200 if de else 100
                        else:
                            print("Wrong code!")
                            wrongans = wrongans + 1
                    else:
                        print("They refuse to help")
                        wrongans = wrongans + 1
                else:
                    print("They don't trust your reason")
                    wrongans = wrongans + 1

            # ================= BANKER =================
            elif num123 == 3:
                print("You are a fake banker")

                reason = input("Why are you calling? ").lower()

                if "bank" in reason or "money" in reason:
                    print("They trust you.")

                    code = random.randint(100000, 999999)
                    print("Ask them for a code")

                    ask = input("What do you say? ").lower()

                    if any(word in ask for word in ["code", "access", "number", "card"]):
                        print("Access code:", code)

                        entered = input("Enter code: ")

                        if entered.isdigit() and int(entered) == code:
                            print("Hack successful!")
                            money += 200 if de else 100
                        else:
                            print("Wrong code!")
                            wrongans = wrongans + 1
                    else:
                        print("They refuse to help")
                        wrongans = wrongans + 1
                else:
                    print("They don't trust your reason")
                    wrongans = wrongans + 1

            # ================= ARCHITECT =================
            elif num123 == 4:
                print("You are an architect")
                print("Say how their house is weakening")

                reason = input("Why are you calling? ").lower()

                if "architect" in reason or "fragile" in reason or "house" in reason or "weak" in reason:

                    housecode = random.randint(1, 2)

                    if housecode == 1:
                        print("I just bought the house")

                        print("They are suspicious but continue...")

                        reasonhouse = input("Are you lying? ").lower()

                        if "no" in reasonhouse:
                            print("They trust you.")

                            code = random.randint(100000, 999999)
                            print("Ask them for a code")

                            ask = input("What do you say? ").lower()

                            if any(word in ask for word in ["code", "access", "number", "card"]):
                                print("Access code:", code)

                                entered = input("Enter code: ")

                                if entered.isdigit() and int(entered) == code:
                                    print("Hack successful!")
                                    money += 200 if de else 100
                                else:
                                    print("Wrong code!")
                                    wrongans = wrongans + 1
                            else:
                                print("They refuse to help")
                                wrongans = wrongans + 1
                        else:
                            print("They don't trust you")
                            wrongans = wrongans + 1
                    else:
                        print("Call failed. They are suspicious.")
                        wrongans = wrongans + 1
                else:
                    print("They don't trust your reason")
                    wrongans = wrongans + 1

            # ================= SUSPICIOUS GUY (bounty event) =================
            elif num123 == 5:
                yesno = random.randint(1, 2)
                print("Hello how are you")
                print("Say, I need your digital code to see your virtual activities ")
                answer = input("Why are you calling? ").lower()
                if "digital" in answer or "code" in answer or "virtual" in answer or "activity" in answer:
                    print("Something about you doesn't seem right.")
                    print("You called me out of nowhere")
                    print("now you're asking for a verification code?")
                    answer = input("Can if I ask you a few answers? ").lower()
                    if "yes" in answer or "sure" in answer or "go ahead" in answer:
                        pass
                    else:
                        print("Dialing police")
                        wrongans += 2

                    answer = input("Why are you calling me out of nowhere? ").lower()
                    if "verify" in answer or "code" in answer or "digital" in answer or "virtual" in answer:
                        print("Oh... I see.")
                        answer = input("How did you get my phone number? ").lower()
                        answer = ""
                        if "company" in answer or "database" in answer or "business" in answer:
                            print("I see, understood.")

                            answer = input("What if I don't give you my verification code? ").lower()
                        if "have" in answer or "to" in answer or "dont" in answer:
                            if yesno == 1:
                                print("Okay.")

                        else:
                            print("Nice talking to you.")

                        answer = input("Why do you need my verification code? ").lower()
                        if "account" in answer or "owner" in answer or "confirm" in answer:
                            print("Okay, I trust you.")
                            code = random.randint(100000, 999999)
                            print("Access code:", code)
                            entered = input("Enter code: ")
                            if entered == str(code):
                                print("Hack successful!")
                                money += 300 if de else 150
                    else:
                        print("They didn't ask about a verification code.")
                else:
                    print("They don't trust you")
                    wrongans += 2

            # ================= POLICE (bounty event) =================
            elif num123 == 6:
                yesno = random.randint(1, 2)
                if stars == 2:
                    answer = input("999 What’s your emergency?\nExplain that you are a police officer in need of assistance.\n").lower()
                    if "police" in answer or "assistance" in answer or "help" in answer or "officer" in answer:
                        answer = input("Something doesn't seem right...\nMind if I ask you a few answers? ").lower()
                        if "no" in answer or "sure" in answer:
                            pass
                        else:
                            print("")
                            wrongans += 3

                        answer = input("Why are you calling me on the 999 number? ").lower()
                        if "confused" in answer or "quick" in answer or "999" in answer or "random phone" in answer:
                            print("Okay, makes sense.")
                            answer = input("Why not use your radio to communicate? ").lower()
                            if "lost" in answer or "left" in answer or "stolen" in answer:
                                print("I see, understood.")

                                answer = input("And why did you let that happen? ").lower()
                            if "careless" in answer or "mistake" in answer or "cant" in answer:
                                if yesno == 1:
                                    print("Well, don't let it happen again.")

                            else:
                                print("No can do sir, sorry.")

                            answer = input("Why do you need my verification code? ").lower()
                            if "location" in answer or "send" in answer or "assistance" in answer:
                                print("Okay, I believe you.")
                                code = random.randint(100000, 999999)
                                print("Access code:", code)
                                entered = input("Enter code: ")
                                if entered == str(code):
                                    print("Hack successful!")
                                    money += 400 if de else 200
                        else:
                            print("They don't trust you")
                    else:
                        print("They don't trust you")
                        wrongans += 3
                else:
                    answer = input("999 What’s your emergency?\nExplain that you are a police officer in need of assistance.\n").lower()
                    if "police" in answer or "assistance" in answer or "help" in answer or "officer" in answer:
                        answer = input("Something doesn't seem right...\nMind if I ask you a few answers? ").lower()
                        if "no" in answer or "sure" in answer:
                            pass
                        else:
                            print("")
                            wrongans += 3

                        answer = input("Why are you calling me on the 999 number? ").lower()
                        if "confused" in answer or "quick" in answer or "999" in answer or "random phone" in answer:
                            print("Okay, makes sense.")
                            answer = input("Why not use your radio to communicate? ").lower()
                            if "lost" in answer or "left" in answer or "stolen" in answer:
                                print("I see, understood.")
                                authority_number = random.radint(100, 999)
                                print("Your badge number is", authority_number)
                                answer = input("An officer wouldn't let that happen, whats your badge number?").lower()
                            if answer == authority_number:
                                if yesno == 1:
                                    print("So you are a real police officer, I will let you off the hook this time.")

                            else:
                                print("No can do sir, sorry.")

                            answer = input("Why do you need my verification code? ").lower()
                            if "location" in answer or "send" in answer or "assistance" in answer:
                                print("Okay, I believe you.")
                                code = random.randint(100000, 999999)
                                print("Access code:", code)
                                entered = input("Enter code: ")
                                if entered == str(code):
                                    print("Hack successful!")
                                    money += 400 if de else 200
                        else:
                            print("They don't trust you")
                    else:
                        print("They don't trust you")
                        wrongans += 5

            # ================= SECRET SERVICES (bounty event) =================
            elif num123 == 7:
                yesno = random.randint(1, 2)
                answer = input("Secret Services here, what may you need?\n(Ask about a code)\n ").lower()
                if "code" in answer:
                    print("Something about you doesn't seem right.")
                    answer = input("What do you need the code for? ").lower()
                    if "check" in answer or "safe" in answer:
                        pass
                    else:
                        print("Dialing police")
                        wrongans += 7

                    authority_number = random.radint(1000000, 1000000000)
                    print("Your number is", authority_number)
                    answer = input("Ah, I see... Can we still trust you? What is your number? ").lower()
                    if answer == authority_number:

                        print("That checks out.")
                        answer = input("Just to confirm, may you state that again? ").lower()

                        if answer == authority_number:
                            print("All clear.")

                            answer = input("Why do you need the code again? ").lower()
                        if "check" in answer or "safe" in answer:
                            if yesno == 1:
                                print("Alright.")

                        else:
                            print("Sorry sir, no can do.")

                        answer = input("How will you make sure of it? ").lower()
                        if "protect" in answer:
                            print("Okay, I trust you.")
                            code = random.randint(100000, 999999)
                            print("Access code:", code)
                            entered = input("Enter code: ")
                            if entered == str(code):
                                print("Hack successful!")
                                money += 500 if de else 250
                    else:
                        print("They don't trust you")
                else:
                    print("They don't trust you")
                    wrongans += 7

            # ================= FBI (bounty event) =================
            elif num123 == 8:
                yesno = random.randint(1, 3)
                answer = input("FBI here wai- WHO ARE YOU!\n ").lower()
                if "code" in answer:
                    print("Something doesn't seem right here.")
                    answer = input("HOW DID YOU GET OUR NUMBER? ").lower()
                    if "FBI" in answer or "force" in answer or "work" in answer:
                        pass
                    else:
                        print("LIAR!")
                        wrongans += 10

                    authority_number = random.radint(1000000000000, 1000000000000000000000)
                    print("Your number is", authority_number)
                    answer = input("Ah, I see... Can we still trust you? What is your number? ").lower()
                    if answer == authority_number:
                        print("That checks out.")
                        answer = input("Just to confirm, may you state that again? ").lower()

                        if answer == authority_number:
                            print("All clear.")

                            answer = input("What do you need from us? ").lower()
                        if "code" in answer:
                            if yesno == 1:
                                print("THE CODE?!?!?")

                        else:
                            print("Sorry sir, no can do.")

                        answer = input("WHAT DO YOU NEED THE CODE FOR? ").lower()
                        if "information" in answer or "secure" in answer or "duty" in answer or "job" in answer:
                            print("Okay, I trust you.")
                            code = random.randint(100000, 999999)
                            print("Access code:", code)
                            entered = input("Enter code: ")
                            if entered == str(code):
                                print("Hack successful!")
                                money += 1000 if de else 500
                    else:
                        print("They don't trust you")
                else:
                    print("They don't trust you")
                    wrongans += 10

        else:
            print("They don't trust you")
            wrongans += 2

    # =========================
    # SHOP
    # =========================
    elif response == "buy":
        print("\n===== SHOP =====")
        print("Double Earnings - $150")

        if de:
            print("Already owned")
        elif money < 150:
            print("Not enough money")
        else:
            choice = input("BUY or PASS: ").lower()

            if choice == "buy":
                money -= 150
                de = True
                print("Double earnings activated!")
            else:
                print("Cancelled")
    # =========================
    # MISSION
    #==========================
    elif response == "mission":
        if stars == 1:
            print("==========MISSION==========")
            print("tip: Press [ENTER] to proceed:")
            print("MISSION BRIEF")
            input("A small technology company has contacted your agency.")
            input("One of their employees left a company laptop on a train.")
            input("The laptop has now been found, but it is locked and the employee forgot the password.")
            input("The company has given you full permission to recover the important work files.")
            input("Your mission is to safely access the laptop and recover the documents.")
            input("before the automatic file cleanup starts.")
            print("Connecting to Recovery Terminal...")
            print("Connection Established.")
            print("Scanning Device...")
            time.sleep(2)
            print("[#] 10%")
            time.sleep(1.6)
            print("[##] 20%")
            time.sleep(2)
            print("[###] 30%")
            time.sleep(1)
            print("[#####] 50%")
            time.sleep(1)
            print("[#######] 70%")
            time.sleep(1)
            print("[#########] 99%")
            time.sleep(5)
            print("[#########] 100%")

            print("Device Found")
            time.sleep(1)
            print("Status: Online")
            time.sleep(1)
            print("Encryption: Active")
            time.sleep(1)
            print("Permission Token: Verified")

            print("Director:")
            print("Good work. The company has authorised this recovery so....")
            print("Everything you do is legal.")

            time.sleep(1)

            print("Initializing Recovery Module...")
            print("Loading...")
            print("Loading...")
            print("Ready.")

            input("Press ENTER to begin...")


            while True:

                print("\nChoose where to search.")
                print("1. Games")
                print("2. Work Documents")
                print("3. Music")
                print("4. Exit")

                choice = input("Enter your choice: ").lower()


                if choice in ["1", "games"]:

                    print("Opening Game - 1")

                    print("===================================")
                    print("      PASSWORD CRACKER")
                    print("===================================")

                    password = random.randint(1000,9999)

                    print("Guess the 4-digit password.")
                    print("You have 15 attempts.\n")

                    attempts = 15

                    while attempts > 0:

                        guess = int(input("Enter password: "))

                        if guess == password:
                            print("\n✅ ACCESS GRANTED!")
                            print("+$250")
                            money += 250
                            break

                        elif guess < password:
                            print("⬆️ Too low!")

                        else:
                            print("⬇️ Too high!")

                        attempts -= 1
                        print("Attempts remaining:", attempts)


                    if attempts == 0:
                        print("\n❌ ACCESS DENIED!")
                        print("The password was", password)


                    input("\nPress ENTER to return to the menu...")


                elif choice in ["2","work documents","documents"]:

                    print("===================================")
                    print("      WORK DOCUMENT RECOVERY")
                    print("===================================")

                    input("Director: ")

                    print("The employee stored several important company files here.")
                    time.sleep(2)

                    print("Some of the files have been encrypted after the laptop was lost.")
                    time.sleep(2)

                    print("We have the legal recovery key...")
                    time.sleep(2)

                    print("...but we need you to verify it.")

                    input("Press ENTER to continue...")


                    print("Scanning folders...")
                    time.sleep(2)

                    print("Finance ✓")
                    time.sleep(1)

                    print("Human Resources ✓")
                    time.sleep(1)

                    print("Engineering ✓")
                    time.sleep(1)

                    print("Confidential Archive FOUND")
                    time.sleep(2)


                    code = random.randint(100,999)

                    print("Generating temporary recovery code...")
                    print("Recovery Code:", code)

                    time.sleep(3)

                    print("\n"*40)

                    answer = input("Enter Recovery Code: ")


                    if answer == str(code):

                        print("Verifying...")
                        time.sleep(2)

                        print("Recovery Key Accepted.")
                        print("Decrypting Archive...")

                        time.sleep(2)

                        print("Recovered Files:")
                        print("- Company_Budget.xlsx")
                        print("- Employee_List.docx")
                        print("- Project_Phoenix.pdf")
                        print("- Client_Contracts.zip")

                        print("We got their weak points")
                        print("To get paid you will need to inform them about this")

                        input("Press enter to write a email")

                        emailwriting = input(
                            "Make it at least 50 words long and make it formal: "
                        )


                        if "incident" in emailwriting.lower() or "problem" in emailwriting.lower():

                            print("Money +200")
                            money += 200

                            if de == True:
                                print("Money +400")
                                money += 400

                        else:

                            while True:

                                rewrite = input("Rewrite it please and talk about the PROBLEM: ")

                                if "incident" in rewrite.lower() or "problem" in rewrite.lower():

                                    print("You got $200")
                                    money += 200
                                    break


                    else:

                        print("Recovery Key Incorrect.")
                        print("Archive Locked.")


                    input("\nPress ENTER to return to the menu...")


                elif choice in ["3","music"]:

                    print("===================================")
                    print("        AUDIO RECOVERY")
                    print("===================================")

                    print("Searching music files...")
                    time.sleep(2)

                    print("Corrupted file found.")
                    time.sleep(1)

                    print("Repairing audio...")
                    time.sleep(3)

                    print("Audio recovered!")

                    input("\nPress ENTER to return to the menu...")


                elif choice in ["4","exit","quit"]:

                    print("Disconnecting...")
                    break


                else:

                    print("Invalid choice.")
        elif stars == 2:
            data_game = True
            print("==========MISSION==========")
            print("tip: Press [ENTER] to proceed:")
            print("MISSION BRIEF")
            input("A small technology company has contacted your agency.")
            input("One of their employees accidently corrupted major files needed to run their business.")
            input("Some files were able to be recovered, yet some weren't.")
            input("The company has given you full permission to their files, yet they have forgotten the password to access the data.")
            input("Your mission is to safely identify the corrupted documents and restore them.")
            input("before the automatic file cleanup starts.")


            print("Connecting to Recovery Terminal...")
            print("Connection Established.")
            print("Scanning Device...")
            time.sleep(2)
            print("[#] 10%")
            time.sleep(1.6)
            print("[##] 20%")
            time.sleep(2)
            print("[###] 30%")
            time.sleep(1)
            print("[#####] 50%")
            time.sleep(1)
            print("[#######] 70%")
            time.sleep(1)
            print("[#########] 99%")
            time.sleep(5)
            print("[#########] 100%")

            print("Device Found")
            time.sleep(1)
            print("Status: Online")
            time.sleep(1)
            print("Encryption: Active")
            time.sleep(1)
            print("Permission Token: Verified")

            print("Director:")
            print("Good work. The company has authorised this recovery so....")
            print("Everything you do is legal.")

            time.sleep(1)

            print("Initializing Recovery Module...")
            print("Loading...")
            print("Loading...")
            print("Ready.")

            input("Press ENTER to begin...")
            year = str(random.randint(1944, 2022))
            attempts = 3


            while True:

                print("\nChoose where to search.")
                print("1. Data")
                print("2. Work Files")
                print("3. Music")
                print("4. Exit")

                choice = input("Enter your choice: ").lower()


                if choice in ["1", "data"]:
                    if data_game:
                        print("Opening Data Login - 1")

                        print("===================================")
                        print("      PASSWORD CRACKER")
                        print("===================================")
                        print("You don't have access to the data yet.")
                        print("Complete the security questions in order to access the data.")
                        print("The company has given you the information needed, yet, in the form of a riddle?\n")
                        if year[0] == "1":
                            roman_year = "MCM"
                        else:
                            roman_year = "MM"
                            
                        if int(year[2]) >= 1 and int(year[2]) <= 3:
                            roman_year += "X" * int(year[2])
                        elif year[2] == "4":
                            roman_year += "XL"
                        elif year[2] == "5":
                            roman_year += "L"
                        elif int(year[2]) >= 6 and int(year[2]) <= 8:
                            roman_year += "L"
                            roman_year += "X" * (int(year[2]) - 5)
                        elif year[2] == "9":
                            roman_year += "XC"

                        if int(year[3]) >= 1 and int(year[3]) <= 3:
                            roman_year += "I" * int(year[3])
                        elif year[3] == "4":
                            roman_year += "IV"
                        elif year[3] == "5":
                            roman_year += "V"
                        elif int(year[3]) >= 6 and int(year[3]) <= 8:
                            roman_year += "V"
                            roman_year += "I" * (int(year[3]) - 5)
                        elif year[3] == "9":
                            roman_year += "IX"

                        sec_questions = input(f"(Our company was founded in the year {roman_year})\nWhat year was this company found in?\n")
                        if sec_questions == year:
                            print("Access Granted")
                            data_game = False
                        else:
                            attempts -= 1
                            print(f"You have {attempts} attempts before you are locked out.")
                            if attempts == 0:
                                input("Press ENTER to return to the menu...")
                    else:
                        print("You have already gained access to the data, try going into the files and the information will show up.")
                        pass


                elif choice in ["2","work documents","documents"]:
                    if data_game == False:
                        user_answer = ""
                        print("===================================")
                        print("      WORK DOCUMENT RECOVERY")
                        print("===================================")

                        input("Director: ")

                        print("Many files were corrupted seemingly out of nowhere.")
                        time.sleep(2)

                        print("We have access to all of these files...")
                        time.sleep(2)

                        print("...but not all were corrupted.")

                        input("Press ENTER to continue...")


                        print("Scanning folders...")
                        time.sleep(2)

                        print("Checking fatal flaws ✓")
                        time.sleep(1)

                        print("Restoring obviously corrupted files ✓")
                        time.sleep(1)

                        print("Failed to check 1 file")
                        time.sleep(1)

                        print("Files located ✓")
                        time.sleep(2)

                        print("Accessing Data...")
                        time.sleep(2)

                        print("\nYour job is to determine if this file is genuine by checking if everything matches up between the data and the file.")
                        time.sleep(2)

                        answer = random.choice(["stable", "corrupted"])
                        date = int(random.randint(1, 25))
                        month = int(random.randint(1, 12))
                        company_password = int(random.randint(100000, 999999))
                        company_id = int(random.randint(1000000000, 9999999999))
                        company_time_hour = int(f"{random.randint(1, 12):02d}")
                        company_time_minute = int(f"{random.randint(1, 60):02d}")
                        print(f"\nData:\nCompany founded in ____ (This must've been corrupted during file transfer)\nDate: {date}/{month}\nPassword: {company_password}\nFile ID: {company_id}\nTime Created: {company_time_hour}:{company_time_minute}")
                        print("\nDocument:")
                        if answer == "stable":
                            pass
                        else:
                            change = int(random.randint(1, 6))
                            if change == 1:
                                date = int(random.randint(1, 25))
                            elif change == 2:
                                month = int(random.randint(1, 12))
                            elif change == 3:
                                company_password = int(random.randint(100000, 999999))
                            elif change == 4:
                                company_id = int(random.randint(1000000000, 9999999999))
                            elif change == 5:
                                company_time_hour = int(f"{random.randint(1, 12):02d}")
                            else:
                                company_time_minute = int(f"{random.randint(1, 60):02d}")

                            print(f"\nData:\nCompany founded in ____\nDate: {date}/{month}\nPassword: {company_password}\nFile ID: {company_id}\nTime Created: {company_time_hour}:{company_time_minute}")
                            user_answer = input("\nIs this file corrupted or stable? ").lower
                        if user_answer == answer:

                            print("Verifying...")
                            time.sleep(2)

                            print("Recovery Key Accepted.")
                            print("Decrypting Archive...")

                            time.sleep(2)

                            print("Recovered Files:")
                            print("- Company_Budget.xlsx")
                            print("- Employee_List.docx")
                            print("- Project_Phoenix.pdf")
                            print("- Client_Contracts.zip")

                            print("We got their weak points")
                            print("To get paid you will need to inform them about this")

                            input("Press ENTER to write a email")

                            emailwriting = input(
                                "Make it at least 50 words long and make it formal: "
                            )


                            if "corrupted" in emailwriting.lower() or "fixed" in emailwriting.lower():

                                print("Money + 200")
                                money += 200

                                if de == True:
                                    print("Money + 300")
                                    money += 300

                            else:

                                while True:

                                    rewrite = input("Rewrite it please and talk about how you checked if the files were CORRUPTED and FIXED them: ")

                                    if "corrupted" in rewrite.lower() or "fixed" in rewrite.lower():

                                        print("You got $300")
                                        money += 300
                                        break


                        else:

                            print("Recovery Key Incorrect.")
                            print("Archive Locked.")


                        input("\nPress ENTER to return to the menu...")
                    else:
                        print("Gain access to the data before going through the files.")

                elif choice in ["3","music"]:

                    print("===================================")
                    print("        AUDIO RECOVERY")
                    print("===================================")

                    print("Searching music files...")
                    time.sleep(2)

                    print("Corrupted file found.")
                    time.sleep(1)

                    print("Repairing audio...")
                    time.sleep(3)

                    print("Audio recovered!")

                    input("\nPress ENTER to return to the menu...")


                elif choice in ["4","exit","quit"]:

                    print("Disconnecting...")


                else:

                    print("Invalid choice.")
        elif stars == 3:
            star_3 = True
            data_game = True
            print("==========MISSION==========")
            print("tip: Press [ENTER] to proceed:")
            print("MISSION BRIEF")
            input("A mysterious user has been flagged by the system.")
            input("It is your job to find out if the system has successfully flagged this user by manually checking.")


            print("Connecting to Recovery Terminal...")
            print("Connection Established.")
            print("Scanning Device...")
            time.sleep(2)
            print("[#] 10%")
            time.sleep(1.6)
            print("[##] 20%")
            time.sleep(2)
            print("[###] 30%")
            time.sleep(1)
            print("[#####] 50%")
            time.sleep(1)
            print("[#######] 70%")
            time.sleep(1)
            print("[#########] 99%")
            time.sleep(5)
            print("[#########] 100%")

            print("Device Found")
            time.sleep(1)
            print("Status: Online")
            time.sleep(1)
            print("Encryption: Active")
            time.sleep(1)
            print("Permission Token: Verified")

            print("Director:")
            print("Good work. The company has authorised this recovery so....")
            print("Everything you do is legal.")

            time.sleep(1)

            print("Initializing Recovery Module...")
            print("Loading...")
            print("Loading...")
            print("Ready.")

            input("Press ENTER to begin...")
            while star_3:

                print("\nChoose where to search.")
                print("1. Access")
                print("2. Work Files")
                print("3. Music")
                print("4. Exit")

                choice = input("Enter your choice: ").lower()

                if choice in ["1", "access"]:
                    if data_game:
                        def email_asign():
                            global email_id, email1, email2, email3, email4, email5
                            if random.randint(1, 100) == 50:
                                email_id = random.randint(1, 99999)
                                email1 = random.randint(10000, 99999)
                                email2 = random.randint(10000, 99999)
                                email3 = random.randint(10000, 99999)
                                email4 = random.randint(10000, 99999)
                                email5 = random.randint(10000, 99999)
                                if random.randint(1, 100) == 50:
                                    email_id = random.randint(100000, 999999)
                                    email1 = random.randint(100000, 999999)
                                    email2 = random.randint(100000, 999999)
                                    email3 = random.randint(100000, 999999)
                                    email4 = random.randint(100000, 999999)
                                    email5 = random.randint(100000, 999999)
                                else:
                                    email_id = random.randint(1000, 9999)
                                    email1 = random.randint(1000, 9999)
                                    email2 = random.randint(1000, 9999)
                                    email3 = random.randint(1000, 9999)
                                    email4 = random.randint(1000, 9999)
                                    email5 = random.randint(1000, 9999)
                            else:
                                email_id = random.randint(1000, 9999)
                                email1 = random.randint(1000, 9999)
                                email2 = random.randint(1000, 9999)
                                email3 = random.randint(1000, 9999)
                                email4 = random.randint(1000, 9999)
                                email5 = random.randint(1000, 9999)
                            chosen_email = random.randint(1, 5)
                            if len({email_id, email1, email2, email3, email4, email5}) != 6:
                                email_asign()
                        email_asign()
                        chosen_email = random.randint(1, 5)
                        if chosen_email == 1:
                            email1 = email_id
                        elif chosen_email == 2:
                            email2 = email_id
                        elif chosen_email == 3:
                            email3 = email_id
                        elif chosen_email == 4:
                            email4 = email_id
                        else:
                            email5 = email_id
                        print("tip: Press [ENTER] to proceed:")
                        input("Your job is to intercept to re-find the password to the company system in order to check.")
                        input("Compare the email ID to five different emails to find out the email that contains the password.")
                        input(f"The email ID is: {email_id}")
                        print("\n" * 30)
                        print("Scrolling up is for cheaters!")
                        print("\n" * 45)
                        while data_game:
                            print("\nChoose an email to investigate:")
                            print("Email 1")
                            print("Email 2")
                            print("Email 3")
                            print("Email 4")
                            print("Email 5")
                            print("Say \"choose\" when you are ready to match the email!")
                            choice = str(input()).lower()
                            if choice in ["1", "first", "1st", "email1", "email_1"]:
                                    print(f"The ID of Email 1 is {email1}")
                            elif choice in ["2", "second", "2nd", "email2", "email_2"]:
                                    print(f"The ID of Email 2 is {email2}")
                            elif choice in ["3", "third", "3rd", "email3", "email_3"]:
                                    print(f"The ID of Email 3 is {email3}")
                            elif choice in ["4", "fourth", "4th", "email4", "email_4"]:
                                    print(f"The ID of Email 4 is {email4}")
                            elif choice in ["5", "fith", "5th", "email5", "email_5"]:
                                    print(f"The ID of Email 5 is {email5}")
                            elif choice == "choose":
                                choice = str(input("What email matches? ")).lower()
                                if choice in ["1", "first", "1st", "email1", "email_1"]:
                                        if email1 == email_id:
                                            print("Sucessfully retrieved password")
                                            data_game = False
                                        else:
                                            print("ID does not match, returning to menu")
                                            break
                                elif choice in ["2", "second", "2nd", "email2", "email_2"]:
                                        if email2 == email_id:
                                            print("Sucessfully retrieved password")
                                            data_game = False
                                        else:
                                            print("ID does not match, returning to menu")
                                            break
                                elif choice in ["3", "third", "3rd", "email3", "email_3"]:
                                        if email3 == email_id:
                                            print("Sucessfully retrieved password")
                                            data_game = False
                                        else:
                                            print("ID does not match, returning to menu")
                                            break
                                elif choice in ["4", "fourth", "4th", "email4", "email_4"]:
                                        if email4 == email_id:
                                            print("Sucessfully retrieved password")
                                            data_game = False
                                        else:
                                            print("ID does not match, returning to menu")
                                            break
                                elif choice in ["5", "fith", "5th", "email5", "email_5"]:
                                        if email5 == email_id:
                                            print("Sucessfully retrieved password")
                                            data_game = False
                                        else:
                                            print("Unsuccessful access, ID does not match, returning to menu...")
                                            star_3 = False
                                            break
                    else:
                        print("You have already gained access")
                elif choice in ["2", "work files"]:
                    if data_game == False:
                        input("You have gained access to the systems.")
                        input("Compare the IDs to determine whether the email is sent from outside the organisation.")
                        input("Memorise the digits and copy them down into the system to check if the email is legitimate.")
                        email_id = random.randint(100000, 999999)
                        attempts = 3
                        input(f"Press [ENTER] when you are ready, the digits are {email_id}")
                        print("\n" * 30)
                        print("Scrolling up is for cheaters!")
                        print("\n" * 45)
                        while attempts != 0:
                            print(f"You have {attempts} attempts.")
                            choice = int(input("ID: "))
                            if choice == email_id:
                                print("Successfully identified email.")
                                money += 350
                                star_3 = False
                                break
                            else:
                                attempts -= 1
                        if attempts == 0:
                            print("Unsuccessful identification, returning to menu...")
                            star_3 = False
                            break
                    else:
                        print("No access")


        elif stars == 4:
            print("tip: Press [ENTER] to proceed:")
            print("MISSION BRIEF")
            idc = input("A small technology company has contacted your agency. ")
            idc = input("One of their employees left a company laptop on a train. ")
            idc = input("The laptop has now been found, but it is locked and the employee forgot the password. ")
            idc = input("The company has given you full permission to recover the important work files. ")
            idc = input("Your mission is to safely access the laptop and recover the documents. ")
            idc = input("before the automatic file cleanup starts. ")

            print("\nConnecting to Recovery Terminal...")
            print("Connection Established.")
            print("Scanning Device...")
            time.sleep(1)
            print("[#] 10%")
            time.sleep(0.5)
            print("[##] 20%")
            time.sleep(0.5)
            print("[###] 30%")
            time.sleep(0.5)
            print("[#####] 50%")
            time.sleep(0.5)
            print("[#######] 70%")
            time.sleep(0.5)
            print("[#########] 99%")
            time.sleep(1)
            print("[#########] 100%")
            print("Device Found")
            time.sleep(0.5)
            print("Status: Online")
            time.sleep(0.5)
            print("Encryption: Active")
            time.sleep(0.5)
            print("Permission Token: Verified")

            print("\nDirector:")
            print("Good work. The company has authorised this recovery so....")
            print("Everything you do is legal.")
            time.sleep(1)

            print("\nInitializing Recovery Module...")
            print("Loading...")
            print("Ready.")
            input("Press ENTER to begin...\n")

            # =============================
            # Level 1: Password Decryption
            # =============================
            print("Encrypt OLAAWS")
            print("Every letter has been shifted one place left on the QWERTY keyboard.")
            password_decryption = input("Enter the decrypted password - ").lower().strip()

            if password_decryption == "passed":
                print("Well done!\n")
                idc = input("Enter to continue ")

                # =============================
                # Level 2: Fibonacci Sequence
                # =============================
                print("[0] [1] [1] [2] [3] [5] [8] [?] [21]")
                try:
                    level2 = int(input("What should the ? be replaced with - "))
                except ValueError:
                    level2 = 0

                if level2 == 13:
                    print("Passed Level 2!\n")
                    
                    # =============================
                    # Level 3: Fire wall Sequence
                    # =============================
                    input("Enter to start ")
                    print("1 = 4")
                    print("2 = 10")
                    print("3 = 18")
                    print("4 = 28")
                    print("5 = ?")
                    try:
                        level_3 = int(input("What should the ? be replaced with - "))
                    except ValueError:
                        level_3 = 0

                    if level_3 == 40:
                        print("\nLevel 1 [+]")
                        print("Level 2 [+]")
                        print("Level 3 [+]")
                        print("SYSTEM UNLOCKED\n")
                        input("Press Enter to access file directory ")
                        
                        # =============================
                        # File System Menu
                        # =============================
                        while True:
                            print("\nAvailable Files:")
                            print(" - Ghost_Core")
                            print(" - File_Core")
                            print(" - Boss_Core")
                            print(" - Shadow_Protocol")
                            print(" - Project_Nightfall")
                            print(" - Unknown_File")
                            
                            choice = input("\nWhat file do you wish to open: ").strip().lower()

                            if choice == "ghost_core":
                                print("----------------------------------------")
                                print("GHOST_CORE")
                                print("----------------------------------------")
                                print("[+] Employee records recovered.\n")
                                print("EMPLOYEE: Daniel Cross")
                                print("ID: #77291")
                                print("STATUS: MISSING")
                                print("LAST LOCATION: Sector 04")
                                print("LAST LOGIN: 03:47 AM\n")
                                print("----------------------------------------")
                                print("Director")
                                print("Quick delete that before anyone notices")                            
                                choice = input("Do you wish to delete it").lower()
                                if choice == "yes":
                                    money = money + 300
                                    print("Director")
                                    print("Good Job it was a hard mission and I will give you £300 just for that")
                                else:
                                    break
                                break
                            elif choice == "file_core":
                                print("----------------------------------------")
                                print("FILE_CORE")
                                print("----------------------------------------")
                                print("[+] Recovering deleted documents...")
                                print("[+] 3 documents recovered.\n")
                                print("DOCUMENT 01: Company_Overview.txt")
                                print("DOCUMENT 02: Employee_Reports.txt")
                                print("DOCUMENT 03: Security_Breach.txt\n")
                                print("SECURITY_BREACH.TXT:")
                                print("An unknown user accessed the mainframe")
                                print("at 02:13 AM.")
                                print("Security cameras were disabled.")
                                print("No entry was recorded at the doors.")
                                print("The intruder was never identified.\n")
                                print("[!] 17 additional files corrupted.")
                                print("----------------------------------------")
                                break
                            elif choice == "boss_core":
                                print("----------------------------------------")
                                print("BOSS_CORE")
                                print("----------------------------------------")
                                print("[!] ADMINISTRATOR ACCESS REQUIRED\n")
                                print("ADMINISTRATOR: UNKNOWN")
                                print("ACCESS LEVEL: MAXIMUM")
                                print("SECURITY STATUS: ACTIVE\n")
                                print("LAST ADMIN MESSAGE:")
                                print("If you are reading this, the system")
                                print("has already been compromised.")
                                print("Do not trust the recovery terminal.")
                                print("Someone inside this company is")
                                print("controlling everything.\n")
                                print("[!] ACCESS TO REMAINING DATA BLOCKED.")
                                print("----------------------------------------")
                                break
                            elif choice == "shadow_protocol":
                                print("----------------------------------------")
                                print("SHADOW_PROTOCOL")
                                print("----------------------------------------")
                                print("[+] Classified document recovered.\n")
                                print("OPERATION: SHADOW")
                                print("CLASSIFICATION: TOP SECRET")
                                print("STATUS: ACTIVE")
                                print("AUTHORISED PERSONNEL: 3\n")
                                print("MISSION DETAILS:")
                                print("1. Monitor all employee activity.")
                                print("2. Hide unauthorised system access.")
                                print("3. Remove evidence of Project Nightfall.\n")
                                print("[!] FINAL INSTRUCTION:")
                                print("If the recovery team discovers the")
                                print("truth, activate Protocol 09.\n")
                                print("[!] PROTOCOL 09 NOT FOUND.")
                                print("----------------------------------------")
                                break
                            elif choice == "project_nightfall":
                                print("----------------------------------------")
                                print("PROJECT_NIGHTFALL")
                                print("----------------------------------------")
                                print("[+] Opening classified research...\n")
                                print("PROJECT: NIGHTFALL")
                                print("START DATE: 14/08/2024")
                                print("DIRECTOR: UNKNOWN")
                                print("FUNDING: CLASSIFIED")
                                print("STATUS: TERMINATED\n")
                                print("RESEARCH NOTES:")
                                print("The experiment was successful.")
                                print("The system can now operate without")
                                print("human supervision.")
                                print("However, something unexpected happened.")
                                print("The system began creating its own files.")
                                print("Nobody knows where they came from.\n")
                                print("[!] PROJECT TERMINATED BY ADMIN.")
                                print("----------------------------------------")
                                break
                            elif choice == "unknown_file":
                                print("----------------------------------------")
                                print("UNKNOWN_FILE")
                                print("----------------------------------------")
                                print("[+] Attempting to identify file...")
                                print("[+] File name: UNKNOWN")
                                print("[+] Creator: UNKNOWN")
                                print("[+] Creation date: UNKNOWN\n")
                                print("[!] UNEXPECTED RESPONSE RECEIVED.\n")
                                print("SYSTEM MESSAGE:")
                                print("You should not be here.")
                                print("I know what you are looking for.")






    # =========================
    # QUIT
    # =========================
    if response == "quit":
        print("Exiting game...")
    else:
        print("Invalid option")

