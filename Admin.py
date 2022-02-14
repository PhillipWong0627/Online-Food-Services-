import time


def admin_login():
    i = 0
    while i == 0:
        flat = True
        adminID = input("Admin ID: ").strip().upper()
        adminpassword = input("Admin Password: ").strip()

        with open("Admin.txt", "r") as adminFile:
            readAdminID = adminFile.readlines()

            for line in readAdminID:
                splitLine = line.split(",")
                splitName = splitLine[0]
                splitPassword = splitLine[1].strip()

                if (adminID == splitName.upper() and adminpassword == splitPassword):
                    flat = True
                    break
                else:
                    flat = False

            if flat == True:
                i = 1
                print("Login Successfully...")
                time.sleep(2)
                print("-" * 50)
                # LOGIN ALREADY
            else:
                time.sleep(1)
                print("Invalid ID or Password\nPlease Try Again")


def add_FoodItem():
    while True:
        print("----------Food Category----------")
        print("1. RICE")
        print("2. NOODLE")
        print("3. SIDE DISHES")
        print("4. DRINKS")
        print("5. To Back")

        try:
            addFOodItem = int(input("Please Choose a Category that you want insert Item OR 5 To Back:"))
            if (addFOodItem) == 1:

                riceID = input("Prompt:RXXX\nEnter Food ID: ")
                riceName = str(input("Prompt:" + "x" * 20 + "\nEnter Food Name:"))
                ricePrice = float(input("Enter Food Price: "))

                with open("Rice.txt", "a") as appendRice:

                    appendRice.write("\n%4s,%20s,%4s" % (riceID, riceName, ricePrice))

            elif (addFOodItem) == 2:

                noodleID = input("Enter Food ID: ")
                noodleName = str(input("Enter Food Name: "))
                noodlePrice = float(input("Enter Food Price: "))

                with open("Noodle.txt", "a") as appendNoodle:

                    appendNoodle.write("\n%4s,%20s,%4s" % (noodleID, noodleName, noodlePrice))

            elif (addFOodItem) == 3:

                sideDishesID = input("Enter Food ID: ")
                sideDishesName = str(input("Enter Food Name: "))
                sideFishesPrice = float(input("Enter Food Price: "))

                with open("SideDishes.txt", "a") as appendSideDishes:
                    appendSideDishes.write("\n%4s,%20s,%4s" % (sideDishesID, sideDishesName, sideFishesPrice))

            elif (addFOodItem) == 4:
                drinksID = input("Enter Drinks ID: ")
                drinksName = str(input("Enter Drinks Name: "))
                drinksPrice = float(input("Enter Drinks Price: "))

                with open("Drinks.txt", "a") as appendDrinks:
                    appendDrinks.write("\n%4s,%20s,%4s" % (drinksID, drinksName, drinksPrice))

            elif (addFOodItem) == 5:
                break

            else:
                print("-" * 50)
                print("Please Enter A valid Number")
                print("-" * 50)
                time.sleep(1)
        except ValueError:
            print("Please Key In Int, Not String <3")
            time.sleep(1)


