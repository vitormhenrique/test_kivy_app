from enum import Enum


class ChoicesEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def fromValue(cls, value):
        return [c for c in cls if c.value[0]==value].pop()

    @property
    def key_text(self):
        return self.value[1]

    @property
    def key_value(self):
        return self.value[0]

