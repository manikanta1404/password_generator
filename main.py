import os
import random
import time
import sys
import string
import csv


def password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    try:
        if length < 8:
            print("Password length should be at least 8 characters.")
            print("Try again")
            return None
        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    try:
        # Ask for inputs
        domain = input("Enter your domain name OR your URL (Website) ==> ")
        user = input("Enter Username ==> ")

        try:
            length = int(input("Enter the length of the password ==> "))
        except ValueError:
            print("Please enter a valid number for the password length.")
            return main()

        # Generate password
        passwd = password_generator(length)

        if passwd is None:
            return main()

        print("Generated Password : ", passwd)
        mydict = [{'domain': domain, 'username': user, 'password': passwd}]

        fields = ['domain', 'username', 'password']

        # Set file path
        filename = "pass_all.csv"

        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # Write header only if the file is empty (first run)
            csvfile.seek(0, 2)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerows(mydict)

        print("Your details are stored in csv file ===> ", os.getcwd() + "\\", filename)
        print("Press Ctrl+C to exit.")

        # Just wait until user presses Ctrl+C
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[+] Program exited by user.")
        sys.exit(0)
    except PermissionError as e:
        print(f"Permission error: {e}. Please check your file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    banner.show_banner("Password Generator ")
    main()
