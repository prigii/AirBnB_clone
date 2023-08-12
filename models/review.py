#!/usr/bin/python3
"""
This is the review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This creates the review instances
    """
    place_id = ""
    user_id = ""
    text = ""
