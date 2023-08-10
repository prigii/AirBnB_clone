from models.base_model import BaseModel

"""
Class for creating new users
"""

class User(BaseModel):
    """
    Creates new users and gives them attributes
    """
    def __init__(self, id, email="", password="", first_name="", last_name=""):
        super().__init__(id)
        self.email=email
        self.password=password
        self.first_name=first_name
        self.last_name=last_name
        


