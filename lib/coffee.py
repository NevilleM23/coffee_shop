class coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(name, str):
            raise TypeErrer("Name should be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 to 15 characters")
        self._name = name
