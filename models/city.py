from models.base_model import BaseModel

"""
This is the city instance creator
"""
class City:
    """
    Creates city of origin instances
    """
    def __init__(self, state_id, name):
        self.State.id=state_id
        self.name=name
        