from models.base_model import BaseModel
"""
This is the review class
"""
class Review:
    """
    This creates the review instances
    """
    def __init__(self, place_id, user_id, text):
        self.Place.id=str(place_id)
        self.User.id=str(user_id)
        self.text=str(text)
        
