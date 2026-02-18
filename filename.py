import random

OTP = random.randint(100000, 999999)
print("Generated OTP:", OTP)
count = 0

verify = int(input("Enter the OTP : "))
while(True):
    if(OTP == verify):
        print("Access Granted 🎉")
        break
    else:
        if(count > 1):
            print("You OTP is expire 😒")
            break
        print("Your entered wrong OTP")
        verify = int(input("Enter the OTP : "))
        count += 1
        continue
