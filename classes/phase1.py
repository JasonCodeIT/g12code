from struct import pack
from classes.baseobject import BaseObject

__author__ = 'Jason Poh'


class InjectionPoint(BaseObject):
    def __init__(self, page, inject_type, param):
        self.page = page
        self.inject_type = inject_type
        self.param = param

    def to_dict(self):
        dictionary = {
            self.page: {
                'type': self.inject_type,
                'param': self.param
            }
        }
        return dictionary