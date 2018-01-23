ask = input("What would you like to play instead? \n The two options are: superhero or quote mad lib. Choose one \n: ")

if ask == "superhero":
    name = input("What is your name? \n: ") # The \n means new row with semi colons :
    verb = input("Give a verb \n: ")
    adj = input("Give an adjective \n: ")
    ani = input("Give an animal name \n: ")

    sent = " {}, with their special powers. {} to save the {} {}, before mama got home!".format(name, verb, adj, ani) # can add as many varaibles with comma to seperate
    print(sent)

elif ask == "quote":
    verb1 = input("Please give me a verb \n: ")
    ani1 = input("Please give me an animal \n: ")
    verb2 = input("Please give me a verb \n: ")
    ani2 = input("Please give me a second animal \n: ")

    quo = "{} like a {}, {} like a {}".format(verb1, ani1, verb2, ani2)
    print(quo)