def modify_FoodItem():
    while True:
        print("----------Food Category----------")
        print("1. RICE")
        print("2. NOODLE")
        print("3. SIDE DISHES")
        print("4. DRINKS")
        print("5. To back")

        modifyFoodItem = int(input("Please choose the category that you want modify Item: "))
        counter = 0

        if modifyFoodItem == 1:
            with open("Rice.txt", "r") as modifyRice:
                readModifyRice = modifyRice.readlines()
                # print(readModifyRice)

                for line in readModifyRice:
                    splitModifyRice = line.strip().split(",")
                    # print(splitModifyRice[0])
                    print("%5s,%30s,%10s" % (splitModifyRice[0], splitModifyRice[1], splitModifyRice[2]))

                with open("Rice.txt", "r") as riceFile:
                    checkedRiceId = input("Select Food ID: ")
                    amendRiceID = input("Insert New Food ID: ")
                    amendRiceName = input("Insert New Food Name: ")
                    amendRicePrice = input("Insert New Food Price: ")

                    readRiceFile = riceFile.readlines()
                    # print(riceFile)

                    for line in readRiceFile:
                        splitRiceFile = line.strip().split(",")
                        # print(splitRiceFile)
                        if splitRiceFile[0] == checkedRiceId:
                            # print(readFoodFile[counter])
                            readRiceFile[counter] = amendRiceID + "," + amendRiceName + "," + amendRicePrice + "\n"

                            break
                        else:
                            counter += 1
                    with open("Rice.txt", "w") as overrideRiceFile:
                        # print("".join(readFoodFile))
                        overrideRiceFile.write("".join(readRiceFile))

                    while True:
                        modifyInputR = str(input("Enter B To Continue Modify: ")).upper()

                        if modifyInputR == "B":
                            break

                        elif modifyInputR != "B":
                            print("You are OUT")

                            return

        if modifyFoodItem == 2:
            with open("Noodle.txt", "r") as noodleFile:
                readNoodleFile = noodleFile.readlines()
                for line in readNoodleFile:
                    splitNoodleFile = line.strip().split(",")
                    # print(splitNoodleFile)
                    print("%5s,%30s,%10s" % (splitNoodleFile[0], splitNoodleFile[1], splitNoodleFile[2]))

                with open("Noodle.txt", "r") as noodleFIle1:

                    checkedNoodleId = input("Select Food ID: ")
                    amendNoodleID = input("Insert New Food ID: ")
                    amendNoodleName = input("Insert New Food Name: ")
                    amendNoodlePrice = input("Insert New Food Price: ")

                    readNoodleFile1 = noodleFIle1.readlines()

                for line in readNoodleFile1:
                    # print(readNoodleFile1)
                    splitNoodleFile1 = line.strip().split(",")

                    # print(splitNoodleFile1[0])
                    if splitNoodleFile1[0] == checkedNoodleId:
                        # print(readNoodleFile1[counter])

                        readNoodleFile1[counter] = amendNoodleID + "," + amendNoodleName + "," + amendNoodlePrice + "\n"
                        break
                    else:
                        counter += 1
                with open("Noodle.txt", "w") as overrideNoodleFIle:
                    overrideNoodleFIle.write("".join(readNoodleFile1))

                while True:
                    modifyInputN = str(input("Enter B To Continue Modify: ")).upper()

                    if modifyInputN == "B":
                        break

                    elif modifyInputN != "B":
                        print("You are OUT")

                        return

        if modifyFoodItem == 3:
            with open("SideDishes.txt", "r") as sideDishFile:
                readSideDishFile = sideDishFile.readlines()
                # print(readSideDishFile)
                for line in readSideDishFile:
                    splitSideDishFile = line.strip().split(",")
                    print("%5s,%30s,%10s" % (splitSideDishFile[0], splitSideDishFile[1], splitSideDishFile[2]))

                with open("SideDishes.txt", "r") as sideDishFile1:

                    checkedSideDishId = input("Select Food ID: ")
                    amendSideDishID = input("Insert New Food ID: ")
                    amendSideDishName = input("Insert New Food Name: ")
                    amendSideDishPrice = input("Insert New Food Price: ")

                    raedSideDishFile1 = sideDishFile1.readlines()
                for line in raedSideDishFile1:
                    splitSideDishFile1 = line.strip().split(",")

                    # print(readSideDishFile)

                    # print(splitSideDishFile1[0])
                    if splitSideDishFile1[0] == checkedSideDishId:
                        # print(raedSideDishFile1[counter])
                        raedSideDishFile1[
                            counter] = amendSideDishID + "," + amendSideDishName + "," + amendSideDishPrice + "\n"
                        # print(raedSideDishFile1[counter])
                        break

                    else:
                        counter += 1

                with open("SideDishes.txt", "w") as overrideSideDishFile:
                    overrideSideDishFile.write("".join(raedSideDishFile1))

                while True:
                    modifyInputS = str(input("Enter B To Continue Modify: ")).upper()

                    if modifyInputS == "B":
                        break

                    elif modifyInputS != "B":
                        print("You are OUT")

                        return

        if modifyFoodItem == 4:
            with open("Drinks.txt", "r") as drinksFile:
                readDrinkFile = drinksFile.readlines()

                # print(readDrinkFile)

                for line in readDrinkFile:
                    splitdrinkFile = line.strip().split(",")
                    print("%5s,%30s,%10s" % (splitdrinkFile[0], splitdrinkFile[1], splitdrinkFile[2]))

                with open("Drinks.txt", "r") as drinkFile1:
                    checkedDrinksId = input("Select Food ID: ")
                    amendDrinksID = input("Insert New Food ID: ")
                    amendDRinksName = input("Insert New Food Name: ")
                    amendDrinksPrice = input("Insert New Food Price: ")

                    readDrinkFile1 = drinkFile1.readlines()

                for line in readDrinkFile1:
                    splitdrinkFile1 = line.strip().split(",")

                    if splitdrinkFile1[0] == checkedDrinksId:
                        readDrinkFile1[counter] = amendDrinksID + "," + amendDRinksName + "," + amendDrinksPrice + "\n"

                        break
                    else:
                        counter += 1

                with open("Drinks.txt", "w") as overrideDrinksFile:
                    overrideDrinksFile.write("".join(readDrinkFile1))

                while True:
                    modifyInputD = str(input("Enter B To Continue Modify: ")).upper()

                    if modifyInputD == "B":
                        break

                    elif modifyInputD != "B":
                        print("You are OUT")

                        return

        if modifyFoodItem == 5:
            break


