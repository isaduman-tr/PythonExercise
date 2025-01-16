# db_ps = 12345
# db_un = "isa"

# UserName = input("User Name :")
# Password = int(input("Password :"))

# Control = UserName==db_un and Password==db_ps

# if Control == True:
#     print("Welcome brother come in!!!")
# else:
#     print("Not you brother try again")

#########################################################

# while True:
#     Username = input("User name : ")
#     password = int(input("Password : "))
#     if  db_ps==password and db_un==Username:
#         print("Welcome!: " , db_un)   
#         break
#     elif db_ps ==password and db_un!=Username:
#         print("username is wrong")
#     elif db_ps!=password and db_un==Username:
#         print("PASSWORD is wrong")
#         print("Change passwords? : Y/N")
#         Answer = input()
#         if Answer =="Y":
#             NewPassword = int(input("New Password:"))
#             db_ps = NewPassword
#     else:
#         print("Username and password is wrong")

##########################################################

# for i in range(3):
#     Password = input("Password: ")
#     if not Password :
#         print("You must write a password")
#     elif len(Password)in range(3,8):
#         print("Your password :" ,Password)
#         break
#     elif i == 2:
#         print("You are wrong 3 times please try again 15 minutes later :")
#     else :
#         print("Your password lenght not 3 or 8")    

def topla():
    a = int(input("First number :"))
    b = int(input("Second number :"))
    toplam = a+b
    print(toplam)

topla()