films = {
    "Finding Dory": [3.5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        pass
    else:
        print("We don't have that film...")