def display_Record():
    try:
        while True:
            recordNo = int(input("Record No"
                                 "\n---------"
                                 "\n1 Food Category"
                                 "\n2 Food Menu"
                                 "\n3 Customer Orders"
                                 "\n4 Customer Payment"
                                 "\n5 To Back"
                                 "\nChoose a Code 1-5: "))

            if (recordNo == 1):
                print("----------Menu-----------")
                print("This is for READ only...")
                print("1. RICE")
                print("2. NOODLE")
                print("3. WESTERN")
                print("4. DRINKS")

                while True:
                    try:
                        backInput = int(input("Enter 5 to Back: "))
                        if backInput == 5:
                            print("=" * 50)
                            break
                        else:
                            print("Please Enter 5! ")
                    except ValueError:
                        print("String is not allowed!")
                        time.sleep(1)


            elif recordNo == 2:
                while True:
                    print("1. RICE")
                    print("2. NOODLE")
                    print("3. WESTERN")
                    print("4. DRINKS")
                    print("5. Back")

                    try:
                        categoryCode = int(input("Please Choose a Code 1-5: "))
                        # print("Back To Main Record Choose 5!")
                        print("-" * 50)

                        if categoryCode == 5:
                            break

                        if categoryCode == 1:

                            while True:
                                print("ID  |\tFood Name\t\t\t\t\t|Price")
                                with open("Rice.txt", "r") as riceFile:
                                    readRiceFile = riceFile.readlines()
                                    # print(readRiceFile)
                                    for line in readRiceFile:
                                        splitRice = line.strip().split(",")
                                        # print(splitRice)
                                        print(splitRice[0] + "\t" + splitRice[1] + "\t\t " + "RM" + splitRice[2])
                                    print("=" * 50)
                                    try:
                                        whileUserInput1 = int(input("Enter 6 To Back: "))
                                        if whileUserInput1 == 6:
                                            break
                                        else:
                                            print("Please Enter 6 To Back...")
                                            time.sleep(2)
                                    except ValueError:
                                        print("Please Enter A Int! Not String")
                                        time.sleep(2)


                        elif categoryCode == 2:
                            while True:
                                print("ID  |\tFood Name\t\t\t\t\t|Price")

                                with open("Noodle.txt", "r") as noodleFile:
                                    readNoodleFile = noodleFile.readlines()
                                    for line in readNoodleFile:
                                        splitNoodle = line.strip().split(",")
                                        print(splitNoodle[0] + "\t" + splitNoodle[1] + "\t\t\t" + "RM" + splitNoodle[2])
                                    print("=" * 50)

                                    try:
                                        whileUserInput2 = int(input("Enter 6 To Back: "))
                                        if whileUserInput2 == 6:
                                            break
                                        else:
                                            print("Please Enter 6 To Back...")
                                            time.sleep(2)
                                    except ValueError:
                                        print("Please Enter A Int! Not String")
                                        time.sleep(2)

                        elif categoryCode == 3:
                            while True:
                                print("ID  |\tFood Name\t\t\t\t\t|Price")
                                with open("SideDishes.txt", "r") as westernFile:
                                    readWesternFile = westernFile.readlines()
                                    for line in readWesternFile:
                                        splitWestern = line.strip().split(",")
                                        print(splitWestern[0] + "\t" + splitWestern[1] + "\t\t\t" + "RM" + splitWestern[
                                            2])
                                    print("=" * 50)

                                    try:
                                        whileUserInput3 = int(input("Enter 6 To Back: "))
                                        if whileUserInput3 == 6:
                                            break
                                        else:
                                            print("Please Enter 6 To Back...")
                                            time.sleep(2)
                                    except ValueError:
                                        print("Please Enter A Int! Not String")
                                        time.sleep(2)



                        elif categoryCode == 4:
                            while True:
                                print("ID  |\tFood Name\t\t\t\t\t|Price")
                                with open("Drinks.txt", "r") as drinksFile:
                                    readDrinksFile = drinksFile.readlines()
                                    for line in readDrinksFile:
                                        splitDrinks = line.strip().split(",")
                                        print(
                                            splitDrinks[0] + "\t" + splitDrinks[1] + "\t\t\t\t" + "RM" + splitDrinks[2])
                                    print("=" * 50)
                                    try:

                                        whileUserInput4 = int(input("Enter 6 To Back: "))
                                        if whileUserInput4 == 6:
                                            break
                                        else:
                                            print("Please Enter 6 to Back...")
                                            time.sleep(2)
                                    except ValueError:
                                        print("Please Enter A Int! Not String")
                                        time.sleep(2)

                        else:
                            print("Enter Valid Number\nPlease Try Again")
                            time.sleep(2)
                    except ValueError:
                        print("Please Enter A Integer! Not String!")
                        time.sleep(2)

            elif recordNo == 3:
                with open("CustomerOrder.txt", "r") as orderFile:
                    readOrderFile = orderFile.readlines()

                    for line in readOrderFile:
                        line = line.strip().split(",")

                        print(line[0] + "," + line[1] + "," + line[2])

                    while True:
                        userInput = str(input("Enter B to back: ")).upper()

                        if userInput == "B":
                            break
                        else:
                            print("Please Press B...")


            elif recordNo == 4:
                with open("payment.txt", "r") as paymentFile:
                    readPaymentFile = paymentFile.readlines()

                    for line in readPaymentFile:
                        line = line.strip().split(",")

                        print("%4s|%4s|%20s|%6s" % (line[0], line[1], line[2], line[3]))

                    while True:

                        userInput = str(input("Enter B to back: "))
                        if userInput == "B":
                            time.sleep(1)
                            break
                        else:
                            print("Please Press B...")
            elif recordNo == 5:
                return
            else:
                print("Invalid Input\nPlease Enter a Valid Number")
                time.sleep(1)

    except ValueError:
        print("Please Enter an Integer Number")
        time.sleep(1)


