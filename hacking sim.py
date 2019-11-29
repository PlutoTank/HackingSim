print("  _    _            _    _                _____ _           ")
print(" | |  | |          | |  (_)              / ____(_)          ")
print(" | |__| | __ _  ___| | ___ _ __   __ _  | (___  _ _ __ ___  ")
print(" |  __  |/ _` |/ __| |/ / | '_ \ / _` |  \___ \| | '_ ` _ \ ")
print(" | |  | | (_| | (__|   <| | | | | (_| |  ____) | | | | | | |")
print(" |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, | |_____/|_|_| |_| |_|")
print("                                 __/  |                     ")
print("                                 |___/                      ")


#Python tips and tricks! comments use the hash things
#Instead of using {} you just indent it and use : to start it
#for loops use for i in range(amount of loops) or you can do the same thing or you can give a start value, stop value, and a incriment
#While loops don't use () because python is weird. Same sort of colon thing
#basiclly python hates brackets
#break is still usefull and the same

import random
import os
import time

end = ""
nametest = True 
nametrys = 0 #how many trys for hacker name
edge = 0 #name's edge
leet = 0
isleet = False
memeboi = False



#battle vars

block = 0
power = 0
gold = 0
sword = " "
dam = 1
global hp
hp = 5
armor = "Meme Shirt"
win = False
totalhp = 5
dam2 = 3
totalg = 100
gold = random.randint(5,20)
totalg += gold
sword = "PingMax2000"
dam = 2
emaxatk = 0
eminatk = 0
eaim = 0
re = 4
realName = ""

#4 numbers at in name at least
#1337ness meter above 5
#add edge meter must be above 5


#Fourm code
re = 0

t = True
sp = ""
box = "----------------------------------------------------------------"

p12 = "|How do you 1337 hack?|"
p13 = "Hi guys i want 2 be a 1337 hacker so my friends think im cool"
p14 = "Can anyone teach me how 2 1337 hack?"
p15 = "- edgelord666"

p21 = "|Should I hack edgelord666?|"
p22 = "Hi my dudes vote yes or no"
p23 = "> yes 10"
p24 = "> no 1"
p25 = "-  ma5k3dM3m3r"
posting = True


sendhint = False
    






def matrix():
    
    hint = False
    
    print("              _        _     ")
    print("  /\/\   __ _| |_ _ __(_)_  __")
    print(" /    \ / _` | __| '__| \ \/ / ")
    print("/ /\/\ \ (_| | |_| |  | |>  < ")
    print("\/    \/\__,_|\__|_|  |_/_/\_\ ")
    print("")
    print("------------WELCOME TO THE MATRIX FOURMS!------------")
    print("We are a group of elite hackers")
    print("Ask for passwords and we may or may not help you")
    print("If you are a troll (low level human) please go back to 4chan")
    print("Rules:")
    print("Must have some level of edge")
    print("No posting dead memes")
    print("Please make sure your ip is not being tracked")
    print("Thanks for reading - xx_ma5t3r-0f-3dg3_xx")
    print("")
    print("IMPORTANT PLEASE READ:")
    print("type 'passhint' in menu to put in request for a password hint (sent to inbox)")
    print("type 'fourm' to go to the fourms")
    print("type 'inbox' to see messages")
    print("type 'exit' to exit")
    print("type 'chatroom' to enter the chat room");
    print("")

    while t == True:
        menu = input("Type an action: ").lower()



        if menu == "fourm":
            fourm()

        elif menu == "passhint":


            if hint == False:
                print("Request Sent!")
                print("Check inbox!")
                global sendhint
                sendhint = True
                hint = True
                
                
        
            else:
                print("You already sent one!")
                
                
            
        elif menu == "inbox":
            inbox()

        elif menu == "exit":
            func1()

        elif menu == "chatroom":
            chatRoom();

        else:
            print("Invalid")
        
        

def fourm():
    
     print("              _        _          ___                              ")
     print("  /\/\   __ _| |_ _ __(_)_  __   / __\__  _ __ _   _ _ __ ___  ___ ")
     print(" /    \ / _` | __| '__| \ \/ /  / _\/ _ \| '__| | | | '_ ` _ \/ __|")
     print("/ /\/\ \ (_| | |_| |  | |>  <  / / | (_) | |  | |_| | | | | | \__ \ ")
     print("\/    \/\__,_|\__|_|  |_/_/\_\ \/   \___/|_|   \__,_|_| |_| |_|___/ ")
     print("")
     print("")
     print("")
     print("")


     print(box)
     print(p12)
     print(sp)
     print(p13)
     print(p14)
     print(p15)
     print(box)
     print(sp)



     print(box)
     print(p21)
     print(sp)
     print(p22)
     print(p23)
     print(p24)
     print(p25)
     print(box)
     print(sp)

     
         

        
     while posting:   
         print("type 'exit' to leave")
         print("type 'post' to post something")
         fourmo = input("Action: ").lower()
     
         if fourmo == "exit":
             matrix()
             break
             

         else:
             print("")
             print("")
             title = input("Title: ")
             print("")
             post = input("Body: ")
             print(box)
             print("|" + title + "|")
             print(sp)
             print(post)
             print(" - " + hackname)
             print(box)

