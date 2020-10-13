#!/usr/bin/env python3.8
from locker import User, Credential

def create_user(name, user_password):
    """
    Parameters
    """
    created_user = User(name, user_password)
    return created_user