def search_record():
    while True:
        try:
            print("=" * 50)
            searchInput = int(input("Enter 1 search for Customer Order"
                                    "\nEnter 2 search for Customer Payment"
                                    "\nEnter 3 to Back"
                                    "\nPlease Enter 1-3: "))

            print("=" * 50)
            if searchInput == 1:
                with open("CustomerOrder.txt", "r") as searchCustOrder:
                    readSearchCustOrder = searchCustOrder.readlines()

                    for line in readSearchCustOrder:
                        line = line.strip().split(",")

                        print(line[0] + "," + line[1] + "," + line[2] + "," + line[3])

                    adminInput = input("Enter Customer ID: ")

                    with open("CustomerOrder.txt", "r") as searchCustOrderFile:
                        readSearchCustOrderFile = searchCustOrderFile.readlines()

                        for line in readSearchCustOrderFile:
                            line = line.strip().split(",")

                            if adminInput == line[0]:
                                print("%3s|%5s|%15s|%5s" % (line[0], line[1], line[2], line[3]))


                backInput = str(input("Enter B to Back: "))
                if backInput == "B":
                    time.sleep(1)
                    continue
                else:
                    print("Invalid Input...")

            elif searchInput == 2:
                with open("payment.txt", "r") as paymentFile:

                    readPaymentFile = paymentFile.readlines()

                    for line in readPaymentFile:
                        line = line.strip().split(",")

                        print(line[0] + "," + line[1] + "," + line[2] + "," + line[3])

                    adminInput1 = input("Enter Payment ID: ")

                    with open("payment.txt", "r") as paymentFile1:
                        readPaymentFile1 = paymentFile1.readlines()

                        for line in readPaymentFile1:
                            line = line.strip().split(",")

                            if adminInput1 == line[0]:
                                print("%3s|%3s|%15s|%5s" % (line[0], line[1], line[2], line[3]))

                backInput = str(input("Enter B to Back: "))
                if backInput == "B":
                    time.sleep(1)
                    continue
                else:
                    print("Invalid Input...")

            elif searchInput == 3:
                return

            else:
                print("Invalid Input...")
        except ValueError:
            print("Enter Int Number")


