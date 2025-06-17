import uuid


class User:
    def __init__(self,
                 id,
                 name,
                 email,
                 is_active: bool = True
                 ):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active



