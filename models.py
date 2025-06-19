import uuid
from datetime import datetime


class User:
    def __init__(self,
                 id: int,
                 name: str,
                 email: str,
                 is_active: bool = True
                 ):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active


class Event:
    def __init__(self,
                 id: int,
                 name: str,
                 title: str,
                 location: str,
                 date: str,
                 is_open: bool = True):
        self.id = id
        self.name = name
        self.title = title
        self.location = location
        self.date = date
        self.is_open: is_open