def chatRoom():
    print(box);
    print("|Welcome to the chatRoom|")
    print("H3y guy5. h0w d0 y0u h4ck 4 m1n3cr4ft s3rv3r. I need to know nooooooooow.")
    print("--XxcreeperboyxX")
    print();
    print("Downl04d LOIC, so den you can DDDOSS them");
    print("--__St3v3H34d5849__")
    print();
    while True:
        
        print("Type 'exit to leave at any time")
        pTalk = input("Type your message here: ");
        if random.randrange(0,5) == 4:
            RPGGAME();
            break;
        print("")
        print(pTalk);
        print("--"+hackname);
        print();
        if "hack" in pTalk:
            print("I 4m th3 b3st h4cker in teh w0rld. Y0u d4re t4lk t0 me?");
            print("--_____XxXxB3srH4k3e3V3rxXxX____");
            print();
        elif "meme" in pTalk:
            print("Do you want to share memes???")
            print("TheMemeCollector6");
            print();
        elif pTalk == "exit":
            matrix();
            break;
        elif "minecraft" in pTalk:
            print("do you waant to play mynecraft????????????????");
            print("--_-_-cooklbioy7_____-----");
            print();
        else:
            message = random.randrange(1,7);
            if message == 1:
                print("Get out of here n00b");
                print("--DabBoi69696969");
                print();
            elif message == 2:
                print("Where do you live young boy?");
                print("--nOtApEdOfIlE");
                print();
            elif message == 3:
                print("kys scrub");
                print("--EDGELORD666");
                print();
            elif message == 4:
                print("hey... you wanna buy a, funnel cake?");
                print("--uNdErSteadyhuckstler");
                print();
            elif message == 5:
                print("how can I download more RAMs. Please I need more or my mom will kill be because I used it all!");
                print("--Ssokerkid22");
                print();
            elif message == 6:
                print("Guys check out my new virus!");
                print("--PlageDoctor6743__");
                print();
            elif message == 7:
                print("Do you want to see my scars??? I have a lot");
                print("--WaKeMeUpInSiDeXxXxXxXx________xXxX");
                print();
            else:
                print("Mind if I roll need???");
                print("--l00tH0rder");
                print();

    
    


def inbox():
    global sendhint
    print(hackname + "'s inbox")

    print("> Welcome to the Matrix " + hackname)

    if hackCount == 0 and sendhint == True:
          print("> What's your name again?")
          
          sendhint = False

    elif hackCount == 1 and sendhint == True:
          print("> What is your brother's favourite game. What is his jersey number. No creep...")
          
          sendhint = False
    elif hackCount == 2 and sendhint == True:
          print("> What was that bank called again?")
          
          sendhint = False
    elif hackCount == 3 and sendhint == True:
          print("> Sometimes after you DDOS like a pro it deletes the password")
          
          sendhint = False
    elif hackCount == 4 and sendhint == True:
          print("> One time I hacked this guy's door lock and it was just his house number XDDD")
         
          sendhint = False
    else:
        print("> Duuuuuuude.......Dude what's going on?")
        sendhint = False
        

#end of fourm code

dotNumber = 0
hackCount = 0

def passwordGuesser(password,tries):
    
    attempts = 0
    
    while True:
        
        if attempts < tries:
            correctChars = 0;
            charsIn = 0;
            guess = input("Hack the password: ");
            
            if guess == "exit":
                func1();
                break;
            
            else:
            
                if guess == password:
                    print("You have successfully cracked the password")
                    global hackCount;
                    hackCount += 1;
                    func1();
                    #hint = False;
                    break;
                
                else: #if they get the password wrong

                    if len(guess) > len(password):

                        dif = len(guess) - len(password)

                        for i in range(len(guess) - dif):

                            if guess[i] == password[i]:

                                correctChars +=1

                    else:

                        for i in range(len(guess)):
                       
                           if guess[i] == password[i]:
                            
                                correctChars += 1

                    print("Correct characters: " + str(correctChars))
                    attempts += 1;
                    charsIn = 0;
                    correctChars = 0

                    
                        
                   
        else:
            print("You could not hack in time and you have been out hacked by a password!")
            func1();
            break;

