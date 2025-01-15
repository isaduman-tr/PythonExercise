db_ps = 12345
db_un = "isa"

UserName = input("User Name :")
Password = int(input("Password :"))

Control = UserName==db_un and Password==db_ps

if Control == True:
    print("Welcome brother come in!!!")
else:
    print("Not you brother try again")

