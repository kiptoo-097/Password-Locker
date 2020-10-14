#!/usr/bin/env python3.8
from locker import User, Credential
import getpass
import random
import string

def create_user(name, user_password):
    """
    Parameters
    """
    created_user = User(name, user_password)
    return created_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()

def delete_user(user):
    """
    delete user function
    """
    user.delete_user()


def create_credential(account, acnt_username, acnt_password):
    """
    Parameters
    """
    new_credential = Credential(account, acnt_username, acnt_password)
    return new_credential

def save_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credential
    """
    credential.delete_credential()


def find_credential(acnt_username):
    """
    Function to find credential
    """
    return Credential.find_by_acnt_username(acnt_username)


def check_existing_credentials(acnt_username):
    """
    Function to check existing credential
    ----------
    name
    Returns
    -------
    user
    """
    return Credential.find_by_acnt_username(acnt_username)


def display_credentials():
    """
    Function to display credential
    Returns
    -------
    """
    return Credential.display_all_credentials()
def main():
    
    user_name = input("Enter your name > ")
    print(f"Hi {user_name}, WELCOME!!!!") 
    a_member= input(f"{user_name}.Already a member? YES/N0 > ").lower()

    if a_member == "no":
        print("Wow singnup with us!")
        user_name = input("Please Enter your preferred username..> ")

        p_generate = input(f"{user_name}. Do you we  generate password for you? YES/N0 > ").lower()
        if p_generate == "no":
            print("-"*30)
            print("|Password saved and secure.|")
            print("-"*30)
            getpass.getpass()
            print("PERFECT!! YOU ARE NOW LOGGED IN")

        while True:
            print("""
            USE THE SHORT ABBREVIATION
            cc - to create a new credential
            dc - to display credential
            fc - to find credential
            xx - to delete credential
            rp - random password
            """)
            nav_code = input("Navigate using short codes > ").lower()

            if nav_code == "cc":
                print(" Creating Account")
                print("-" * 22)

                print("Account?")
                account = input("> ")

                print("Username ?")
                acnt_username = input("> ")

                print("Enter Password")
                acnt_password = input("> ")

                save_credential(create_credential(account, acnt_username, acnt_password))

                print("\n")
                print("SUCCESS!")
                print(f"New Credential {account} {acnt_username} {acnt_password} created!")
                print("\n")

            elif nav_code == "rp":
                print( "Enter the account you want to generate > ")
                media_acc = input("Enter media account Type > ")

                def random_password(string_length):
                    """
                    Parameters
                    ----------
                    string_length
                    Returns
                    -------
                    """
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))

                print("Your random password for {media_acc} is: ", random_password(7))

            elif nav_code == "dc":

                if display_credentials():
                    print("Here is a list of all your Credentials and passwords")
                    print("\n")
                    for credential in display_credentials():
                        print(f"{credential.account} {credential.acnt_username}{acnt_password}")
                        print("\n")
                else:
                    print("\n")
                    print("Not saved? Try saving one")
                    print("\n")

            elif nav_code == 'fc':

                print("Enter username?")

                search_acnt_username = input()
                if check_existing_credentials(search_acnt_username):
                    search_credential = find_credential(search_acnt_username)
                    print(f"{search_credential.account} {search_credential.acnt_username}")
                    print('-' * 20)

                    print(f"password.......{search_credential.acnt_password}")

                else:
                    print("It does not exist..Try creating One")

            elif nav_code == "xx":
                print("Enter the account username of the Account to be deleted.")
                delete_acc = input("> ")
                my_del = find_credential(delete_acc)
                Credential.credential_list.remove(my_del)
                print(f"{delete_acc} Deleted succefully")
            elif nav_code == "ex":
                print("Logged out")
                break

    elif a_member == "yes":
        print("Enter your username and password to login")
        user_name = input()
        print("-"*30)
        print("-"*30)
        acnt_password= getpass.getpass()

        while True:
            print("""
            USE THE SHORT ABBREVIATION BELOW
            cc - to create a new credential
            dc - to display credential
            fc - to find credential
            xx - to delete credential
            rp - random password
            """)

            nav_code = input("Navigate using short codes> ").lower()

            if nav_code == "cc":
                print(" Create account")
                print("-" * 12)

                print("Account ....")
                account = input("> ")

                print("username ....")
                acnt_username = input("> ")

                print("Enter Password")
                acnt_password = input("> ")

                save_credential(create_credential(account, acnt_username, acnt_password))

                print("\n")
                print(f"New Credential {account} {acnt_username} {acnt_password} has been created")
                print("\n")

            elif nav_code == "rp":
                print(
                    "Please enter the account you want to generate password for > ")
                media_acc = input("Enter account type > ")

                def random_password(string_length):
                    """
                    Parameters
                    """
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))

                print(
                    f"Your random password for {media_acc} is: ", random_password(7))

            elif nav_code == "dc":

                if display_credentials():
                    print("Your Credentials and passwords are")
                    print("\n")
                    for credential in display_credentials():
                        print(f"{credential.account} {credential.acnt_username}{acnt_password}")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "You don't have any saved credentials yet. Try saving one")
                    print("\n")

            elif nav_code == 'fc':

                print("Enter the account username you want to search for")

                search_acnt_username = input()
                if check_existing_credentials(search_acnt_username):
                    search_credential = find_credential(search_acnt_username)
                    print(f"{search_credential.account} {search_credential.acnt_username}")
                    print('-' * 20)

                    print(f"Account password.......{search_credential.acnt_password}")

                else:
                    print("That credential does not exist")

            elif nav_code == "xx":
                print("Enter the username of the credential you would like to delete.")
                print("Confirm delete")
                delete_acc = input("> ")
                my_del = find_credential(delete_acc)
                Credential.credential_list.remove(my_del)
                print(
                    f"Credential with  account username {delete_acc} has been removed succefully")
            elif nav_code == "ex":
                print("Logged out")
                break

    else:
        print("Kindly check your entries and try again.")

if __name__ == "__main__":
    main()