#START OF RPG CODE
        
def RPGGAME():


    print();
    print();
    print("YOU ARE BEING HACKED!!!");
    re = 4
    



    def ping():
        
        global you
        global power
        global win
        global ehp
        
        power += 1;
        print(str(ehp)) 
        if you == True:
            print("")
            print("You pinged the " + emn + " with your "+ sword + " and did " + str(roundr) + " damage!");
            ehp -= roundr;
            
        
            if ehp <= 0:

                ehp = 0
                print("")
                print("You did a killing headshot on the " + emn);
                win = True
                slaying = False;
                
                        
                   
        
            else:
                you = random.randint(0,3)
                enemyattack()
                
               
        

      
      

               
      
        else:
            print("")
            print("Connection Failed");
            you = random.randint(0,3)
            enemyattack()
           
      


    def pod():
        
        global power
        global you
        global win
        global ehp
        
        power -= 2;
        if you:
            print("")
            print("You spamed pings and pinged the " + emn + " with your " + sword + " and did " + str(round1) + " damage!");
            ehp -= round1
            if ehp <= 0:
                
                ehp = 0
                win = True;
                print("")
                print("You did a killing headshot on the " + emn);
                slaying = False;
                matrix()
                
            else:
                you = random.randint(0,3)
                slaying = False;
        

             

        else:
            print("Connection Failed")
            you = random.randint(0,3)
            slaying = False;


    def protect():
        global block
        global power
        block = 1
        power += 1;
        slaying = False

    def enemyattack():

        global hp
        
        em = random.randint(0,eaim)
        enemy = random.randint(eminatk,emaxatk)

        if em:
            hp -= enemy
            print("")
            print("The " + emn + " pinged you for " + str(enemy) + " damage!")
            
        else:
            
            print("The " + emn + "'s connection failed")
            

        if (hp <= 0):
            
            hp = 0
            print("")
            print("You died")
            slaying = False
            re = 0
            func1();
              

        
        


    if re > 3:

        global ehp
      
        
        echoice = random.randint(0,2)

        if echoice:

       
            emaxatk = 3
            eminatk = 1
            eaim = 2
            ehp = 4;
            emn = "n00b";
            etotal = 0;
          
       
      

      
        else:

            emaxatk = 4
            eminatk = 1
            eaim = 3
            ehp = 3;
            emn = "Angry n00b";
            etotal = 0;
            
            
    #succ benis
        
        slaying = True;
        damr1 = 2 + dam
        damr2 = 1 + dam2
        global you
        you = random.randint(0,3)
        roundr = random.randint(dam,dam2)
        round1 = random.randint(damr1,damr2)
        total = 0;
        
      
      
      
        while slaying:

            print("")
            print("Your Heath: " + str(hp));
            print(emn + " Heath: " + str(ehp));
            block = 0;
            win = 0;

            if (ehp <= 0):
                break
            
            elif(hp <= 0):
                break
            
            else:
                if power > 2:

                    fight = input("[P]ing, [G]host Ip or PO[D]: ").lower()

                    if fight == "p" or fight == "ping":
                        ping()

                    elif fight == "pod" or fight == "d":
                        pod()
                
                    else:
                        protect()
                else:
                    fight = input("[P]ing or [J]ump Ip: ").lower()
            
                    if fight == "p" or fight == "ping":
                        ping()
                
                    else:
                        protect()
#END OF RPG CODE

#Name Function

def name():
    global realName
    realName = input("what is your real name: ");
    print("Hello " + realName);
    func1()



