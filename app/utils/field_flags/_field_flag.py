"""
Defines the class that represents operations over fields.
"""


class FieldFlag():

    """
    Represents operations over fields.
    """

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return repr(self)
    
    def __eq__(self, other):
        return isinstance(other, FieldFlag) and self.name == other.name
    
    def __hash__(self):
        return hash((FieldFlag, self.name))


DELETE_FLAG = FieldFlag('DELETE')
IGNORE_FLAG = FieldFlag('IGNORE')