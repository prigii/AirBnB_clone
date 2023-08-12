#!/usr/bin/python3
"""
Class for creating new users
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Creates new users and gives them attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
