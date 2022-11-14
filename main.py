#Code for generating a random password with choices for more -> less secutiry

import random
import secrets


#ui will be used as a shortend version of UserInput to avoid confusion and long var names
uiType = input("Realistic(1) or obscure password?(2): ")
if(uiType == "1"):
    #Here we will generate a good but "easy" to remember password
    words = open('words.txt', 'r')
    wordsRead = words.readlines()
    finalPassword = ""
    count = 0
    for x in range(4):
        count = count + 1 
        rand = random.randint(0, len(wordsRead))
        x = wordsRead[rand].strip()
        print("Word {} in your password is:".format(count) + " " + x)
        finalPassword = finalPassword + x
        #The final password is now 4 random words that you have no connection to.
        #Should be fairly easy to remeber if you get a good sequence and hard to guess
    if(len(finalPassword) < 20):
        #Should we get 4 short words we'll add one more! just in case. Can be removed if wishes
        rand = random.randint(0, len(wordsRead))
        x = wordsRead[rand]
        finalPassword = finalPassword + x
        print("Your password is: " + "" + finalPassword)
    else:
        print("Your password is: " + "" + finalPassword)
elif(uiType == "2"):
    uiLength = input("Please select the lenght of your password: ")
    #This might be somewhat of a shortcut but we could manually add random numbers and letter
    #And shuffle them a couple of time. I don't expect to use this feature often.
    print("Your password is:" + " " + secrets.token_urlsafe(int(uiLength)))
    
        
else:
    print("You've enterd something incorrectly, I suggest you rerun the program!")
