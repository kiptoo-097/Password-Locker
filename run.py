#!/usr/bin/env python3.8
from locker import User, Credential

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