def fooditems():
    while True:
        print("=" * 25, "Guest View", "=" * 25)
        option = int(
            input("\nChoose your options\n1.View Menu\n2.Login or Register as customer\n3.Back\nChoose and enter (1-3): "))
        if option == 1:

            while True:
                print("=" * 25, "Guest View", "=" * 25)
                print("=" * 20, "Rice", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t\t|Price")

                with open("Rice.txt", "r") as ricefile:
                    readricefile1 = ricefile.readlines()
                    # print (readricefile1)
                    for a in readricefile1:
                        splitRice = a.strip().split(",")
                        # print (splitRice)
                        print(splitRice[0] + "\t" + splitRice[1] + "\t\t" + "RM" + splitRice[2])
                    print("=" * 50)
                    break

            while True:
                print("=" * 20, "Noodle", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t|Price")

                with open("Noodle.txt", "r") as noodlefile:
                    readnoodlefile1 = noodlefile.readlines()
                    # print (readricefile1)
                    for a in readnoodlefile1:
                        splitNoodle = a.strip().split(",")
                        # print (splitRice)
                        print(splitNoodle[0] + "\t" + splitNoodle[1] + "\t\t" + "RM" + splitNoodle[2])
                    print("=" * 50)
                    break

            while True:
                print("=" * 20, "Side Dishes", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t\t|Price")

                with open("SideDishes.txt", "r") as sidedishesfile:
                    readsidedishesfile1 = sidedishesfile.readlines()
                    for a in readsidedishesfile1:
                        splitsidedishes = a.strip().split(",")
                        print(splitsidedishes[0] + "\t" + splitsidedishes[1] + "\t\t\t" + "RM" + splitsidedishes[2])
                    print("=" * 50)
                    break

            while True:
                print("=" * 20, "Drinks", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t|Price")

                with open("Drinks.txt", "r") as drinksfile:
                    readdrinksfile1 = drinksfile.readlines()
                    for a in readdrinksfile1:
                        splitdrinks = a.strip().split(",")
                        print(splitdrinks[0] + "\t" + splitdrinks[1] + "\t\t\t" "RM" + splitdrinks[2])
                    print("=" * 50)
                    break

        elif option == 2:
            userId = CustDetails()
            fooditem1(userId)
            break
        elif option == 3:
            return

def CustDetails():
    Any = True
    while True:
        CustDetail = int(input("\n1. Login\n2. Register\nEnter 1 to Login or Enter 2 to Register: "))
        if CustDetail == 1:
            LoginID = input("Username: ")
            LoginPassword = input("Password: ")

            with open("customer.txt", "r") as loginfile:
                readloginfile1 = loginfile.readlines()
                # print (readloginfile1)
                for a in readloginfile1:
                    splitLogin = a.strip().split(",")
                    splitusername = splitLogin[0]
                    splitpassword = splitLogin[1]
                    if (LoginID == splitusername and LoginPassword == splitpassword):
                        Any = False
                        break
                    else:
                        Any = True
                if Any == False:
                    print("Login Successful!")
                    userId = LoginID
                    return userId
                    # break
                else:
                    print("Invalid Username or Password, please try again.")
        elif CustDetail == 2:
            RegisterID = input("New Username: ")
            RegisterPassword = input("New Password: ")

            with open("customer.txt", "a") as registerfile:
                registerfile.write("\n" + RegisterID + "," + RegisterPassword)
                print("Register Successful!, You are logged in")
                break

        else:
            print("Invalid input, Please try again")
            return CustDetails()


def fooditem1(userId):
    while True:
        print("=" * 25, "Login View", "=" * 25)
        option1 = int(input("\nChoose your options"
                            "\n1.View Food Category\n2.View Food Item\n3.Select food item and add to cart\n4.Proceed to payment"
                            "\n5.Exit\nChoose and enter (1-5): "))
        if option1 == 1:
            print("\nFood Category\n1.Rice\n2.Noodle\n3.Side Dishes\n4.Drinks")

            while True:
                userinput = int(input("Enter 0 to go back menu: "))
                if userinput == 0:
                    break

        elif option1 == 2:
            while True:
                print("=" * 20, "Rice", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t\t|Price")

                with open("Rice.txt", "r") as ricefile:
                    readricefile1 = ricefile.readlines()
                    # print (readricefile1)
                    for a in readricefile1:
                        splitRice = a.strip().split(",")
                        # print (splitRice)
                        print(splitRice[0] + "\t" + splitRice[1] + "\t\t" + "RM" + splitRice[2])
                    print("=" * 50)
                    break

            while True:
                print("=" * 20, "Noodle", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t|Price")

                with open("Noodle.txt", "r") as noodlefile:
                    readnoodlefile1 = noodlefile.readlines()
                    # print (readricefile1)
                    for a in readnoodlefile1:
                        splitNoodle = a.strip().split(",")
                        # print (splitRice)
                        print(splitNoodle[0] + "\t" + splitNoodle[1] + "\t\t" + "RM" + splitNoodle[2])
                    print("=" * 50)
                    break

            while True:
                print("=" * 20, "Side Dishes", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t\t|Price")

                with open("SideDishes.txt", "r") as sidedishesfile:
                    readsidedishesfile1 = sidedishesfile.readlines()
                    for a in readsidedishesfile1:
                        splitsidedishes = a.strip().split(",")
                        print(splitsidedishes[0] + "\t" + splitsidedishes[1] + "\t\t\t" + "RM" + splitsidedishes[2])
                    print("=" * 50)
                    break

            while True:
                print("=" * 20, "Drinks", "=" * 25)
                print("ID  |\tFoodName\t\t\t\t|Price")

                with open("Drinks.txt", "r") as drinksfile:
                    readdrinksfile1 = drinksfile.readlines()
                    for a in readdrinksfile1:
                        splitdrinks = a.strip().split(",")
                        print(splitdrinks[0] + "\t" + splitdrinks[1] + "\t\t\t" "RM" + splitdrinks[2])
                    print("=" * 50)
                    break

        elif option1 == 3:
            lineCouter = 1

            while True:

                print("Your Are C", lineCouter,
                      "\nOrder/Nah -- O/N")

                userInput = str(input("Enter O/N: ")).upper()

                if userInput == "O":
                    while True:
                        # print("Order Food :D")
                        print("----------Food Category----------")
                        print("1.Rice\n2.Noodle\n3.Side Dishes\n4.Drinks")

                        orderInput = int(input("Enter Food Code: "))
                        if orderInput == 1:
                            with open("Rice.txt", "r") as riceFile:
                                readRiceFile = riceFile.readlines()
                                for line in readRiceFile:
                                    line = line.strip().split(",")
                                    print(line[0] + "," + line[1] + "," + line[2])
                                orderID = input("Enter Food ID: ")

                                with open("Rice.txt", "r") as RICEFILE:
                                    readRICEFILE = RICEFILE.readlines()
                                    for line in readRICEFILE:
                                        line = line.strip().split(",")

                                        if orderID == line[0]:
                                            print(line[0] + "," + line[1] + "," + line[2])
                                            x = "C" + str(lineCouter) + "," + line[0] + "," + line[1] + "," + line[
                                                2] + "\n"
                                            with open("CustomerOrder.txt", "a") as addRiceFile:
                                                addRiceFile.write(x)

                                    inputDLLM = str(input("Enter Continue/Next_Cust/Exit C/N/E: "))
                                    if inputDLLM == "C":
                                        continue

                                    elif inputDLLM == "N":
                                        print("Next Cust")
                                        lineCouter += 1
                                        break
                                    elif inputDLLM == "E":
                                        fooditem1(userId)
                                        return None
                                    else:
                                        print("Invalid code, Please type the valid code.")


                        elif orderInput == 2:
                            with open("Noodle.txt", "r") as noodleFile:
                                readNoodleFile = noodleFile.readlines()
                                for line in readNoodleFile:
                                    line = line.strip().split(",")
                                    print(line[0] + "," + line[1] + "," + line[2])
                                orderID = input("Enter Food ID: ")

                                with open("Noodle.txt", "r") as NOODLEFILE:
                                    readNOODLEFILE = NOODLEFILE.readlines()
                                    for line in readNOODLEFILE:
                                        line = line.strip().split(",")

                                        if orderID == line[0]:
                                            print(line[0] + "," + line[1] + "," + line[2])
                                            x = "C" + str(lineCouter) + "," + line[0] + "," + line[1] + "," + line[
                                                2] + "\n"
                                            with open("CustomerOrder.txt", "a") as addRiceFile:
                                                addRiceFile.write(x)

                                    inputDLLM = str(input("Enter Continue/Next_Cust/Exit C/N/E: "))
                                    if inputDLLM == "C":
                                        continue

                                    elif inputDLLM == "N":
                                        print("Next Cust")
                                        lineCouter += 1
                                        break
                                    elif inputDLLM == "E":
                                        fooditem1(userId)
                                        return None
                                    else:
                                        print("Invalid code, Please type the valid code.")

                        elif orderInput == 3:
                            with open("SideDishes.txt", "r") as sideDishFile:
                                readSDFile = sideDishFile.readlines()
                                for line in readSDFile:
                                    line = line.strip().split(",")
                                    print(line[0] + "," + line[1] + "," + line[2])

                                orderID = input("Enter Food ID: ")

                                with open("SideDishes.txt", "r") as sideDishFile1:

                                    readSDFile1 = sideDishFile1.readlines()

                                    for line in readSDFile1:
                                        line = line.strip().split(",")

                                        if orderID == line[0]:
                                            print(line[0] + "," + line[1] + "," + line[2])
                                            x = "C" + str(lineCouter) + "," + line[0] + "," + line[1] + "," + line[
                                                2] + "\n"

                                            with  open("CustomerOrder.txt", "a") as appSDFile:
                                                appSDFile.write(x)

                                userInput = str(input("Enter Continue/Next_Cust/Exit C/N/E: "))
                                if userInput == "C":
                                    continue
                                elif (userInput == "N"):
                                    lineCouter += 1
                                    break
                                elif (userInput == "E"):
                                    fooditem1(userId)
                                    return None
                                else:
                                    print("Invalid code, Please type the valid code.")

                        elif orderInput == 4:
                            with open("Drinks.txt", "r") as drinksFIle:
                                readDrinksFile = drinksFIle.readlines()

                                for line in readDrinksFile:
                                    line = line.strip().split(",")

                                    print(line[0] + "," + line[1] + "," + line[2])

                                orderID = input("Enter Food ID: ")

                                with open("Drinks.txt", "r") as drinksFile1:
                                    readDrinksFile1 = drinksFile1.readlines()

                                    for line in readDrinksFile1:
                                        line = line.strip().split(",")

                                        if orderID == line[0]:
                                            print(line[0] + "," + line[1] + "," + line[2])
                                            x = "C" + str(lineCouter) + "," + line[0] + "," + line[1] + "," + line[
                                                2] + "\n"

                                            with open("CustomerOrder.txt", "a") as appDrinks:
                                                appDrinks.write(x)

                                    userInput = str(input("Enter Continue/Next_Cust/Exit C/N/E: "))

                                    if userInput == "C":
                                        continue
                                    elif userInput == "N":
                                        lineCouter += 1
                                        break

                                    elif userInput == "E":
                                        fooditem1(userId)
                                        return None

                                    else:
                                        print("Invalid code, Please type the valid code.")

                        else:
                            print("Invalid code, Please type the valid code.")

                elif userInput == "N":
                    fooditem1(userId)
                    return None

                else:
                    print("Invalid code, Please type the valid code.")
                    fooditem1(userId)
                    return None

        elif option1 == 4:
            print("=" * 20, "Payment", "=" * 25)
            print("You have these in your cart")

            with open("CustomerOrder.txt", "r") as Custorder:

                readCustorder1 = Custorder.readlines()
                # print (readCustorder1)
                for a in readCustorder1:
                    splitCustorder = a.strip().split(",")
                    print(splitCustorder)
                order2 = int(input("Do you wish to proceed? If YES press 1, if NO press 2: "))

                if order2 == 1:

                    with open("CustomerOrder.txt", "r") as paymentFile:
                        readpaymentFile = paymentFile.readlines()

                        total = 0
                        for line in readpaymentFile:
                            line = line.strip().split(",")

                            covert = float(line[3])
                            total += covert

                        print("Your total is:RM", total)
                        print("\nPlease make payment to confirm order.")

                        linecounter = 1

                        print("You are P", linecounter)

                        payby = int(input("\nHow would you like to pay your order?"
                                          "\n1.Online transfer\n2.Credit Card\n3.Debit Card"
                                          "\nPlease Choose Your Option: "))

                        if payby == 1:
                            with open("payment.txt", "a") as paymentfile:
                                paymentfile.write(
                                    "P" + str(linecounter) + "," + userId + "," + "Online transfer" + "," + str(
                                        total) + "\n")
                                print("Thank you for shopping with us, your order is going to arrive in a short while")
                            break

                        elif payby == 2:
                            with open("payment.txt", "a") as paymentfile:
                                paymentfile.write(
                                    "P" + str(linecounter) + "," + userId + "," + "Credit Card" + "," + str(
                                        total) + "\n")
                                print("Thank you for shopping with us, your order is going to arrive in a short while")
                            break

                        elif payby == 3:
                            with open("payment.txt", "a") as paymentfile:
                                paymentfile.write(
                                    "P" + str(linecounter) + "," + userId + "," + "Debit Card" + "," + str(
                                        total) + "\n")
                                print("Thank you for shopping with us, your order is going to arrive in a short while")
                            break

                        else:
                            print("Invalid input, please try again")


                elif order2 == 2:
                    fooditem1(userId)
                    return None

                else:
                    print("Entered invalid number!")

        elif option1 == 5:
            print("Logged out, Thank you, come again!")
            return

        else:
            print("Invalid code entered")


def adminFunction():
    while True:
        time.sleep(1)

        try:
            dataInput = int(input("Enter Code 1/2/3 to Log In Admin/Customer/Exit: "))
            if dataInput == 1:
                print("=" * 50)
                print("1. Login to Access System"
                      "\n2. Add Food Item Category Wise"
                      "\n3. Modify Food Item"
                      "\n4. Display All records of"
                      "\n\t a. Food Category"
                      "\n\t b. Food Items Category wise"
                      "\n\t c. Customer Orders"
                      "\n\t d. Customer Payment"
                      "\n5. Search Specific record of"
                      "\n\t a. Customer Order"
                      "\n\t b. Customer Payment"
                      "\n6. Back ")

                print("=" * 50)
                time.sleep(1)

                try:
                    adminInput = int(input("Enter Code 1/6 to Log In Admin or Back: "))

                    if adminInput == 1:
                        admin_login()

                        while True:

                            accessAdmin = int(input("Enter Code 2-6: "))

                            if accessAdmin == 2:
                                add_FoodItem()
                                continue
                            elif accessAdmin == 3:
                                modify_FoodItem()
                                continue
                            elif accessAdmin == 4:
                                display_Record()
                                continue
                            elif accessAdmin == 5:
                                search_record()
                                continue
                            elif accessAdmin == 6:
                                break
                    elif adminInput == 6:
                        continue

                    else:
                        print("Please Enter 1/6")
                        time.sleep(1)
                        continue

                except ValueError:
                    print("Enter Valid Num")

                    time.sleep(1)
            elif dataInput == 2:
                fooditems()

            elif dataInput == 3:
                exit()

        except ValueError:
            print("Enter Int Number....")


adminFunction()




