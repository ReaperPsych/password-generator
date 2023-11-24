import random

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

def create_password(length):
    password = ''
    for i in range(length):
        password = password + random.choice(arr)
    print('Password: ', password)

    site = input("Which site do you want to use the password for? \n")
    website = site

    with open('pass.txt', 'a') as f:
        f.write(f"{website} : {password}\n")

    print("Saved to file pass.txt")
    choice = input("Would you like to generate password again?[y/n]: ")
    if choice.lower() == 'y':
        generate_password()
    else:
        print("Exiting now!")



def generate_password():
    length = input("Enter the length of password you want: ")

    if length.isdigit() and int(length) > 0:
        length = int(length)

        if length < 8:
            ans = input("It is recommended to use a password longer than 8 characters.\nWould you like to try again? If not, the process will resume. [y/n]: ")

            if ans.lower() == 'y':
                generate_password()

            elif ans.lower() == 'n':
                create_password(length)

            else:
                print("Please enter a valid choice: ")
                generate_password()
                
        else:
            create_password(length)


    else:
        print("Please enter a valid positive integer for the password length")
        generate_password()

generate_password()
