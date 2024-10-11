def connect(psd):
    if psd=="TechTitans":
        return True
    else:
        return False

def setup():
    print("Ready to go!!")


def menu(title: str, options: list):
    while True:
        print("\n\n", title)
        for i, j in zip(options, range(1, len(options) + 1)):
            print("\t", j, ". ", i)
        choice = input("\nEnter your choice: ")
        if int(choice) not in range(1, len(options) + 1):
            a = input(
                "\nInvalid Choice. Enter E to exit or any other key to try again\n"
            )
            if a.lower() == "e":
                return 0
        else:
            return int(choice)


psd = input("Enter the connection password: ")

if connect(psd):
    print("\nConnected Successfully!!")
    setup()
    while True:
        ch = menu(
            "Welcome to Upasana Hospital", ["Login as Admin", "Login as Staff", "Exit"]
        )
        if ch == 1:
            usrname = input("Enter ADMIN Username: ")
            pswd = input("Enter ADMIN Password: ")
            #cur.execute("SELECT CURDATE()+5")
            #p = cur.fetchall()[0][0]
            #print(p)
            if usrname == "SADRAP" and pswd == "1234":
                print("\nAdmin Here OMG")
            else:
                print("\nWrong Username or Password")
        elif ch == 2:
            while True:
                ch2 = menu(
                    "Login as: ",
                ["Doctor","Surgeon",
            "Receptionist","Exit"]
            )
                if ch2 == 1:
                    print("Doctor Menu")
                elif ch2== 2:
                    print("Surgeon Menu")
                elif ch2==3:
                    print("Receptionist Menu")
                else:
                    break
        elif ch == 3:
            exch = input(
                """\nAre you sure you want to exit?\n"""
                """Enter Y if YES, or any other key if NO\n"""
            )
            if exch.lower() == "y":
                break
        else:
            break