def func1():
    print("")
    print(hackname + "'s computer")
    print("1337linux Version 4.2")
    print("")
    
    
    global hackCount;
    while True:
        a = (input("C:\> ")).lower();#waits for user to input command. It is in a loop so that it can happen multiple times
        if a == "h":
            for i in range(70):
                global dotNumber;
                dotNumber += 1;
                print()
                for i in range(dotNumber):
                    print("HACKING " + (". " * dotNumber));
                

                
                    
        elif a == "matrix":
            matrix();


            
            break;
        elif a == "fight":
            if hackCount == 0:
                
                print("You go into your mom's bedroom and open her computer.");
                print("You begin to breath heavilly as you reach for your bottle of mountain dew");
                print("You unscrew the cap and pour your power fuel down your throat");
                print("You begin to hack");
                print("The first stage is to guess the password");
                passwordGuesser(realName, 100);
                break;
            
            elif hackCount == 1:
                print("After going through all of your mom's files you leave her room");
                print("You pack your computer up and head to your little brother's room to hack his computer");
                print("Your brother's room is filled with MineCraft toys and posters");
                print("You open up his laptop to find a computer so dirty it rivals your own");
                print("Your brother's sports jersey with the number 67 is hanging on the wall")
                print("You pull out your computer and begin to hack");
                passwordGuesser("MineCraft67", 999);
                break;
            
            elif hackCount == 2:
                print("After looking at your little brother's disgusting files you hear your mom come into the house")
                print("You quickly pack up your computer and jump out the window so she doesn't catch you skipping school");
                print("You are now outside and need money, so you decide to hack the local DaNkBaNk");
                print("You walk over to the bank");
                print("Panting from the physical activity you pull out your computer and try to connect to the bank's wifi");
                print("The bank's wifi has a password. It's time to hack")
                passwordGuesser("DaNkBaNk", 20);
                break;
            
            elif hackCount == 3:
                print("You are now in the bank's network");
                print("You open up LOIC and are ready to fire");
                hsdkjfhjksdhfkjhsdkjfhkjh = input("Press enter to DDOS the bank's security");
                for i in range(200):
                    print("Pew Pew. DDOS DDOS" + str(i));
                    print("Your arms are heavy, your knees are weak as you think of your missed mom's spaghetti")
                    print("But you move on. All you need now is the password so you can transfer funds into your account")
                    passwordGuesser("", 15);
                
            elif hackCount == 4:
                
                print("After finding out that your DDOS destroyed the password your bank account is full but your desire for mom's spaghetti is too strong")
                print("You start walking home to your house, #6167")
                print("When you get home the door's hackable lock is locked and you need to hack the 4 didget code")
                passwordGuesser("6167",5);
                
            elif hackCount == 5:
                print("You get home and eat your mom's spaghetti");
                
                hackCount = 6;
                
            else:
                
                
                while(True):
                    print("You are bored so you decide to hack the people in your game of Call Of Duty");
                    choice = input("Do you wish to DDos them or Hack into their files: ");
                    if choice == "DDOS":
                        print();
                        for i in range(200):
                            print("Pew Pew. DDOS DDOS" + str(i));
                        print();

                            
                    elif choice == "exit":
                        func1();
                        break;
                    elif choice == "h" or "hack" or "Hack":
                        print();
                        print("This next section is for the hardcore only. There are no hints and the passwords are random")
                        print("However, the passwords are all numbers between 0 and 100000 and you will have 30 attempts")
                        print();
                        
                        passwordGuesser(str( random.randrange(0,100000)),30);
                        

                    else:
                        print("That choice is invalid");
                    
                

                
        elif a == "help":
            print();
            print("help: lists all commands");
            print("fight: sends you into the hacking world");
            print("h: hacks NASA");
            print("matrix: enters the matrix fourms");
        else:
            print("That is invalid!");
            print("For a list of valid commands type help");


while nametest:
    hackname = input("Enter hacker name: ").lower()

    for i in range(len(hackname)):
    
        if "3" in hackname:

            if leet < 11:
                leet += 0.25
            
            if edge < 11:
                edge += 0.1

        if "0" in hackname:
        
            if leet < 11:
                leet += 0.21
            
            if edge < 11:
                edge += 0.11

        if "x" in hackname:

            if leet < 11:
                leet += 0.20
        
            if edge < 11:
                edge += 0.5

        if "_" in hackname:

            if leet < 11:
                leet += 0.10
         
            
            if edge < 11:
                edge += 0.10

        if "s" in hackname:
  
            if edge < 11:
                edge += 0.20

        if "5" in hackname:

            if leet < 11:
                 leet += 0.20
                 
            if edge < 11:
                edge += 0.1

        if "1337" in hackname:

            if isleet == False:
                isleet = True
            
                leet += 0.5
                edge += 0.3
        if "meme" in hackname:

            if memeboi == False:
                mememoi = True

                leet += 0.5
                edge += 0.2
            
        if "1" in hackname:
        
            if leet < 11:
                leet += 0.2

            if edge < 11:
                edge += 0.1
                
    print("")
    print ("edge " + str(round(edge)))
    print ("1337ness " + str(round(leet)))
    print(" ")

    if edge < 5:
        print("You need more edge")
        print("Hint try adding the letter x")
        print(" ")
        
        
        
    
    elif leet < 5:
        print("You need more 1337ness")
        print("Hint: Try switching letters with numbers like e to 3")
        print(" ")
        
    else:
        name()
        nametest = False
        break




    
        
