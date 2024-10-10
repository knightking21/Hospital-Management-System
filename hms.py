import mysql.connector as sql


def connect(pswd: str, usr: str = "root"):
    global mydb, cur
    mydb = sql.connect(host="localhost", user=usr, passwd=pswd)
    if mydb.is_connected():
        cur = mydb.cursor()
        return True
    else:
        return False


def setup():
    global cur
    cur.execute("create database if not exists hms")
    cur.execute("use hms")
    # cur.execute("""create table if not exist""" """settings()""")
    cur.execute(
        """create table if not exists """
        """specialisation(SPECID int PRIMARY KEY AUTO_INCREMENT, SPECNAME varchar(25) NOT NULL)"""
    )
    cur.execute(
        """create table if not exists """
        """patients(PATID int(3) AUTO_INCREMENT PRIMARY KEY, NAME varchar(50) NOT NULL,"""
        """AGE int NOT NULL, GENDER varchar(10) NOT NULL, CONTACT varchar(10) NOT NULL,"""
        """ADDRESS varchar(25) NOT NULL, RID int NOT NULL REFERENCES room(RID),"""
        """DOCID int NOT NULL REFERENCES doctors(DOCID), SURID int REFERENCES surgeons(SURID),"""
        """NURID int NOT NULL REFERENCES nurses(NURID), AMOUNT int DEFAULT 0,"""
        """ADMIT_DATE date NOT NULL) AUTO_INCREMENT=1000"""
    )
    cur.execute(
        """create table if not exists """
        """doctors(DOCID int AUTO_INCREMENT PRIMARY KEY, NAME varchar(50) NOT NULL,"""
        """AGE int NOT NULL, GENDER varchar(10) NOT NULL, CONTACT varchar(10) NOT NULL,"""
        """ADDRESS varchar(25) NOT NULL, SPECID int NOT NULL REFERENCES specialisation(SPECID),"""
        """SALARY int NOT NULL, JOIN_DATE date NOT NULL) AUTO_INCREMENT=100"""
    )
    cur.execute(
        """create table if not exists """
        """surgeons(SURID int AUTO_INCREMENT PRIMARY KEY, NAME varchar(50) NOT NULL,"""
        """AGE int NOT NULL, GENDER varchar(10) NOT NULL, CONTACT varchar(10) NOT NULL,"""
        """ADDRESS varchar(25) NOT NULL, SPECID int NOT NULL REFERENCES specialisation(SPECID),"""
        """SALARY int NOT NULL, JOIN_DATE date NOT NULL) AUTO_INCREMENT=100"""
    )
    cur.execute(
        """create table if not exists """
        """nurses(NURID int AUTO_INCREMENT PRIMARY KEY, NAME varchar(50) NOT NULL,"""
        """AGE int NOT NULL, GENDER varchar(10) NOT NULL, CONTACT varchar(10) NOT NULL,"""
        """ADDRESS varchar(25) NOT NULL,"""
        """SALARY int NOT NULL, JOIN_DATE date NOT NULL) AUTO_INCREMENT=100"""
    )
    cur.execute(
        """create table if not exists """
        """other_staffs(OTHID int AUTO_INCREMENT PRIMARY KEY, NAME varchar(50) NOT NULL,"""
        """AGE int NOT NULL, GENDER varchar(10) NOT NULL, CONTACT varchar(10) NOT NULL,"""
        """ADDRESS varchar(25) NOT NULL, OCCUPATION varchar(25) NOT NULL,"""
        """SALARY int NOT NULL, JOIN_DATE date NOT NULL) AUTO_INCREMENT=100"""
    )
    # cur.execute("""create table if not exists """ """room()""")
    # cur.execute("""create table if not exists """ """treatments()""")
    # cur.execute("""create table if not exists """ """surgeries()""")


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
            cur.execute("SELECT CURDATE()+5")
            p = cur.fetchall()[0][0]
            print(p)
            if usrname == "SADRAP" and pswd == str(p):
                print("\nAdmin Here OMG")
            else:
                print("\nWrong Username or Password")
        elif ch == 2:
            print("Staffs Here")
        elif ch == 3:
            exch = input(
                """\nAre you sure you want to exit?\n"""
                """Enter Y if YES, or any other key if NO\n"""
            )
            if exch.lower() == "y":
                break
        else:
            break
