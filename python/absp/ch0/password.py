password_file = open("password.txt")
password = password_file.read()

entered_password = input("Enter password: ")
if entered_password != password:
    print("Access Denied")
else:
    print("Access Granted")
    if password == "123" or password == "1234" or password == "12345":
        print("That's a very simple password")

