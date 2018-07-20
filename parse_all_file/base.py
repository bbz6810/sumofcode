from common.tools import train_all_file


class Base:
    def __init__(self):
        self.file_type = dict()

    def scan_file(self, file_path):
        all_file = train_all_file(file_path)
        for i in all_file:
            suffix = i.split('.')[-1].lower()
            self.file_type[suffix] = self.file_type.setdefault(suffix, 0) + 1
        result = sorted(self.file_type.items(), key=lambda x: x[1], reverse=False)
        for r in result:
            print(r)


if __name__ == '__main__':
    Base().scan_file(r'C:\\')
