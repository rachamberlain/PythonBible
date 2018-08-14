known_users = ["Raz","Coles","Coops","Wiz","Bov","Big Dave,","Rymer"]


while True:
    print("Hi, my name is Travis")
    user_name = input("What is your name? :").strip().capitalize()

    if user_name in known_users:
        print("Hello {} how are you today?".format(user_name))
        remove = input("Would you like to be removed from the system? (y/n)? :").strip().lower()

        if remove == "y":
            known_users.remove(user_name)
        elif remove =="n":
            print("No problem")

    else:
        print("Hmmm I don't think I have met you yet {}".format(user_name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add_me == "y":
            known_users.append(user_name)
        elif add_me == "n":
            print("Thats fine, maybe another time...")
