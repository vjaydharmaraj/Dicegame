import random

x = "y"

while x == "y":
    # Generates a random number
    # between 1 and 6 (including both 1 and 6)

    no = random.randint(1 , 6)


    if no == 1:
        print("[-----]")
        print("[    ]")
        print("[   0   ]")
        print("[     ]")
    elif no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif no == "3":
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    
    x = input("press y to roll again and n to to exit: "  )
    print("\n")