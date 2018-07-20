from language.base import Base
from common.re_compile import Compile


class Build:
    def __init__(self, types):
        self.types = types

    def create(self):
        return Base(self.types, Compile().build(self.types))


class CreateFactory:
    @staticmethod
    def get(types):
        return Build(types).create()
