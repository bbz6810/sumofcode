import re


def python_re():
    return re.compile('^\w')


def cpp_re():
    return re.compile('^[#{}\w]')


def c_re():
    return re.compile('^[#{}\w]')


def java_re():
    return re.compile('^[{}\w]')


class Compile:
    def __init__(self):
        self.compile = {
            'python': python_re(),
            'cpp': cpp_re(),
            'c': c_re(),
            'java': java_re(),
        }

    def build(self, types):
        return self.compile[types]
