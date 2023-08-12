#!/usr/bin/env python3
"""
This is the city instance creator
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Creates city of origin instances
    """
    state_id = ""
    name = ""
