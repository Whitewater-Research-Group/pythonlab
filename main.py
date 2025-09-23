#Pythonlab welcome message 

name = input("input your name:")
email = input("input your email:")

message = f"\nHello {name},welcome to Pythonlab!"
message += f"\nwould you like us to send more info to {email}?"

print(message)
options = input("enter y/n:")

if options == 'y':
    print("Thanks for joining pythonlab more info will be sent to you")
elif options == 'n':
    print("Thanks for joining pythonlab")
else:
    print("Enter a valid option")