import re

from common.tools import train_code_file


class Base:
    def __init__(self, types, re_match):
        self.types = types
        self.re_match = re_match

    def one_file(self, file_name):
        line = 0
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                for i in f.readlines():
                    match = re.match(self.re_match, i.strip())
                    if match:
                        line += 1
        except Exception as e:
            print(e)
        return line

    def all_file(self, file_path):
        line = 0
        all_file = train_code_file(file_path, self.types)
        for file in all_file:
            line += self.one_file(file)
        print('file-->type:{}, num:{}, sums:{}'.format(self.types, len(all_file), line))
